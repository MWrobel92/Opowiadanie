import re
import sys

from zmienne import KuferekZmiennych
from instrukcje import utwórz_główną_instrukcję, ALFABET
from wyliczanki import Warunek
from bledy import BłądObsłużony

def przetwórz_tekst(zbiór_tekstów: dict, tytuł: str, wejście=[], wypisz=True):
    tekst = zbiór_tekstów[tytuł]

    zmienne = KuferekZmiennych()
    zmienne.włóż('Zapłata', wejście, 'aaa')
    instrukcja, _ = utwórz_główną_instrukcję(zmienne)

    koniec_zdania = r'[\.!]\s+'

    koniec_akapitu = '\n\n'
    akapity = tekst.strip().split(koniec_akapitu)

    for akapit in akapity:
        zdania = re.split(koniec_zdania, akapit)

        znacznik = 0
        punkty_powrotu = []
        while znacznik < len(zdania):
            zdanie = zdania[znacznik]
            try:
                wynik = instrukcja.parse_string(zdanie)
                if type(wynik[0]) is Warunek:
                    if wynik[0] == Warunek.NIESPEŁNIONY:
                        break
                    elif wynik[0] == Warunek.SPEŁNIONY_PĘTLA:
                        punkty_powrotu.append(znacznik)
                elif type(wynik[0]) is tuple:
                    nazwa, czasownik, funkcja, argument = wynik[0]
                    do_przekazania = zmienne.wyjmij(argument, biernik=True)
                    wynik = przetwórz_tekst(zbiór_tekstów, funkcja, do_przekazania, False)
                    zmienne.włóż(nazwa, wynik, czasownik)
            except Exception as błąd:
                print("========== Ponieśliśmy porażkę ==========")
                print(f"Błąd w zdaniu: \"{zdanie}\" ({type(błąd).__name__})")
                if not isinstance(błąd, BłądObsłużony):
                    print("Toż tego bełkotu nie da się czytać!")
                    print("Może ten techniczny żargon coś pomoże...")
                print(błąd)
                return
            znacznik += 1
            if (znacznik == len(zdania)) and len(punkty_powrotu) > 0:
                znacznik = punkty_powrotu.pop()
    if wypisz:
        print(zmienne)

    return zmienne.wyjmij(zmienne.ostatnio_używana)


def wczytaj_kod(nazwa_pliku: str):

    wczytane_rozdziały = {}

    with open(nazwa_pliku) as pliczek:

        nazwa_rozdziału = ''
        treść_rozdziału = ''
        reguła_nazwy = f'[{ALFABET}]+\n'

        for linia in pliczek:

            if re.match(reguła_nazwy, linia) is not None:
                if len(treść_rozdziału) > 0:
                    wczytane_rozdziały[nazwa_rozdziału] = treść_rozdziału
                nazwa_rozdziału = linia[:-1]
                treść_rozdziału = ''
            else:
                treść_rozdziału += linia

        if len(treść_rozdziału) > 0:
            wczytane_rozdziały[nazwa_rozdziału] = treść_rozdziału

    return wczytane_rozdziały

parametry = sys.argv

if len(parametry) < 2:
    print('Nie podano nazwy pliku z kodem źródłowym do uruchomienia!')
else:
    księgozbiór = wczytaj_kod(parametry[1])
    if len(księgozbiór) == 0:
        print('Tu nic nie ma')
    else:
        przetwórz_tekst(księgozbiór, list(księgozbiór)[-1], parametry[2:])