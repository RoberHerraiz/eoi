import unittest


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b

def check_equality(a, b):
    if a != b:
        raise Exception (str(a) + ' is not equal to ' + str(b))
    print('Check equality')

def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ArithmeticError("Divisor can't be zero")
    return a / b

def expect_raises(error_type, fun, arg1, arg2):
    try:
        fun(arg1, arg2)
        raise AssertionError(f"Excepted exception but not thrown{str(error_type)}")
    except error_type as e:
        pass

class Test(unittest.TestCase):
    def test_suma(self):
        check_equality(suma(2, 2), 4)

    def test_resta(self):
        resultado = resta(2,2)
        self.assertEqual(resultado, 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 2), 4)

    def test_division(self):
        with self.assertRaises(ArithmeticError):
            division(2, 0)

class PythonTestStrings(unittest.TestCase):
    
    def text_format_replaces_variables_in_string(self):
        result = "hola {0}, {1}".format("carlos", "que tal")
        self.assertEqual("hola carlos, quasdasde tal", result)


if __name__ == '__main__':
    unittest.main()