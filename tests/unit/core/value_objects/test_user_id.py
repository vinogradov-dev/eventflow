"""Тесты для Value Object UserId."""

import pytest

from src.core.value_objects import UserId


class TestUserId:
    """Набор тестов для проверки UserId."""

    @pytest.mark.parametrize(
        "value",
        [
            "usr_12345",
            "x",
            "x" * 50,
            "user@example.com",
            "usr_000001",
        ],
    )
    def test_create_valid_user_id(self, value):
        """Создание валидного UserId."""
        user_id = UserId(value)
        assert user_id.value == value

    @pytest.mark.parametrize(
        "invalid_value",
        [
            "",  # Пустая строка
        ],
    )
    def test_create_user_id_empty_value_raises_error(self, invalid_value):
        """Попытка создать UserId с пустым значением."""
        with pytest.raises(ValueError, match="не может быть пустым"):
            UserId(invalid_value)

    @pytest.mark.parametrize(
        "invalid_value",
        [
            "x" * 51,  # 51 символ
            "x" * 100,  # 100 символов
        ],
    )
    def test_create_user_id_too_long_raises_error(self, invalid_value):
        """Попытка создать UserId длиннее 50 символов."""
        with pytest.raises(ValueError, match="не должно превышать 50"):
            UserId(invalid_value)

    def test_user_id_is_immutable(self):
        """Проверка неизменяемости UserId."""
        user_id = UserId("usr_123")
        with pytest.raises(AttributeError):
            user_id.value = "usr_456"  # noqa
