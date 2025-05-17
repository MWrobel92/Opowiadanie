import pyparsing as pp

bz = pp.Word(' \n')

def weź_cyfrę(tokeny):
    if tokeny[0] == 'jeden':
        return 1
    elif tokeny[0] == 'dwa':
        return 2
    elif tokeny[0] == 'trzy':
        return 3
    elif tokeny[0] == 'cztery':
        return 4
    elif tokeny[0] == 'pięć':
        return 5
    elif tokeny[0] == 'sześć':
        return 6
    elif tokeny[0] == 'siedem':
        return 7
    elif tokeny[0] == 'osiem':
        return 8
    elif tokeny[0] == 'dziewięć':
        return 9

cyfra = pp.CaselessLiteral('jeden') | pp.CaselessLiteral('dwa') | \
    pp.CaselessLiteral('trzy') | pp.CaselessLiteral('cztery') | \
    pp.CaselessLiteral('pięć') | pp.CaselessLiteral('sześć') | \
    pp.CaselessLiteral('siedem') | pp.CaselessLiteral('osiem') | \
    pp.CaselessLiteral('dziewięć')

cyfra.set_parse_action(weź_cyfrę)

def weź_naście(tokeny):
    if tokeny[0] == 'dziesięć':
        return 10
    if tokeny[0] == 'jedenaście':
        return 11
    elif tokeny[0] == 'dwanaście':
        return 12
    elif tokeny[0] == 'trzynaście':
        return 13
    elif tokeny[0] == 'czternaście':
        return 14
    elif tokeny[0] == 'piętnaście':
        return 15
    elif tokeny[0] == 'szesnaście':
        return 16
    elif tokeny[0] == 'siedemnaście':
        return 17
    elif tokeny[0] == 'osiemnaście':
        return 18
    elif tokeny[0] == 'dziewiętnaście':
        return 19

naście = pp.CaselessLiteral('dziesięć') | \
    pp.CaselessLiteral('jedenaście') | pp.CaselessLiteral('dwanaście') | \
    pp.CaselessLiteral('trzynaście') | pp.CaselessLiteral('czternaście') | \
    pp.CaselessLiteral('piętnaście') | pp.CaselessLiteral('szesnaście') | \
    pp.CaselessLiteral('siedemnaście') | pp.CaselessLiteral('osiemnaście') | \
    pp.CaselessLiteral('dziewiętnaście')

naście.set_parse_action(weź_naście)

def weź_dzieścia(tokeny):
    if tokeny[0] == 'dwadzieścia':
        return 20
    elif tokeny[0] == 'trzydzieści':
        return 30
    elif tokeny[0] == 'czterdzieści':
        return 40
    elif tokeny[0] == 'pięćdziesiąt':
        return 50
    elif tokeny[0] == 'sześćdziesiąt':
        return 60
    elif tokeny[0] == 'siedemdziesiąt':
        return 70
    elif tokeny[0] == 'osiemdziesiąt':
        return 80
    elif tokeny[0] == 'dziewięćdziesiąt':
        return 90

dzieścia = pp.CaselessLiteral('dwadzieścia') | \
    pp.CaselessLiteral('trzydzieści') | pp.CaselessLiteral('czterdzieści') | \
    pp.CaselessLiteral('pięćdziesiąt') | pp.CaselessLiteral('sześćdziesiąt') | \
    pp.CaselessLiteral('siedemdziesiąt') | pp.CaselessLiteral('osiemdziesiąt') | \
    pp.CaselessLiteral('dziewięćdziesiąt')

dzieścia.set_parse_action(weź_dzieścia)

def weź_setki(tokeny):
    if tokeny[0] == 'sto':
        return 100
    elif tokeny[0] == 'dwieście':
        return 200
    elif tokeny[0] == 'trzysta':
        return 300
    elif tokeny[0] == 'czterysta':
        return 400
    elif tokeny[0] == 'pięćset':
        return 500
    elif tokeny[0] == 'sześćset':
        return 600
    elif tokeny[0] == 'siedemset':
        return 700
    elif tokeny[0] == 'osiemset':
        return 800
    elif tokeny[0] == 'dziewięćset':
        return 900

setki = pp.CaselessLiteral('sto') | pp.CaselessLiteral('dwieście') | \
    pp.CaselessLiteral('trzysta') | pp.CaselessLiteral('czterysta') | \
    pp.CaselessLiteral('pięćset') | pp.CaselessLiteral('sześćset') | \
    pp.CaselessLiteral('siedemset') | pp.CaselessLiteral('osiemset') | \
    pp.CaselessLiteral('dziewięćset')

setki.set_parse_action(weź_setki)

dokładnie_dwucyfrowa = dzieścia + bz + cyfra
dokładnie_dwucyfrowa.leave_whitespace()
dokładnie_dwucyfrowa.set_parse_action(lambda t: t[0] + t[2])
dwucyfrowa = dokładnie_dwucyfrowa | dzieścia | naście | cyfra

dokładnie_trzycyfrowa = setki + bz + dwucyfrowa
dokładnie_trzycyfrowa.leave_whitespace()
dokładnie_trzycyfrowa.set_parse_action(lambda t: t[0] + t[2])

zero = pp.CaselessLiteral('zero')
zero.set_parse_action(lambda _: 0)
tuzin = pp.CaselessLiteral('tuzin')
tuzin.set_parse_action(lambda _: 12)
kopa = pp.CaselessLiteral('kopa')
kopa.set_parse_action(lambda _: 60)
gros = pp.CaselessLiteral('gros')
gros.set_parse_action(lambda _: 144)
tysiąc = pp.CaselessLiteral('tysiąc')
tysiąc.set_parse_action(lambda _: 1000)

liczba = dokładnie_trzycyfrowa | setki | dwucyfrowa | \
    tysiąc | gros | kopa | tuzin | zero
