from russian_names import RussianNames
from faker import Faker
import psycopg2
import datetime as dt
import random
import functions as f
import randomtimestamp 
con = psycopg2.connect(
    dbname='postgres',
    user='admin',
    password='root',
    host='127.0.0.1',
    port='5432'
)
cur = con.cursor()
faker = Faker('en_US')
all_kind=[]
all_kind.append(['Коннект стран'])
all_kind.append(['Москва','Санкт-Петербург','Сочи'])#Россия
all_kind.append(['Тбилиси','Батуми'])#Грузия
all_kind.append(['Минск','Гомель'])#Беларуссия 
all_kind.append(['Сухум'])#Абхазия
all_kind.append(['Мадрид','Барселона','Валенсия','Севилья'])#Испания
all_kind.append(['Рим','Венеция','Милан','Неаполь','Турин','Болонья','Флоренция'])#Италия
all_kind.append(['Будва','Херцог-Нови',])#Черногория
all_kind.append(['Салоники','Афины','Гераклион'])#Греция
all_kind.append(['Берлин','Дрезден','Мюнхен','Дортмунд'])#Германия
all_kind.append(['Лондон','Манчестер','Ливерпуль'])#Великобритания
all_kind.append(['Стамбул','Анкара','Анталья'])#Турция
all_kind.append(['Каир','Александрия','Шарм-Эль-Шейх'])#Египет
all_kind.append(['Лиссабон','Порту'])#Португалия
all_kind.append(['Париж','Марсель','Бордо','Брест'])#Франция
print(all_kind)
created_dt = randomtimestamp.randomtimestamp(start_year=2022)
date=dt.datetime(2023,1,1)
#a=dt.timedelta(days=2)
#date=(date+a).strftime("%Y-%m-%d")
price_datas=[]
print(date)
#for i in range(1,len(all_kind)):
 #   print(i,all_kind[i])
for i in range(1,251):
    quantity_f_p=random.randint(5,50) #1
    id_country=random.randint(1,14) #9
    num_c=random.randint(0,len(all_kind[id_country])-1)
    city=all_kind[id_country][num_c] #2
    hotel=faker.unique.text(15)[:-1] #3
    price_per_adult=random.randint(3,9)*1000 #4
    price_per_child=int(random.randint(45,65)/100*price_per_adult) #5
    price_datas.append([i,price_per_adult,price_per_child])
    duration = random.randint(7,21) #6
    date_of_departure = date
    date_print = date.strftime("%Y-%m-%d")#7
    delta_t=dt.timedelta(days=random.randint(0, 3))
    date=(date+delta_t)        
    id_food = random.randint(1, 7) #8
    cur.execute(
        f"""
        INSERT INTO tour(quantity_free_places,city,hotel,price_per_adult,price_per_child,duration,date_of_departure,id_food,id_country)
        values ({quantity_f_p},'{city}','{hotel}',{price_per_adult},{price_per_child},{duration},'{date_print}',{id_food},{id_country})
        """
        )
    con.commit()
    print(f"({quantity_f_p},'{city}','{hotel}',{price_per_adult},{price_per_child},{duration},'{date_print}',{id_food},{id_country})")
con.close()