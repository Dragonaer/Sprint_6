import random
from faker import Faker
import secrets


from datetime import datetime, timedelta

def generate_random_date(start_year=2020, end_year=2030):
    year = random.randint(start_year, end_year)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_days = 366 if is_leap else 365
    day_of_year = random.randint(1, max_days)
    date = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)
    return date.strftime('%d.%m.%Y')


fake_ru = Faker('ru_RU')
def generate_registration_data():
    name = fake_ru.first_name()
    lastname = fake_ru.last_name()
    adress = 'Москва, ул. Ленина, д.3'
    number = secrets.randbelow(90_000_000_000) + 10_000_000_000
    return name, lastname, adress, number

