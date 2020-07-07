import unittest
from random import randint
import re

# TDD - Test-driven development

# Paso 1: Definir una buena lista de requisitos - Piensa primero.

# None -> 0
# "" -> 0
# "8" -> 8
# "1,a" -> 1
# "a" -> 0
# "1,2,3" -> 6
# "2,10" -> 12

# Carácter separador variable
# "//#/3#2" -> 5
# "//#/3,2" -> 0
# "//%/1%2%3" -> 6
# "//%%/1%%2%%3" -> 6
# "//%%/1%2%3" -> 0

# Paso 2: escribir el test primero

# Paso 3: ejecutar todos los test y ver que el último falla

# Paso 4: escribir el código mínimo/más simple para que el test pase

# Paso 5: ejecutar todos los test y ver si todos siguen pasando

# Paso 6: refactoring

# Paso 7: repetir


def sum_numbers_in(expression):

    if expression is None or expression == "":
        return 0

    separator, expression = get_separator(expression)

    if separator in expression:
        tokens = expression.split(separator)
        total = 0
        for token in tokens:
            total += parse_int(token)
        return total
    return parse_int(expression)


def parse_int(token):
    if re.match('^[0-9]+$', token):
        return int(token)
    return 0


def get_separator(expression):
    regex = '^//(.+)/'
    m = re.match(regex, expression)
    separator = ','
    if m:
        separator = m.groups()[0]
        n = 3 + len(separator)
        expression = expression[n:]
    return (separator, expression)


class TDD_Tests(unittest.TestCase):
    def test_none_and_empty_compute_as_zero(self):
        self.assertEqual(sum_numbers_in(""), 0)
        self.assertEqual(sum_numbers_in(None), 0)

    def test_numbers_in_expresion_are_converted_ti_integers(self):
        self.assertEqual(sum_numbers_in("8"), 8)
        self.assertEqual(sum_numbers_in("10"), 10)

    def test_numbers_in_expression_are_separated_by_commas(self):
        self.assertEqual(sum_numbers_in("1,4,1"), 6)

    def test_non_numeric_symbols_are_evaluated_as_zeros(self):
        self.assertEqual(sum_numbers_in("1,a"), 1)
        self.assertEqual(sum_numbers_in("a"), 0)
        self.assertEqual(sum_numbers_in("1a,2"), 2)

    def test_numbers_with_another_separator(self):
        self.assertEqual(sum_numbers_in("//#/3#2"), 5)
        self.assertEqual(sum_numbers_in("//%/1%2%3"), 6)
        self.assertEqual(sum_numbers_in("//%/1,2,3"), 0)
        self.assertEqual(sum_numbers_in("//%%/1%%2%%3"), 6)


if __name__ == '__main__':
    unittest.main()
