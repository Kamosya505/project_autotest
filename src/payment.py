from src.notifier import notify_user
from src.logger import logger

def process_payment(amount: float) -> bool:
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    return True

def handle_transaction(amount: float):
    try:
        if process_payment(amount):
            notify_user(f"Платёж на сумму {amount} успешно обработан.")
    except Exception as e:
        logger.error(f"Ошибка в handle_transaction: {e}")
        raise
