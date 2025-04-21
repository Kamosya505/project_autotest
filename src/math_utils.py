from src.logger import logger

def calculate(a: float, b: float, operation: str) -> float:
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                raise ValueError("Деление на ноль недопустимо")
            return a / b
        else:
            raise ValueError(f"Недопустимая операция: {operation}")
    except Exception as e:
        logger.error(f"Ошибка в calculate: {e}")
        raise
