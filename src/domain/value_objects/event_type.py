from enum import StrEnum


class EventType(StrEnum):
    """Тип события в системе EventFlow.
    
    Определяет 4 допустимых типа событий для агрегации статистики.
    
    Members:
        PURCHASE: Покупка (транзакция с деньгами)
        CLICK: Клик (без денежного значения)
        VIEW: Просмотр (без денежного значения)
        REGISTRATION: Регистрация пользователя
    """
    PURCHASE = "purchase"
    CLICK = "click"
    VIEW = "view"
    REGISTRATION = "registration"
