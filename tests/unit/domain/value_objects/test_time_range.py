"""Тесты для Value Object TimeRange."""

import pytest
from datetime import datetime

from src.domain.value_objects import TimeRange


class TestTimeRange:
    """Набор тестов для проверки TimeRange."""

    @pytest.mark.parametrize(
        "from_date,to_date",
        [
            (datetime(2026, 1, 1), datetime(2026, 1, 31)),
            (datetime(2026, 1, 1, 0, 0, 0), datetime(2026, 1, 1, 23, 59, 59)),
            (datetime(2026, 6, 15, 12, 30), datetime(2026, 12, 31, 23, 59, 59)),
            (datetime(2025, 1, 1), datetime(2027, 1, 1)),
        ],
    )
    def test_create_valid_time_range(self, from_date, to_date):
        """Создание валидного TimeRange."""
        time_range = TimeRange(from_date, to_date)
        assert time_range.from_ == from_date
        assert time_range.to == to_date

    @pytest.mark.parametrize(
        "from_date,to_date",
        [
            # to равно from
            (datetime(2026, 1, 1), datetime(2026, 1, 1)),
            (datetime(2026, 6, 15, 12, 0, 0), datetime(2026, 6, 15, 12, 0, 0)),
            # to раньше from
            (datetime(2026, 1, 31), datetime(2026, 1, 1)),
            (datetime(2026, 12, 31), datetime(2026, 1, 1)),
            (datetime(2026, 1, 1, 12, 0, 0), datetime(2026, 1, 1, 11, 59, 59)),
        ],
    )
    def test_create_time_range_invalid_range_raises_error(self, from_date, to_date):
        """Попытка создать TimeRange, где to <= from."""
        with pytest.raises(ValueError, match="to должно быть больше"):
            TimeRange(from_date, to_date)

    def test_time_range_is_immutable(self):
        """Проверка неизменяемости TimeRange."""
        time_range = TimeRange(datetime(2026, 1, 1), datetime(2026, 1, 31))
        with pytest.raises(AttributeError):
            time_range.from_ = datetime(2026, 2, 1)
