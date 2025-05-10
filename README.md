**Opowiadanie** to język programowania umożliwiający pisanie kodu źródłowego piękną polszczyzną.

Niniejsze repozytorium zawiera kod źródłowy interpretera języka *Opowiadanie* napisany w języku
*Python*.

# Specyfikacja języka

Instrukcje zapisane są w formie zdań zakończonych kropką lub wykrzyknikiem. Większość instrukcji
zapisywanych jest w postaci podmiot-orzeczenie-dopełnienie. Podmiotem jest zmienna, której chcemy
przypisać wartość. Orzeczenie określa operację, którą chcemy wykonać. Poprzez dopełnienie
przekazujemy zmienne, na których chcemy wykonać daną operację.

Charakterystyczną cechą języka opowiadanie jest to, że zmienne mazją swój rodzaj gramatyczny. Jest
od ustalany przy pierwszym przypisaniu wartości do zmiennej i wynika z rodzaju gramatycznego
czasownika użytego jako orzeczenie. Jest on niezmienny, zastosowanie błędnego rodzaju w dalszej
części kodu skutkuje błędem programu.

Podmiot zapisujemy w mianowniku, natomiast dopełnienie w bierniku.

Jeśli zamiast podmiotu użyjemy słowa *następnie*, *potem* lub *ponadto*, podmiotem będzie ostatnio
użyta zmienna. Jeśli w charakterze podmiotu użyjemy słowa *siebie*, dopełnieniem będzie ta sama
zmienna, która jest podmiotem.

Liczby zapisujemy w postaci słownej, od zera do tysiąca. Dopuszczalne też są liczebniki zwyczajowe:
*tuzin*, *kopa* i *gros*.