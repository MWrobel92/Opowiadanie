**Opowiadanie** to język programowania umożliwiający pisanie kodu źródłowego piękną polszczyzną.

Niniejsze repozytorium zawiera kod źródłowy interpretera języka *Opowiadanie* napisany w języku
*Python*.

# Instrukcja obsługi

Aby uruchomić interpreter trzeba mieć zainstalowanego Pythona oraz pakiet
[pyparsing](https://pypi.org/project/pyparsing/). Kod był testowany w środowisku z językiem
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
zapisywanych jest w szyku podmiot-orzeczenie-dopełnienie. Podmiotem jest zmienna, której chcemy
przypisać wartość. Orzeczenie określa operację, którą chcemy wykonać. Poprzez dopełnienie
przekazujemy zmienne, na których chcemy wykonać daną operację.

Kod jest podzielony na funkcje. Deklaracja funkcji zaczyna się od jej nazwy, którą podajemy poprzez
wpisanie pojedynczego słowa w osobnym wierszu. Jeśli plik nie zawiera żadnej nazwy funkcji, cały
kod traktowany jest jako jedna funkcja. Ostatnia funkcja w pliku jest główną funkcją programu.
W obrębie funkcji kod możemy podzielić na akapity za pomocą pustego wiersza.

Charakterystyczną cechą języka opowiadanie jest to, że zmienne mają swój rodzaj gramatyczny. Jest
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

Przykłady prawidłowych plików z kodem źródłowym znajdują się w folderze *przyklady*. Plik
*witaj.opo* to typowy *Hello world*, tylko po polsku.

## Instrukcje

W tym rozdziale znajduje się dokumentacja dopuszczalnych instrukcji. Dla każdej z nich w pierwszej
linii podajemy ogólną składnię, a w drugiej działający przykład. W ogólnej składni ukośnikami
rozdzielamy kolejno formy dla rodzaju męskiego, żeńskiego i nijakiego.

### Przypisanie zmiennej liczbowej

> `<zmienna> miał/miała/miało <liczba> <dodatek>.`

> `Hieronim miał trzydzieści pięć lat.`

Liczby zapisujemy w postaci słownej, od zera do tysiąca. Dopuszczalne też są liczebniki zwyczajowe:
`tuzin`, `kopa` i `gros`. Zamiast czasownika `miał/miała/miało` możemy użyć równoważnie
`liczył/liczyła/liczyło`. Dodatkowe słowo po liczbie jest tylko ozdobnikiem, nie ma ono wpływu na
działanie programu.

### Przypisanie napisu

> `<zmienna> powiedział/powiedziała/powiedziało: <napis>.`

> `Adam powiedział: nie mam tu czego szukać.`

Jeśli zamiast czasownika `powiedział/powiedziała/powiedziało` użyjemy
`krzyknął/krzyknęła/krzyknęło`, do napisu zostanie dodany wykrzyknik. Istnieje też możliwość
przypisania pustego napisu za pomocą czasownika `milczał/milczała/milczało`, wtedy bez podawania
napisu.

### Przypisanie kolekcji

Kolekcję dwuelementową tworzymy podając nazwy dwóch zmiennych, których wartości mają trafić do
nowej kolekcji. Kolekcja zawierająca dwa elementy z końca zdania zostanie przypisana do zmiennej z
początku zdania.

> `<zmienna> zgrupował/zgrupowała/zgrupowało <zmienna> i <zmienna>.`

> `Zespół zgrupował ołówek i klawisz.`

Ponadto każdą zmienną możemy przekształcić w kolekcję jednoelementową zawierającą tę jedną wartość.

> `<zmienna> lubił/lubiła/lubiło samotność.`

> `Pudełko lubiło samotność.`

### Pobranie elementu kolekcji

> `<zmienna> wyjął/wyjęła/wyjęło <zmienna> i <zmienna>.`

> `Piotr wyjął zapłatę i Aleksandra.`

Do pierwszej zmiennej zapisujemy zwrócony element, druga zmienna jest kolekcją, a trzecia indeksem
elementu.

### Skopiowanie zmiennej

> `<zmienna> naśladował/naśladowała/naśladowało <zmienna>.`

> `Siłaczka naśladowała ołówek.`

### Wypisywanie zmiennej

> `<zmienna> wyjawił/wyjawiła/wyjawiło swój sekret.`

> `Aleksander wyjawił swój sekret.`

### Przypisanie biernika

Jeśli domyślna forma ostatnio użytej zmiennej nie jest satysfakcjonująca, można ją zmienić.

> `To wyróżniało <biernik>.`

> `To wyróżniało Aleksandra.`

### Wykonywanie działań

Podstawowe działania (dodawanie, odejmowanie itd.) wykonujemy podając na początku zdania nazwę
zmiennej, do której chcemy zapisać wynik, a na końcu zdania nazwy dwóch zmiennych będących
argumentami.

> `<zmienna> dodał/dodała/dodało <zmienna> i <zmienna>.`

> `Koszyk dodał zespół i Sylwię.`

Operacje są zdefiniowane tak samo, jak w języku *Python*. Przykładowo, wynikiem dodawania dwóch
liczb jest ich suma, a wynikiem dodawania napisów jest napis będący ich połączeniem. Inne działania
wykonujemy za pomocą następujących czasowników:

- `odjął/odjęła/odjęło`: odejmowanie,
- `pomnożył/pomnożyła/pomnożyło`: mnożenie,
- `podzielił/podzieliła/podzieliło`: dzielenie,
- `rozdzielił/rozdzieliła/rodzieliło`: dzielenie modulo,
- `spotęgował/spotęgowała/spotęgowało`: podniesienie do potęgi.

### Inkrementacja

> `<zmienna> zwiększył/zwiększyła/zwiększyło.`

> `Siłaczka zwiększyła się.`

Jeśli zamiast czasownika `zwiększył/zwiększyła/zwiększyło` użyjemy
`zmniejszył/zmniejszyła/zmniejszyło`, wykonamy dekrementację, tzn. zmiejszymy wartość zmienną o 1
zamiast ją zwiększać.

### Pobranie długości

> `<zmienna> zmierzył/zmierzyła/zmierzyło <zmienna>.`

> `Sylwia zmierzyła ołówek.`

Jeśli zmienną podaną na końcu zdania jest kolekcja lub napis, pobrana zostanie jego długość. Jeśli
zaś jest to liczba, pobrana bedzie jej wartość bezwzględna.

### Rzutowanie na wartośc liczbową

> `<zmienna> odczytał/odczytała/odczytało <zmienna>.`

> `Piotr odczytał Aleksandra.`

Przetwarza napis zawierający same cyfry na liczbę.

### Odwrócenie kolejności

> `<zmienna> zawrócił/zawróciła/zawróciło <zmienna>.`

> `Adam zawrócił.`

Jeśli zmienną podaną na końcu zdania jest kolekcja lub napis, zostanie utworzony nowy napis (lub
nowa kolekcja) o odwróconej kolejności. Jeśli zaś jest to liczba, pobrana będzie jej liczba
przeciwna.

### Przywołanie zmiennej

Ta instrukcja nie wykonuje żadnego działąnia poza ustawieniem danej zmiennej jako ostatnio
używanej. Przydatne w przypadku funkcji lub gdy chcemy użyć słowa `następnie`.

> `<zmienna> wyszedł/wyszła/wyszło na środek.`

> `Wynik wyszedł na środek.`

## Pętle i instrukcje warunkowe

Instrukcja warunkowa:

> `<zmienna> sprawdził/sprawdziła/sprawdziło się.`

> `Hieronim sprawdził się.`

Warunek pętli (działa jak pętla *while* w języku *Python*):

> `<zmienna> przejął/przejęła/przejęło dowodzenie.`

> `Siłaczka przejęła dowodzenie.`

Warunek jest spełniony, jeśli zmienna zawiera liczbę o dodatniej wartości lub napis/kolekcję o
niezerowej długości. Ciałem pętli lub instrukcji warunkowej jest pozostała część akapitu. Koniec
akapitu możemy traktować jak koniec bloku kodu.

## Funkcje

Jak wspomnieliśmy we wstępie, deklaracja funkcji zacyna się od jej nazwy, którą podajemy poprzez
wpisanie pojedynczego słowa w osobym wierszu. W obrębie funkcji dostępna jest zmienna o nazwie
`zapłata`, która zawiera argument przekazany do funkcji. Jeśli potrzebujemy więcej niż jednego
argumentu, musimy spakować je do kolekcji. Główna funkcja programu zawira w tej zmiennej kolekcję
z argumentami programu.

Funkcja zwraca wartość ostatnio użytej zmiennej. Funkcje wywołujemy za pomocą następującej
instrukcji, gdzie do zmiennej z początku zdania przypisujemy zwracaną wartość, a zmienną z końca
zdania przekazujemy jako argument.

> `<zmienna> objął/objęła/objęło <funkcja> i <zmienna>.`

> `Rezultat objął Przeznaczenie i Piotra.`