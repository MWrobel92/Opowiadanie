**Opowiadanie** to język programowania umożliwiający pisanie kodu źródłowego piękną polszczyzną.

Niniejsze repozytorium zawiera kod źródłowy interpretera języka *Opowiadanie* napisany w języku
*Python*.

# Instrukcja obsługi

Aby uruchomić interpreter trzeba mieć zainstalowanego Pythona oraz pakiet
[https://pypi.org/project/pyparsing/ pyparsing]. Kod był testowany w środowisku z językiem
*Python* w wersji 3.10.12 i pakietem *pyparsing* w wersji 3.2.0.

W celu uruchomienia interpretera należy pobrać zawartośc repozytorium, uruchomić terminal w głównym
folderze i wpisać komendę:

> `python uruchom.py <plik z kodem> <argumenty programu (opcjonalnie)>`

Przykładowe polecenia:

> `python uruchom.py przyklady/witaj.opo`

> `python uruchom.py przyklady/silnia.opo 12`


# Specyfikacja języka

## Informacje ogólne

Instrukcje zapisane są w formie zdań zakończonych kropką lub wykrzyknikiem. Większość instrukcji
zapisywanych jest w postaci podmiot-orzeczenie-dopełnienie. Podmiotem jest zmienna, której chcemy
przypisać wartość. Orzeczenie określa operację, którą chcemy wykonać. Poprzez dopełnienie
przekazujemy zmienne, na których chcemy wykonać daną operację.

Kod jest podzielony na funkcje. Deklaracja funkcji zacyna się od jej nazwy, któro podajemy poprzez
podanie pojedynczego słowa w osobym wierszu. Jeśli plik nie zawiera żadnej nazwy funkcji, cały kod
traktowany jest jako jedna funkcja. Ostatnia funkcja w pliku jest główną funkcją programu.
W obrębie funkcji kod możemy podzielić na akapity za pomocą pustego wiersza.

Charakterystyczną cechą języka opowiadanie jest to, że zmienne mazją swój rodzaj gramatyczny. Jest
od ustalany przy pierwszym przypisaniu wartości do zmiennej i wynika z rodzaju gramatycznego
czasownika użytego jako orzeczenie. Jest on niezmienny, zastosowanie błędnego rodzaju w dalszej
części kodu skutkuje błędem programu.

Podmiot zapisujemy w mianowniku, natomiast dopełnienie w bierniku, choć zapisanie dopełnienia w
mianowniku również jest dopuszczalne. Dla zmiennych rodzaju męskiego biernik jest domyślnie
tworzony przez dodanie końcówki *-a*, a dla zmiennych rodzaju żeńskiego zakończonych na *-a*
poprzez zamianę końcówki na *-ę*.

Jeśli zamiast podmiotu użyjemy słowa `następnie`, `potem` lub `ponadto`, podmiotem będzie ostatnio
użyta zmienna. Jeśli w charakterze dopełnienia użyjemy słowa `siebie`, dopełnieniem będzie ta sama
zmienna, która jest podmiotem.

Przykłady prawidłowych plików z kodem źródłowym znajdują się w folderze *przyklady*.

## Instrukcje

W tym rozdziale znajduje się dokumentacja dopuszczalnych instrukcji. Dla każdej z nich w pierwszej
linii podajemy ogólną składnię, a w drugiej działający przykład. W ogólnej składni ukośnikami
rozdzialamy kolejno formy dla rodzaju męskiego, żeńskiego i nijakiego.

### Przypisanie zmiennej liczbowej

> `<zmienna> miał/miała/miało <liczba> <dodatek>.`

> `Hieronim miał trzydzieści pięć lat.`

Liczby zapisujemy w postaci słownej, od zera do tysiąca. Dopuszczalne też są liczebniki zwyczajowe:
`tuzin`, `kopa` i `gros`. Zamiast czasownika `miał/miała/miało` możemy użyć równoważnie
`liczył/liczyła/liczyło`. Dodatkowe słowo po liczbie jest tylko ozdobnikiem, nie ma ono wpływy na
działanie programu.