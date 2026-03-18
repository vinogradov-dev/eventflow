from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.event_type import EventType
from src.domain.value_objects.money import Money
from src.domain.value_objects.user_id import UserId


@dataclass(slots=True)
class EventEntity:
    """Сущность события.

    Entity для определения события.

    Attributes:
        id: не пустая строка
        user_id: Value Object UserId
        event_type: Value Object EventType тип события
        timestamp: Время создания события
        money: Value Object Money или None. По умолчанию None. Передаётся, если event_type = purchase
    """

    id: str
    user_id: UserId
    event_type: EventType
    timestamp: datetime
    money: Money | None = None

    def __post_init__(self) -> None:
        if len(self.id) < 1:
            raise ValueError("Значение id события не может быть пустым")
        if self.event_type == EventType.PURCHASE and not self.money:
            raise ValueError("Значение атрибута money не должно быть None")
        if self.event_type != EventType.PURCHASE and self.money:
            raise ValueError("Не нужно передавать значение атрибута money")
