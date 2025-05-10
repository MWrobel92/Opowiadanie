from liczba import liczba
from zmienne import KuferekZmiennych, BłądNazwy, BłądRodzaju
from instrukcje import utwórz_główną_instrukcję

def test_liczby():
	przykłady = [
		('siedemdziesiąt osiem', 78),
		('dwieście siedemdziesiąt pięć', 275),
		('tuzin', 12),
		('siedemdziesiąt', 70),
		('SiedemNaście', 17),
		('PIĘĆ', 5),
		('trzysta czterdzieści dwa', 342),
		('zErO', 0),
	]
	for napis, wartość in przykłady:
		assert liczba.parse_string(napis)[0] == wartość

def test_instrukcji_podstawowych():
	zmienne = KuferekZmiennych()
	_, instrukcja = utwórz_główną_instrukcję(zmienne)

	instrukcja.parse_string('Hieronim liczył\ntrzydzieści pięć lat.')
	instrukcja.parse_string('Ania miała tuzin jajek.')
	instrukcja.parse_string('Syriusz powiedział: dwanaście lat na to czekałem w Azkabanie.')
	instrukcja.parse_string('Hieronim lubił samotność.')
	instrukcja.parse_string('Ania wyjawiła swój sekret.')
	instrukcja.parse_string('Syriusz wyjawił swój sekret.')

def test_błędu_nazwy():
	zmienne = KuferekZmiennych()
	_, instrukcja = utwórz_główną_instrukcję(zmienne)
	try:
		instrukcja.parse_string('UFO wyjawiło swój sekret.')
		assert False
	except BłądNazwy:
		assert True

def test_błędu_rodzaju():
	zmienne = KuferekZmiennych()
	_, instrukcja = utwórz_główną_instrukcję(zmienne)
	instrukcja.parse_string('Hieronim liczył\ntrzydzieści pięć lat.')
	try:
		instrukcja.parse_string('Hieronim miała siedemset dwanaście groszy.')
		assert False
	except BłądRodzaju:
		assert True