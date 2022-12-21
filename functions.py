from russian_names import RussianNames
from faker import Faker
import datetime
import random
faker = Faker('ru_RU')

def get_phone_number():
    n='+7-9'
    for j in range(12):
        if j in[2,6,9]:
            n+='-'
        else: n+=str(random.randint(0,9))
    return n
def get_FIO():
    a1=RussianNames().get_person()
    a1=a1.split()
    a1.insert(0,a1[2])
    del a1[3]
    return str(' '.join(a1))
def get_foreign_passport():
    n=''
    for i in range(0,2):
        n+=str(random.randint(0,9))
    n+=' '
    for j in range(0,6):
        n+=str(random.randint(0,9))
    return n
def get_birth_certificate():
    n='I'*random.randint(1, 3)
    n+='-'
    alf='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    n+=alf[random.randint(0, len(alf)-1)]
    n+=alf[random.randint(0, len(alf)-1)]
    n+=' '
    for i in range(6):
        n+=str(random.randint(0,9))
    return n
def get_all_info():
    client = faker.simple_profile()
    while client['birthdate'] < datetime.date(1940, 1, 1):
        client = faker.simple_profile()
    age=str(datetime.date.today()-client['birthdate'])
    if (float(age.split()[0])/365 < 18):
        n='-'
        pers_document=get_birth_certificate()
    else:
        n=get_phone_number()
        pers_document=get_foreign_passport()
    a1=get_FIO()
    client['name']=a1
    return a1,pers_document,client['birthdate'],n, client['sex']
def determ_relat_degree(age_diff,sex):
    if ((18 <= age_diff < 40) and (sex=='F')):
        return 'мать'
    elif ((40 <= age_diff < 100) and (sex=='F')):
        return 'баба'
    elif ((18 <= age_diff < 40) and (sex=='M')):
        return 'отец'
    elif ((40 <= age_diff < 100) and (sex=='M')):
        return 'дед'
def isnt_dif_surname(surname1,surname2):
    if len(surname1) > len(surname2):
        if (surname1[:len(surname2)-2]==surname2[:-2]):
            return True
        else: return False
    else: 
        if (surname1[:-2]==surname2[:len(surname1)-2]):
            return True
        else: return False
def get_norm_surname(surname):
    if (surname[len(surname)-1]=='а'):
        return surname[:-1]+'ко'
    elif (surname[len(surname)-1]=='я'):
        return surname[:-3]+'ко'
    elif (surname[len(surname)-1]=='й'):
        return surname[:-3]+'ко'
    else:
        return surname+'ко'
def get_norm_surname2(surname,sex):
    if (sex=='M'):
        if (surname[len(surname)-1]=='а'):
            return surname[:-1]
        elif (surname[len(surname)-1]=='я'):
            return surname[:-2]+'ий'
        elif (surname[len(surname)-1]=='й'):
            return surname
        else:
            return surname
    if (sex=='F'):
        if (surname[len(surname)-1]=='й'):
            return surname[:-2]+'ая'
        elif (surname[len(surname)-1]=='я'):
            return surname
        elif (surname[len(surname)-1]!='а'):
            return surname+'а'
        else:
            return surname