from faker import Faker
import random
from datetime import datetime, timedelta
import calendar

fake = Faker('ru_RU')

def generate_phone_number():
    number = ''.join(str(random.randint(0, 9)) for _ in range(10))  # 10 случайных цифр
    return f"+7{number}"

def generate_order_data(): # случайные данные для заполнения полей о заказчике
    return {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "address": fake.street_name(),
        "phone": generate_phone_number()
    }

def get_valid_rental_date(): # случайная дата, начиная с завтрашней
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    last_day = calendar.monthrange(tomorrow.year, tomorrow.month)[1]

    random_day = random.randint(tomorrow.day, last_day)
    return random_day

def generate_random_comment(length):
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return ''.join(random.choice(letters) for _ in range(length))
