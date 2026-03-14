"""Тесты для Value Object EventType."""

import pytest

from src.core.value_objects import EventType


class TestEventType:
    """Набор тестов для проверки EventType."""

    @pytest.mark.parametrize(
        "event_type,expected_value",
        [
            (EventType.PURCHASE, "purchase"),
            (EventType.CLICK, "click"),
            (EventType.VIEW, "view"),
            (EventType.REGISTRATION, "registration"),
        ],
    )
    def test_event_type_values(self, event_type, expected_value):
        """Проверка значений EventType."""
        assert event_type.value == expected_value
        assert str(event_type) == expected_value

    @pytest.mark.parametrize(
        "input_value,expected_type",
        [
            ("purchase", EventType.PURCHASE),
            ("click", EventType.CLICK),
            ("view", EventType.VIEW),
            ("registration", EventType.REGISTRATION),
        ],
    )
    def test_event_type_from_string(self, input_value, expected_type):
        """Создание EventType из строки."""
        event_type = EventType(input_value)
        assert event_type == expected_type

    def test_event_type_invalid_value_raises_error(self):
        """Попытка создать EventType с неверным значением."""
        with pytest.raises(ValueError):
            EventType("invalid_type")

    @pytest.mark.parametrize(
        "invalid_value",
        [
            "PURCHASE",  # Верхний регистр
            "Purchase",  # Смешанный
            "purchases",  # Опечатка (множественное число)
            "clicks",  # Опечатка (множественное число)
            "",  # Пустая строка
            "buy",  # Несуществующее значение
        ],
    )
    def test_event_type_invalid_values_raise_error(self, invalid_value):
        """Попытка создать EventType с неверными значениями."""
        with pytest.raises(ValueError):
            EventType(invalid_value)

    def test_event_type_is_immutable(self):
        """Проверка неизменяемости EventType (Enum неизменяем по природе)."""
        # Enum по своей природе неизменяем, но проверим, что нельзя изменить значение
        with pytest.raises(AttributeError):
            EventType.PURCHASE.value = "changed"
