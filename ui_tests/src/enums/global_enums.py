from enum import Enum


class TimeoutEnum(Enum):
    """
    Класс, в котором содержится список необходимых тайм-аутов
    """

    ONE_TENTH_SEC: float = 0.1
    HALF_SEC: float = 0.5
    ONE_SEC: float = 1.0
    ONE_AND_A_HALF_SEC: float = 1.5
    TWO_SEC: float = 2.0
    THREE_SEC: float = 3.0
    FIVE_SEC: float = 5.0
    TEN_SEC: float = 10.0
    THIRTY_SEC: float = 30.0
    SIXTY_SEC: float = 60.0
