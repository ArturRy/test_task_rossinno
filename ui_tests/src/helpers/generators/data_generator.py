import random

import faker


class BaseDataGenerator:
    """
    Класс для генерации тестовых данных
    """

    fake = faker.Faker()

    def login_generation(self):
        """
        Метод для генерации логина пользователя
        """

        return self.fake.first_name() + ' Autotest'

    def password_generation(self):
        """
        Метод для генерации пароля пользователя
        """

        return self.fake.password() + ' Autotest'

    def get_random_string(self, length=5):
        """
        Метод, возвращающий рандомную строку. Длина строки передаётся в параметре length
        """

        string = [self.fake.random_lowercase_letter() for _ in range(length)]
        return ''.join(string) + ' Autotest'
