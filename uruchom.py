import sys

from kod.glowne import wczytaj_kod, przetwórz_tekst

parametry = sys.argv

if len(parametry) < 2:
    print('Nie podano nazwy pliku z kodem źródłowym do uruchomienia!')
else:
    księgozbiór = wczytaj_kod(parametry[1])
    if len(księgozbiór) == 0:
        print('Tu nic nie ma')
    else:
        przetwórz_tekst(księgozbiór, list(księgozbiór)[-1], parametry[2:])