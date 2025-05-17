from enum import Enum


class Rodzaj(Enum):
    MĘSKI = 'męski'
    ŻEŃSKI = 'żeński'
    NIJAKI = 'nijaki'


class Warunek(Enum):
    SPEŁNIONY = 'warunek spełniony'
    SPEŁNIONY_PĘTLA = 'warunek spełniony pętla'
    NIESPEŁNIONY = 'warunek niespełniony'