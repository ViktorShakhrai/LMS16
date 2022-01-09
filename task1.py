# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check
# if the passed email parameter is a valid email string.

# Створіть метод класу з ім’ям `validate`, який слід викликати з методу `__init__` для перевірки параметра email,
# переданого до конструктора. Логіка всередині методу `validate` може полягати в тому,
# щоб перевірити, чи переданий параметр електронної пошти є дійсним рядком електронної пошти.

import validate_email


class Email:
    def __init__(self, email):
        if Email.validate(email):
            self.email = email

        else:
            print("Uncorrect Email!")

    @classmethod
    def validate(cls, email):
        return validate_email.validate_email(email)

em = Email("vikto1759@gmail.com")