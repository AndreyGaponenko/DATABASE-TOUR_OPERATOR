from russian_names import RussianNames
from faker import Faker
import psycopg2
import datetime
import random
import functions as f
faker = Faker('ru_RU')
all_kind=[]

con = psycopg2.connect(
    dbname='postgres',
    user='admin',
    password='root',
    host='127.0.0.1',
    port='5432'
)
all_people=[]
cur = con.cursor()
#print(get_FIO(),get_phone_number())
#a1=RussianNames().get_person()
#print(a1)
#print(a1.split()[2])
#print(get_foreign_passport(),get_birth_certificate())
i = 0
index = 0
only_one_each_relate=[]
while i < 200:
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
        #print(i,j,name,client['sex'])
        #print(client)
        cur.execute(
            f"""
            INSERT INTO Client(FIO,pers_document,birth_date,phone_number)
            values ('{name}','{pers_document}','{birth}','{n}')
            """
            )
        con.commit()
        if n[len(n)-1]=='NULL':
            all_kind.append([name,index, birth])
            continue
        else:
            for j in(all_kind):
                age_diff=int(str(abs(birth-j[2])).split()[0])/365
                #print(age_diff)
                if ((f.isnt_dif_surname(name.split()[0], j[0].split()[0])) and (age_diff >= 18) and ([j[1],f.determ_relat_degree(age_diff,client['sex'])] not in(only_one_each_relate))):
                    print(name.split()[0],j[0].split()[0])
                    only_one_each_relate.append([j[1],f.determ_relat_degree(age_diff,client['sex'])])
                    print(j[1],f.determ_relat_degree(age_diff,client['sex']),index)
                    cur.execute(
                        f"""
                        INSERT INTO Relativies(id_client_child,degree_of_relative,id_client)
                        values ('{j[1]}','{f.determ_relat_degree(age_diff,client['sex'])}','{index}')
                        """
                        )
                    con.commit()
    i += 1

con.close()

print('ok')