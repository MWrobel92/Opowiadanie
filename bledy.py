from wyliczanki import Rodzaj


class BłądObsłużony(Exception):
    def __init__(self, wiadomość: str):
        super().__init__(wiadomość)


class BłądTypu(BłądObsłużony):
    def __init__(self, zmienna_1: str, zmienna_2: str):
        super().__init__(f'Nie można wykonać działania! {zmienna_1.capitalize()} '
                         f'i {zmienna_2.capitalize()} są z różnych parafii')


class BłądDzienieniaPrzezZero(BłądObsłużony):
    def __init__(self, zmienna: str):
        super().__init__(f'Nie można wykonać dzielenia! {zmienna.capitalize()} jest zerem')


class BłądRodzaju(BłądObsłużony):
    def __init__(self, zmienna: str, stary_rodzaj: Rodzaj, nowy_rodzaj: Rodzaj):
        if stary_rodzaj == Rodzaj.MĘSKI:
            niego = 'niego'
            był = 'był'
        elif stary_rodzaj == Rodzaj.ŻEŃSKI:
            niego = 'jej'
            był = 'była'
        else:
            niego = 'niego'
            był = 'było'
        starego = stary_rodzaj.value + 'ego'
        nowego = nowy_rodzaj.value + 'ego'
        wiadomość = f'Cóż za nietakt! {zmienna.capitalize()} jest rodzaju {starego}, tymczasem' + \
            f' zwrócono się do {niego} jakby {był} rodzaju {nowego}'
        super().__init__(wiadomość)


class BłądNazwy(BłądObsłużony):
    def __init__(self, zmienna: str):
        super().__init__(f'{zmienna.capitalize()} nie istnieje! To smutne')


class BłądBrakuOstatniej(BłądObsłużony):
    def __init__(self):
        super().__init__(f'O kogo może chodzić? Nie utworzono jeszcze żadnej zmiennej')