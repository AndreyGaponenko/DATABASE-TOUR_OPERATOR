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
date=dt.datetime(2021,1,1)
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
    price_per_child=int(random.randint(45,65)/100*price_per_adult) 
    duration = random.randint(7,21) #6
    price_datas.append([i,price_per_adult,price_per_child,duration]) #5
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
    #print(f"({quantity_f_p},'{city}','{hotel}',{price_per_adult},{price_per_child},{duration},'{date_print}',{id_food},{id_country})")

faker1 = Faker('ru_RU')
all_kinder=[]
all_kinder_id=[]
i = 0
index = 0
only_one_each_relate=[]
while i < 220:
    index+=1
    client = faker.simple_profile()
    client['name'], pers_document, client['birthdate'], n, client['sex'] = f.get_all_info()
    SURNAME=client['name'].split()[0]
    a1=client['name'].split()
    if SURNAME[len(SURNAME)-1]=='а' or SURNAME[len(SURNAME)-1]=='я':
        client['sex']='F'
    else:
        client['sex']='M'
    a1[0]=f.get_norm_surname2(SURNAME,client['sex'])
    client['name']=' '.join(a1)
    #print(i,client['name'],client['sex'])
    
    k=random.randint(1, 9)
    for j in range(k):
        if j!=0:
            index+=1
            client['name'], pers_document, client['birthdate'], n, client['sex'] = f.get_all_info()
            #print(i,j,client['name'], pers_document, client['birthdate'], n, client['sex'])
            a1=client['name'].split()
            if a1[0][len(a1[0])-1]=='а' or a1[0][len(a1[0])-1]=='я':
                client['sex']='F'
            else:
                client['sex']='M'
            a1[0]=f.get_norm_surname2(SURNAME,client['sex'])
            client['name']=' '.join(a1)
        name=client['name']
        birth=client['birthdate']
        cur.execute(
            f"""
            INSERT INTO Client(FIO,pers_document,birth_date,phone_number)
            values ('{name}','{pers_document}','{birth}','{n}')
            """
            )
        con.commit()
        if n[len(n)-1]=='L':
            all_kinder.append([name,index,birth])
            all_kinder_id.append(index)
            continue
        else:
            for j in(all_kinder):
                age_diff=int(str(abs(birth-j[2])).split()[0])/365
                #print(age_diff)
                if ((f.isnt_dif_surname(name.split()[0], j[0].split()[0])) and (age_diff >= 18) and ([j[1],f.determ_relat_degree(age_diff,client['sex'])] not in(only_one_each_relate))):
                    #print(name.split()[0],j[0].split()[0])
                    only_one_each_relate.append([j[1],f.determ_relat_degree(age_diff,client['sex'])])
                    #print(j[1],f.determ_relat_degree(age_diff,client['sex']),index)
                    cur.execute(
                        f"""
                        INSERT INTO Relativies(id_client_child,degree_of_relative,id_client)
                        values ('{j[1]}','{f.determ_relat_degree(age_diff,client['sex'])}','{index}')
                        """
                        )
                    con.commit()
                    print(j[1],f.determ_relat_degree(age_diff,client['sex']),index)
    i += 1
count_sale_id=1
tour_id=1
date_sale_now=dt.datetime(2021,4,1)
date_sale_discount1=dt.datetime(2021,11,1)
date_sale_discount2=dt.datetime(2021,12,1)
sale_composition=[]
for y in range(2):
    for i in range(7-y,1000,5):   #5,900,5
        count_child=0
        discount_id=3
        id_employee=random.randint(1, 15)
        delta_t=dt.timedelta(days=random.randint(0, 3))
        date_sale_print=date_sale_now.strftime("%Y-%m-%d") #1
        #print(date_sale_print)
        sum_money=0 
        j=i
        while j in(all_kinder_id):
            j+=1
        #print('Composition',j,count_sale_id)
        sale_composition.append([j,count_sale_id])
        sum_money+=price_datas[tour_id-1][1]*price_datas[tour_id-1][3]
        ran=random.randint(1, 8)
        for k in range(j-5,j-5+ran):
            if k!=j:
                #print('Composition',k,count_sale_id)
                sale_composition.append([k,count_sale_id])
                if k in(all_kinder_id):
                    sum_money+=price_datas[tour_id-1][2]*price_datas[tour_id-1][3]
                    count_child+=1
                else:
                    sum_money+=price_datas[tour_id-1][1]*price_datas[tour_id-1][3]
        #print(count_child)
        if count_child>=3:
            sum_money=sum_money*0.85
            discount_id=1
        elif date_sale_discount1>date_sale_now>=date_sale_discount2:
            sum_money=sum_money*0.9
            discount_id=2
        tour_id+=1 #random.randint(1, 3)
        
        date_sale_now=date_sale_now+delta_t #1
        cur.execute(
            f"""
            INSERT INTO sale(date_sale,sum_money,id_tour,id_discount,id_client,id_employee)
            values ('{date_sale_print}',{sum_money},{tour_id},{discount_id},{j},{id_employee})
            """
            )
        con.commit()
        for t in range(len(sale_composition)):
            cur.execute(
                f"""
                INSERT INTO composition_sale(id_client,id_sale)
                values ({sale_composition[t][0]},{sale_composition[t][1]})
                """
                )
            con.commit()
        if ((random.randint(1,10)>7) and (y==0)):
            date_refund=date_sale_now
            delta_t1=dt.timedelta(days=random.randint(0, 2))
            date_refund+=delta_t1
            date_refund=date_refund.strftime("%Y-%m-%d")
            cur.execute(
                f"""
                INSERT INTO refund(id_sale,date_refund,sum_money,id_employee)
                values ({count_sale_id},'{date_refund}',{sum_money},{id_employee})
                """
            )
            con.commit()
        count_sale_id+=1
        sale_composition=[]
        #print(date_sale_print,sum_money,tour_id,discount_id,j,id_employee,discount_id)
    tour_id=tour_id%150
con.close()