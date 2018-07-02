import pytest
from hypothesis import given
import hypothesis.strategies as strat


list1 = list('123456')
list2 = list('abcd')


def dictionaryFromKeys(k, v):
    try:
        res = dict.fromkeys(k, None)
        res.update(zip(k, v))
    except TypeError:
        res = 'TypeError'
    return res


result = dictionaryFromKeys(list1, list2)
print(result)


def test():
    k = ['1', '2', '3', '4']
    v = ['W', 'o', 'r', 'd']
    expected == {'1': 'W', '2': 'o', '3': 'r', '4': 'd'}

    assert dictionaryFromKeys(k, v) == expected


def test1():
    k = ['1', '2', '3', '4', '5']
    v = ['W', 'o', 'r', 'd']
    expected == {'1': 'W', '2': 'o', '3': 'r', '4': 'd', '5': 'None'}

    assert dictionaryFromKeys(k, v) == expected


@pytest.mark.parametrize('k, v', [
    (['1'], 'dearear'),
    ('2', ['friend'])
])
def test2(k, v):
    with pytest.raises(TypeError):
        dictionaryFromKeys(k, v)


@given(st.lists(st.text()))
def test3(extra_values):
    k = ['1', '2', '3', '4', '5']
    v = ['H', 'e', 'l', 'l', 'o']
    expected = {'1': 'H', '2': 'e', '3': 'l', '4': 'l', '5': 'o'}

    assert dictionaryFromKeys(k, v) == expected



