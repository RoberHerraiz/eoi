import unittest
from random import randint

# TDD - Test-driven development

# Paso 1: Definir una buena lista de requisitos - Piensa primero.

# None -> 0

# "" -> 0

# "8" -> 8

# "1, a" -> 1

# "1, 2, 3" -> 6

# "2, 10" -> 12

# Paso 2: escribir el test primero

# Paso 3: ejecutar todos los test y ver que el último falla

# Paso 4: escribir el código mínimo/más simple para que el test pase

# Paso 5: ejecutar todos los test y ver si todos siguen pasando

# Paso 6: refactoring

# Paso 7: repetir


def sum_numbers_in(expression):
    if expression is None or expression == "":
        return 0
    if "," in expression:
        tokens = expression.split(',')
        result = sum(tokens)
        return result
    return int(expression)


class PythonStringTests(unittest.TestCase):
    def test_none_and_empty_compute_as_zero(self):
        self.assertEqual(sum_numbers_in(""), 0)
        self.assertEqual(sum_numbers_in(None), 0)
    
    def test_numbers_in_expresion_are_converted_ti_integers(self):
        self.assertEqual(sum_numbers_in("8"), 8)
        self.assertEqual(sum_numbers_in("10"), 10)
    
    def test_numbers_in_expression_are_separated_by_commas(self):
        self.assertEqual(sum_numbers_in("1,4,1"), 6)

if __name__ == '__main__':
    unittest.main()

