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

    def wagons_number_generation(self, number=1):
        """
        Метод, возвращающий строку с номерами вагонов. Количество вагонов указывается в параметре number
        """

        wagons_string = [self.fake.numerify(text='########') for _ in range(number)]
        return ' '.join(wagons_string)

    @staticmethod
    def string_with_special_characters_generation():
        """
        Метод, возвращающий строку со специальными символами
        """

        letters = 'sdfaffafa'
        string_with_special_characters = '#$%^&!@#$$%%^'
        result = [letters[i] if i % 2 == 0 else string_with_special_characters[i] for i in range(len(letters))]
        return ''.join(result)

    def get_digit_string_with_special_characters(self):
        """
        Метод, возвращающий строку, состоящую из цифр, со специальным символом в середине строки
        """

        string_with_special_characters = '#$%^&!#$$%%^'
        string = (str(self.wagons_number_generation()) +
                  string_with_special_characters[random.randint(0, len(string_with_special_characters))] +
                  str(self.wagons_number_generation()))
        return string

    def company_generation(self):
        """
        Метод, возвращающий произвольное название компании
        """

        return self.fake.unique + ' Autotest'

    def get_random_string(self, length=5):
        """
        Метод, возвращающий рандомную строку. Длина строки передаётся в параметре length
        """

        string = [self.fake.random_lowercase_letter() for _ in range(length)]
        return ''.join(string) + ' Autotest'
