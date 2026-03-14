from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    """Идентификатор пользователя в системе EventFlow.

    Value Object для безопасной передачи ID пользователя.
    Гарантирует, что ID — непустая строка длиной 1-50 символов.

    Example:
        >>> user_id = UserId("usr_12345")
        >>> user_id.value
        'usr_12345'

        >>> UserId("")  # ValueError
        >>> UserId("x" * 51)  # ValueError
    """
    value: str

    def __post_init__(self) -> None:
        if self.value is None or len(self.value) < 1:
            raise ValueError("Значение id пользователя не может быть пустым")
        elif len(self.value) > 50:
            raise ValueError("Значение id пользователя не должно превышать 50 символов")
