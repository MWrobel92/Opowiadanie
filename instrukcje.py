from pyparsing import Word, Literal, CaselessLiteral as cl
from copy import deepcopy

from liczba import liczba, bz
from zmienne import KuferekZmiennych
from bledy import BłądDzienieniaPrzezZero, BłądTypu
from wyliczanki import Warunek


ALFABET = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻaąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'


def utwórz_główną_instrukcję(zmienne: KuferekZmiennych):
    słowo = Word(ALFABET)
    napis = Word(ALFABET + ', \n1234567890')
    dwukropek = Literal(':')
    kropka = Literal('.') | Literal('!')

    def przypisz_liczbę(tokeny):
        zmienne.włóż(tokeny[0], tokeny[4], tokeny[2])
    miał_liczył = cl('miało') | cl('miała') | cl('miał') | \
        cl('liczyło') | cl('liczyła') | cl('liczył')
    przypisanie_liczby = słowo + bz + miał_liczył + bz + liczba + bz + słowo
    przypisanie_liczby.leave_whitespace()
    przypisanie_liczby.set_parse_action(przypisz_liczbę)

    def przypisz_napis(tokeny):
        nazwa, _, czasownik, _, _, wartość = tokeny
        if czasownik.startswith('krzyk'):
            wartość = wartość + '!'
        zmienne.włóż(nazwa, wartość, czasownik)
    powiedział = cl('powiedziało') | cl('powiedziała') | cl('powiedział') | \
        cl('krzyknął') | cl('krzyknęła') | cl('krzyknęło')
    przypisanie_napisu = słowo + bz + powiedział + dwukropek + bz + napis
    przypisanie_napisu.leave_whitespace()
    przypisanie_napisu.set_parse_action(przypisz_napis)

    def przypisz_pusty_napis(tokeny):
        nazwa, _, czasownik = tokeny
        zmienne.włóż(nazwa, '', czasownik)
    milczał = cl('milczało') | cl('milczała') | cl('milczał')
    przypisanie_pustego_napisu = słowo + bz + milczał
    przypisanie_pustego_napisu.leave_whitespace()
    przypisanie_pustego_napisu.set_parse_action(przypisz_pusty_napis)

    def przypisz_kolekcję_jednoelementową(tokeny):
        nazwa_zmiennej, _, czasownik, _, _ = tokeny
        wartość = zmienne.wyjmij(nazwa_zmiennej, czasownik)
        zmienne.włóż(nazwa_zmiennej, [wartość], czasownik)
    lubił = cl('lubiło') | cl('lubiła') | cl('lubił')
    przypisanie_kolekcji_1_elementowej = słowo + bz + lubił + bz + cl('samotność')

    przypisanie_kolekcji_1_elementowej.leave_whitespace()
    przypisanie_kolekcji_1_elementowej.set_parse_action(przypisz_kolekcję_jednoelementową)

    def przypisz_kolekcję_dwuelementową(tokeny):
        nazwa, _, czasownik, _, pierwsza, _, _, _, druga = tokeny
        if pierwsza == 'siebie':
            pierwsza = nazwa
        if druga == 'siebie':
            druga = nazwa
        kolekcja = [zmienne.wyjmij(nazwa_zmiennej, biernik=True) for nazwa_zmiennej
                    in [pierwsza, druga]]
        zmienne.włóż(nazwa, kolekcja, czasownik)
    zgrupował = cl('zgrupowało') | cl('zgrupowała') | cl('zgrupował')
    ii = cl('i')
    przypisanie_kolekcji_2_elementowej = słowo + bz + zgrupował + bz + słowo + bz + ii + bz + słowo
    przypisanie_kolekcji_2_elementowej.leave_whitespace()
    przypisanie_kolekcji_2_elementowej.set_parse_action(przypisz_kolekcję_dwuelementową)

    def wypisz_zmienną(tokeny):
        wartość = zmienne.wyjmij(tokeny[0], tokeny[2])
        print(wartość)
    wyjawił = cl('wyjawiło') | cl('wyjawiła') | cl('wyjawił')
    wypisanie_zmiennej = słowo + bz + wyjawił + bz + \
        cl('swój') + bz + cl('sekret')
    wypisanie_zmiennej.leave_whitespace()
    wypisanie_zmiennej.set_parse_action(wypisz_zmienną)

    def ustaw_biernik(tokeny):
        zmienne.ustaw_biernik(tokeny[-1])
    to = cl('to')
    ustawienie_biernika = to + bz + cl('wyróżniało') + bz + słowo
    ustawienie_biernika.leave_whitespace()
    ustawienie_biernika.set_parse_action(ustaw_biernik)

    def wykonaj_działanie(tokeny):
        nazwa, _, czynność, _, składnik_1, _, _, _, składnik_2 = tokeny
        if składnik_1 == 'siebie':
            składnik_1 = nazwa
        if składnik_2 == 'siebie':
            składnik_2 = nazwa
        wartość_1 = zmienne.wyjmij(składnik_1, biernik=True)
        wartość_2 = zmienne.wyjmij(składnik_2, biernik=True)
        try:
            if czynność.startswith('d'):
                wynik = wartość_1 + wartość_2
            elif czynność.startswith('o'):
                wynik = wartość_1 - wartość_2
            elif czynność.startswith('pom'):
                wynik = wartość_1 * wartość_2
            elif czynność.startswith('pod'):
                wynik = wartość_1 / wartość_2
            elif czynność.startswith('r'):
                wynik = wartość_1 // wartość_2
            elif czynność.startswith('o'):
                wynik = wartość_1 // wartość_2
            elif czynność.startswith('s'):
                wynik = wartość_1 ** wartość_2
            zmienne.włóż(nazwa, wynik, czynność)
        except TypeError:
            zmienna_1 = zmienne.weź_mianownik(składnik_1)
            zmienna_2 = zmienne.weź_mianownik(składnik_2)
            raise BłądTypu(zmienna_1, zmienna_2)
        except ZeroDivisionError:
            zmienna_2 = zmienne.weź_mianownik(składnik_2)
            raise BłądDzienieniaPrzezZero(zmienna_2)
    operator = (
        cl('dodało') | cl('dodała') | cl('dodał') |
        cl('odjęło') | cl('odjęła') | cl('odjął') |
        cl('pomnożyło') | cl('pomnożyła') | cl('pomnożył') |
        cl('podzieliło') | cl('podzieliła') | cl('podzielił') |
        cl('rodzieliło') | cl('rozdzieliła') | cl('rozdzielił') |
        cl('obcięło') | cl('obcięła') | cl('obciął') |
        cl('spotęgowało') | cl('spotęgowała') | cl('spotęgował')
    )
    wykonanie_działania = słowo + bz + operator + bz + słowo + bz + ii + bz + słowo
    wykonanie_działania.leave_whitespace()
    wykonanie_działania.set_parse_action(wykonaj_działanie)

    def inkrementuj(tokeny):
        nazwa, _, czasownik, _, _ = tokeny
        wartość = zmienne.wyjmij(nazwa)
        if czasownik[1] == 'm':
            nowa = wartość - 1
        else:
            nowa = wartość + 1
        zmienne.włóż(nazwa, nowa, czasownik)
    się = cl('się')
    zmniejszył = (
        cl('zmniejszyło') | cl('zmniejszyła') | cl('zmniejszył') |
        cl('zwiększyło') | cl('zwiększyła') | cl('zwiększył')
    )
    inkrementacja = słowo + bz + zmniejszył + bz + się
    inkrementacja.leave_whitespace()
    inkrementacja.set_parse_action(inkrementuj)

    def zmierz_długość(tokeny):
        nazwa, _, czasownik, _, zmienna = tokeny
        if zmienna == 'siebie':
            zmienna = nazwa
        wartość = zmienne.wyjmij(zmienna, biernik=True)
        if type(wartość) is str or type(wartość) is list:
            długość = len(wartość)
        else:
            długość = abs(wartość)
        zmienne.włóż(nazwa, długość, czasownik)
    zmierzył = cl('zmierzyło') | cl('zmierzyła') | cl('zmierzył')
    pobranie_długości = słowo + bz + zmierzył + bz + słowo
    pobranie_długości.leave_whitespace()
    pobranie_długości.set_parse_action(zmierz_długość)

    def wyłuskaj_wartość(tokeny):
        nazwa, _, czasownik, _, zmienna = tokeny
        if zmienna == 'siebie':
            zmienna = nazwa
        napis = zmienne.wyjmij(zmienna, biernik=True)
        wartość = int(napis)
        zmienne.włóż(nazwa, wartość, czasownik)
    odczytał = cl('odczytało') | cl('odczytała') | cl('odczytał')
    zrzutowanie = słowo + bz + odczytał + bz + słowo
    zrzutowanie.leave_whitespace()
    zrzutowanie.set_parse_action(wyłuskaj_wartość)

    def odwróć(tokeny):
        nazwa, _, czasownik = tokeny
        wartość = zmienne.wyjmij(nazwa)
        if type(wartość) is list:
            nowa = [i for i in reversed(wartość)]
        elif type(wartość) is str:
            nowa = ''.join(reversed(wartość))
        else:
            nowa = -wartość
        zmienne.włóż(nazwa, nowa, czasownik)
    zawrócił = cl('zawróciło') | cl('zawróciła') | cl('zawrócił')
    odwrócenie = słowo + bz + zawrócił
    odwrócenie.leave_whitespace()
    odwrócenie.set_parse_action(odwróć)

    def pobierz_element(tokeny):
        nazwa, _, czasownik, _, kolekcja, _, _, _, indeks = tokeny
        if kolekcja == 'siebie':
            kolekcja = nazwa
        if indeks == 'siebie':
            indeks = nazwa
        kolekcja_obj = zmienne.wyjmij(kolekcja, biernik=True)
        indeks_obj = zmienne.wyjmij(indeks, biernik=True)
        element = kolekcja_obj[indeks_obj]
        zmienne.włóż(nazwa, element, czasownik)
    wyjął = cl('wyjęło') | cl('wyjęła') | cl('wyjął')
    pobranie_elementu = słowo + bz + wyjął + bz + słowo + bz + ii + bz + słowo
    pobranie_elementu.leave_whitespace()
    pobranie_elementu.set_parse_action(pobierz_element)

    def kopiuj(tokeny):
        nazwa, _, czasownik, _, zmienna = tokeny
        if zmienna == 'siebie':
            return
        wartość = zmienne.wyjmij(zmienna, biernik=True)
        zmienne.włóż(nazwa, deepcopy(wartość), czasownik)
    naśladował = cl('naśladowało') | cl('naśladowała') | cl('naśladował')
    skopiowanie = słowo + bz + naśladował + bz + słowo
    skopiowanie.leave_whitespace()
    skopiowanie.set_parse_action(kopiuj)

    def sprawdź_warunek(tokeny):
        nazwa, _, czasownik, _, _ = tokeny
        wartość = zmienne.wyjmij(nazwa, czasownik)
        if type(wartość) is str or type(wartość) is list:
            wynik = (len(wartość) > 0)
        else:
            wynik = (wartość > 0)
        return Warunek.SPEŁNIONY if wynik else Warunek.NIESPEŁNIONY
    sprawdził = cl('sprawdziło') | cl('sprawdziła') | cl('sprawdził')
    instrukcja_warunkowa = słowo + bz + sprawdził + bz + się
    instrukcja_warunkowa.leave_whitespace()
    instrukcja_warunkowa.set_parse_action(sprawdź_warunek)

    def sprawdź_warunek_pętli(tokeny):
        nazwa, _, czasownik, _, _ = tokeny
        wartość = zmienne.wyjmij(nazwa, czasownik)
        if type(wartość) is str or type(wartość) is list:
            wynik = (len(wartość) > 0)
        else:
            wynik = (wartość > 0)
        return Warunek.SPEŁNIONY_PĘTLA if wynik else Warunek.NIESPEŁNIONY
    przejął = cl('przejęło') | cl('przejęła') | cl('przejął')
    dowodzenie = cl('dowodzenie') | cl('kontrolę')
    pętla = słowo + bz + przejął + bz + dowodzenie
    pętla.leave_whitespace()
    pętla.set_parse_action(sprawdź_warunek_pętli)

    def przywołaj_zmienną(tokeny):
        zmienne.wyjmij(tokeny[0])
    wyszedł = cl('wyszło') | cl('wyszła') | cl('wyszedł')
    przywołanie_zmiennej = słowo + bz + wyszedł + bz + cl('na') + bz + cl('środek')
    przywołanie_zmiennej.leave_whitespace()
    przywołanie_zmiennej.set_parse_action(przywołaj_zmienną)

    def wywołaj_funkcję(tokeny):
        nazwa, _, czasownik, _, funkcja, _, _, _, argument = tokeny
        return nazwa, czasownik, funkcja, argument
    objął = cl('objęło') | cl('objęła') | cl('objął')
    wywołanie_funkcji = słowo + bz + objął + bz + słowo + bz + ii + bz + słowo
    wywołanie_funkcji.leave_whitespace()
    wywołanie_funkcji.set_parse_action(wywołaj_funkcję)

    instrukcja = (przypisanie_liczby | przypisanie_napisu | przypisanie_pustego_napisu |
                  przypisanie_kolekcji_1_elementowej | przypisanie_kolekcji_2_elementowej |
                  wykonanie_działania | wypisanie_zmiennej | ustawienie_biernika | inkrementacja |
                  pobranie_długości | zrzutowanie | odwrócenie | pobranie_elementu | skopiowanie |
                  instrukcja_warunkowa | pętla | przywołanie_zmiennej | wywołanie_funkcji)
    instrukcja_zdanie = instrukcja + kropka

    return instrukcja, instrukcja_zdanie