# Проект: Арифметический калькулятор с автотестами

## Структура

- src/math_utils.py — функция calculate
- tests/test_math_utils.py — юнит-тесты
- error.log — лог ошибок (автоматически создаётся)
- requirements.txt — зависимости

## Запуск

```
pip install -r requirements.txt
pytest --html=report.html
coverage run -m unittest
coverage report -m
```
