from funcoes.processo_seletivo import *
import os
from pathlib import Path

p = Path(os.getcwd())

path_data = str(p) + "\\data\\workload.csv"

# Testes para a função frequency_sort
def test_frequency_sort1():
    assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 2, 2, 6, 6]

def test_frequency_sort2():
    assert frequency_sort([4, 6, 1, 2, 2, 1, 1, 6, 1, 1, 6, 4, 4, 1]) == [1, 1, 1, 1, 1, 1, 4, 4, 4, 6, 6, 6, 2, 2]

def test_frequency_sort3():
    assert frequency_sort([17, 99, 42]) == [17, 42, 99]

def test_frequency_sort4():
    assert frequency_sort(['bob','bob','carl','alex','bob']) == ['bob','bob','bob','alex','carl']

# Testes para a função reverse_vowels
def test_reverse_vowels1():
    assert reverse_vowels('Bengt Hilgursson') == 'Bongt Hulgirssen'

def test_reverse_vowels2():
    assert reverse_vowels('Why do you laugh? I chose thedeath.') == 'Why da yee leogh? I chusa thudooth.'

def test_reverse_vowels3():
    assert reverse_vowels('These are the people you protect with your pain!') == 'Thisa uro thi peoplu yoe protect weth year peen!'

def test_reverse_vowels4():
    assert reverse_vowels('We had to sacrifice a couple of miners to free Bolivia.') == 'Wa hid ti socrefeco e ciople uf monars te frii Balovae.'

# Testes para a função collapse_intervals
def test_collapse_intervals1():
    collapse_intervals([1, 2, 4, 6, 7, 8, 9, 10, 12, 13]) == '1-2,4,6-10,12-13'

def test_collapse_intervals2():
    collapse_intervals([42]) == '42'

def test_collapse_intervals3():
    collapse_intervals([3, 5, 6, 7, 9, 11, 12, 13]) == '3,5-7,9,11-13'

def test_collapse_intervals4():
    collapse_intervals([]) == ''

def test_collapse_intervals5():
    collapse_intervals(range(1, 1000001)) == '1-1000000'

# Testes para a função calc_employee_dist
def test_calc_employee_dist():
    calc_employee_dist(path_data) == [
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,
        2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,3,3,3,3,3,2,2,2,
        2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,2,2,2,
        2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
        2,2,2,2,2,2,2,1,1,1
    ]