"""Тесты для EventEntity."""

from datetime import datetime
from decimal import Decimal

import pytest

from src.domain.entities import EventEntity
from src.domain.value_objects import EventType, Money, UserId


class TestEventEntity:
    """Набор тестов для проверки EventEntity."""

    @pytest.mark.parametrize(
        argnames=(
            "event_id",
            "event_type",
            "money",
        ),
        argvalues=(
            pytest.param(
                "ev_1",
                EventType.CLICK,
                None,
                id="CLICK without money",
            ),
            pytest.param(
                "ev_2",
                EventType.PURCHASE,
                Money(Decimal("100"), "RUB"),
                id="PURCHASE with money",
            ),
        ),
    )
    def test_create_valid_event(
        self,
        event_id: str,
        event_type: EventType,
        money: Money | None,
    ):
        """Создание валидного Event с разными типами событий.
        
        Проверяет, что Event создаётся корректно:
        - CLICK без money (money=None)
        - PURCHASE с money (Money объект)
        """
        event = EventEntity(
            id=event_id,
            user_id=UserId(value="user_1"),
            event_type=event_type,
            timestamp=datetime(2026, 1, 1, 0, 0),
            money=money,
        )
        assert event.id == event_id
        assert event.event_type == event_type
        assert event.money == money

    @pytest.mark.parametrize(
        argnames=("event_id", "event_type", "money"),
        argvalues=(
            pytest.param(
                "ev_1",
                EventType.PURCHASE,
                None,
                id="PURCHASE without money",
            ),
            pytest.param(
                "ev_2",
                EventType.CLICK,
                Money(Decimal("100"), "RUB"),
                id="CLICK with money",
            ),
            pytest.param(
                "ev_3",
                EventType.VIEW,
                Money(Decimal("50"), "RUB"),
                id="VIEW with money",
            ),
            pytest.param(
                "ev_4",
                EventType.REGISTRATION,
                Money(Decimal("50"), "RUB"),
                id="REGISTRATION with money",
            ),
        ),
    )
    def test_create_event_invalid_money_for_event_type_raises_error(
        self,
        event_id: str,
        event_type: EventType,
        money: Money | None,
    ):
        """Попытка создать Event с некорректным money для типа события.
        
        Проверяет, что возникает ValueError:
        - PURCHASE без money (обязательно для PURCHASE)
        - CLICK с money (должно быть None)
        - VIEW с money (должно быть None)
        - REGISTRATION с money (должно быть None)
        """
        with pytest.raises(ValueError, match="money"):
            EventEntity(
                id=event_id,
                user_id=UserId(value="user_1"),
                event_type=event_type,
                timestamp=datetime(2026, 1, 1, 0, 0),
                money=money,
            )

    def test_create_event_empty_id_raises_error(self):
        """Попытка создать Event с пустым id."""
        with pytest.raises(ValueError, match="id"):
            EventEntity(
                id="",
                user_id=UserId("user_1"),
                event_type=EventType.CLICK,
                timestamp=datetime(2026, 1, 1),
            )
