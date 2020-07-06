import unittest
from random import randint

lista = []
for i in range(20):
    number = randint(0,100)
    lista.append(number)


def max_fun(list):
    max_number = 0
    for number in lista:
        if number >= max_number:
            max_number = number
    return max_number


def min_fun(lista):
    min_number = 10000
    for number in lista:
        if number < min_number:
            min_number = number
    return min_number


class PythonStringTests(unittest.TestCase):
    def test_format_replaces_variables_in_string(self):
        result = "hola {0}, {1}".format("carlos", "que tal")
        self.assertEqual("hola carlos, que tal", result)

    def test_format_without_numbers(self):
        result = "hola {}, {}".format("carlos", "que tal")
        self.assertEqual("hola carlos, que tal", result)

    def test_max_min(self):
        self.assertEqual(max(lista), max_fun(lista))
        self.assertEqual(min(lista), min_fun(lista))


if __name__ == '__main__':
    unittest.main()
