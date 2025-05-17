from .wyliczanki import Rodzaj
from .bledy import BłądRodzaju, BłądBrakuOstatniej, BłądNazwy


def określ_rodzaj(czasownik_wprowadzający: str) -> Rodzaj:
    if czasownik_wprowadzający.endswith('a'):
        return Rodzaj.ŻEŃSKI
    if czasownik_wprowadzający.endswith('o'):
        return Rodzaj.NIJAKI
    return Rodzaj.MĘSKI


class Zmienna:
    def __init__(self, wartość, rodzaj: Rodzaj):
        self.wartość = wartość
        self.rodzaj = rodzaj


class KuferekZmiennych:
    def __init__(self):
        self.zmienne = {}
        self.bierniki = {}
        self.ostatnio_używana = None

    def __str__(self):
        cały_napis = ''
        for nazwa, zmienna in self.zmienne.items():
            napis_zmiennej = f'{nazwa.capitalize()} (rodzaj {zmienna.rodzaj.value}'
            bierniki = [b.capitalize() for b in self.bierniki if self.bierniki[b] == nazwa]
            if len(bierniki) > 0:
                napis_zmiennej += '; w bierniku '
                napis_zmiennej += ', '.join(bierniki)
            napis_zmiennej += f'): {zmienna.wartość}\n'
            cały_napis += napis_zmiennej
        if len(cały_napis) == 0:
            cały_napis = 'Tu nic nie ma!\n'
        return cały_napis

    def włóż(self, nazwa: str, wartość, czasownik_wprowadzający: str) -> None:
        nazwa = nazwa.lower()
        if nazwa in ['potem', 'następnie', 'ponadto']:
            nazwa = self.ostatnio_używana
        rodzaj = określ_rodzaj(czasownik_wprowadzający)
        if nazwa in self.zmienne:
            if rodzaj == self.zmienne[nazwa].rodzaj:
                self.zmienne[nazwa].wartość = wartość
                self.ostatnio_używana = nazwa
            else:
                raise BłądRodzaju(nazwa, self.zmienne[nazwa].rodzaj, rodzaj)
        else:
            self.zmienne[nazwa] = Zmienna(wartość, rodzaj)
            self.ostatnio_używana = nazwa
            if nazwa.endswith('a'):
                self.bierniki[nazwa[:-1] + 'ę'] = nazwa
            elif rodzaj == Rodzaj.MĘSKI:
                self.bierniki[nazwa + 'a'] = nazwa

    def wyjmij(self, nazwa: str, czasownik_wprowadzający: str = '', biernik: bool = False):
        nazwa = nazwa.lower()
        if nazwa in ['potem', 'następnie', 'ponadto']:
            nazwa = self.ostatnio_używana
        if biernik and nazwa in self.bierniki:
            self.ostatnio_używana = self.bierniki[nazwa]
            return self.zmienne[self.bierniki[nazwa]].wartość
        if nazwa in self.zmienne:
            if czasownik_wprowadzający == '':
                self.ostatnio_używana = nazwa
                return self.zmienne[nazwa].wartość
            rodzaj = określ_rodzaj(czasownik_wprowadzający)
            if rodzaj == self.zmienne[nazwa].rodzaj:
                self.ostatnio_używana = nazwa
                return self.zmienne[nazwa].wartość
            else:
                raise BłądRodzaju(nazwa, self.zmienne[nazwa].rodzaj, rodzaj)
        else:
            raise BłądNazwy(nazwa)

    def ustaw_biernik(self, biernik: str):
        if self.ostatnio_używana is None:
            raise BłądBrakuOstatniej()
        else:
            self.bierniki[biernik.lower()] = self.ostatnio_używana

    def weź_mianownik(self, biernik: str):
        mały = biernik.lower()
        if mały in self.bierniki:
            return self.bierniki[mały]
        else:
            return mały
