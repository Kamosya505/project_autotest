# tests/test_integration.py

import unittest
from unittest.mock import patch
from src.payment import handle_transaction


class TestIntegration(unittest.TestCase):

    @patch("src.payment.notify_user")
    def test_valid_payment(self, mock_notify):
        handle_transaction(100)
        mock_notify.assert_called_once_with(
            "Платёж на сумму 100 успешно обработан."
        )

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            handle_transaction(0)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            handle_transaction(-10)

    def test_logging_on_error(self):
        try:
            handle_transaction(0)
        except ValueError:
            pass
        with open("error.log", "r", encoding="utf-8") as f:
            self.assertIn("Ошибка в handle_transaction", f.read())


if __name__ == "__main__":
    unittest.main()
