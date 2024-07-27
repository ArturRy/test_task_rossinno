from enum import Enum


class PyEnum(Enum):
    """
    Класс, расширяющий встроенный класс Enum
    """

    @classmethod
    def list(cls):
        """
        Метод, с помощью которого можно вернуть все перечисления любого класса-наследника от Enum в виде списка
        :return: список всех перечислений класса-наследника от Enum
        """

        return list(map(lambda x: x.value, cls))
