import unittest
from src.math_utils import calculate

class TestCalculate(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 2, "-"), 3)

    def test_multiplication(self):
        self.assertEqual(calculate(4, 3, "*"), 12)

    def test_division(self):
        self.assertAlmostEqual(calculate(10, 2, "/"), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10, 0, "/")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "^")

    def test_logging_on_divide_by_zero(self):
        try:
            calculate(10, 0, "/")
        except ValueError:
            pass
        with open("error.log", "r", encoding="utf-8") as f:
            self.assertIn("Деление на ноль", f.read())

    def test_logging_on_invalid_operation(self):
        try:
            calculate(1, 2, "^")
        except ValueError:
            pass
        with open("error.log", "r", encoding="utf-8") as f:
            self.assertIn("Недопустимая операция", f.read())

if __name__ == "__main__":
    unittest.main()
