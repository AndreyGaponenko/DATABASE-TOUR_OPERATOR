from faker import Faker
import psycopg2
import random
import datetime
import functions as f
faker = Faker('ru_RU')

con = psycopg2.connect(
    dbname='postgres',
    user='admin',
    password='root',
    host='127.0.0.1',
    port='5432'
)

cur = con.cursor()

i = 0
while i < 15:
    employee = faker.simple_profile()
    while employee['birthdate'] > datetime.date(2004, 1, 1):
        client = faker.simple_profile()
    employee['name']=f.get_FIO()
    n=f.get_phone_number()
    i += 1
    cur.execute(
        f"""
        insert into employee(fio, phone_number)
        values ('{employee['name']}', '{n}')
        """
    )
    con.commit()
con.close()

