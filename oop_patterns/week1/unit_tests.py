import unittest

def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        # Что типы float и str (значения 'string', 1.5) вызывают исключение TypeError
        for i in ('string', 1.5):
            with self.subTest(x=i):
                self.assertRaises(TypeError, factorize, i)

    def test_negative(self):
        # Что для отрицательных чисел -1, -10 и -100 вызывается исключение ValueError.

        for i in (-1, -10, -100):
            with self.subTest(x=i):
                self.assertRaises(ValueError, factorize, i)

    def test_zero_and_one_cases(self):
        # Что для числа 0 возвращается кортеж (0,), а для числа 1 кортеж (1,)

            with self.subTest(x=0):
                self.assertEqual(factorize(0), (0,))

            with self.subTest(x=1):
                self.assertEqual(factorize(1), (1,))

    def test_simple_numbers(self):
        # Что для простых чисел 3, 13, 29 возвращается кортеж, содержащий одно данное число.
        for i in (-1, -10, -100):
            with self.subTest(x=i):
                self.assertIs(type(factorize(i)), int)


    def test_two_simple_multipliers(self):
        # Что для чисел 6, 26, 121 возвращаются соответственно кортежи (2, 3), (2, 13) и (11, 11).
        with self.subTest(x=6):
            self.assertEqual(factorize(6), (2, 3))

        with self.subTest(x=26):
            self.assertEqual(factorize(26), (2, 13))

        with self.subTest(x=121):
            self.assertEqual(factorize(121), (11, 11))

    def test_many_multipliers(self):
        # Что для чисел 1001 и 9699690 возвращаются соответственно кортежи (7, 11, 13) и (2, 3, 5, 7, 11, 13, 17, 19).
        with self.subTest(x=1001):
            self.assertEqual(factorize(1001), (7, 11, 13))

        with self.subTest(x=9699690):
            self.assertEqual(factorize(9699690), (2, 3, 5, 7, 11, 13, 17, 19))
