CREATE TABLE Client(  
    id_client SERIAL PRIMARY KEY,
    FIO varchar(100),
    pers_document VARCHAR(14),
    birth_date DATE,
    phone_number VARCHAR(16)
);
CREATE TABLE Relativies(
    id_client_child INT REFERENCES client(id_client),
    degree_of_relative VARCHAR(10),
    id_client INT
);
DROP TABLE client;
DROP TABLE client,relativies;
CREATE TABLE Employee(  
    id_employee SERIAL PRIMARY KEY,
    FIO varchar(100),
    phone_number VARCHAR(16)
);
DROP TABLE employee;
CREATE TABLE Food(  
    id_food SERIAL PRIMARY KEY,
    type_food SMALLINT,
    comments VARCHAR(200)
);
INSERT INTO food(type_food,comments)
VALUES
(1,'В цену включен только завтрак.'),
(1,'В цену включен только обед.'),
(1,'В цену включен только ужин.'),
(2,'В цену включен завтрак и обед.'),
(2,'В цену включен завтрак и ужин.'),
(2,'В цену включен обед и ужин.'),
(3,'В цену включен полноценное трёхразовое питание.');
CREATE TABLE Discount(  
    id_discount SERIAL PRIMARY KEY,
    name_discount VARCHAR(40),
    size REAL,
    condition VARCHAR(100)
);
INSERT INTO discount(name_discount,size,condition)
VALUES
('многодетная семья',0.15,'В туре должно ехать минимум 3 детей'),
('ноябрьская горячая распродажа',0.10,'Купите тур в период с 2022-11-01 по 2022-11-31'),
('наш постоянный путешественник',0.05,'Необходимо съездить нашим турагентством минимум 5 раз');

CREATE TABLE Country(
    id_country SERIAL PRIMARY KEY,
    name_country VARCHAR(20),
    currency VARCHAR(20),
    descriptions VARCHAR(200)
);
INSERT INTO country(name_country,currency,descriptions)
VALUES
('Россия','российский рубль','Самое большое государство по площади. Имеет богатую историю. В общем, можно долго перечислять достижения'),
('Грузия','лари','Прекрасная Кавказская православная страна, имеющая выход к Чёрному морю. В стране используются лари = 20 рублям за единицу'),
('Беларуссия','беларусский рубль','Постсоветское государство в прямом смысле слова: страна является "памятником" СССР, а также известна своей лбовью к картошке'),
('Абхазия','российский рубль','Частичнопризнанное государство на берегу чёрного моря, имеющая много общего с Грузией'),
('Испания','евро','Католическая курортная страна, омываемая мировым океаном практически со всех сторон. Помимо курортов, есть на что посмотреть в плане искусства'),
('Италия','евро','Страна содержит в себе невероятное сочетание пляжных курортов с невероятной культурой наследия Римской цивилизации'),
('Черногория','евро','Постюгославское государство, обладающее завораживающим сочетанием адриатического моря с горами, расположенными прямо на берегу'),
('Греция','евро','Православное государство, известное своими курортами на Средиземном море на многочисленных островах, в частности на острове Крит'),
('Германия','евро','Государство является лидером Евросоюза. Не является курортным, однако здесь есть на что посмотреть (немецкая культура)'),
('Великобритания','фунт стерлингов','Островное государство, обладающее историей, в которой они были порядка 250 лет властелинами мира. Одна поездка в Лондон чего лишь стоит'),
('Турция','доллар США','Является одним из самых распространённых мест для отдыха у россиян ввиду своей дишивизны'),
('Египет','доллар США','Госудаство имеет выход к "кристально чистому" Красному морю, которое по праву можно назвать самым крутым "аквариумом" в мире'),
('Португалия','евро','Государство находится "в уголке" Европы, омывается Атлантическим океаном на западе'),
('Франция','евро','Государство известно круасанами, а также своей столицей - Парижем, "городом любви"');
CREATE TABLE languages(
    id_language SERIAL PRIMARY KEY,
    name_language VARCHAR(20),
    descriptions VARCHAR(100)
);
INSERT INTO languages(name_language,descriptions)
VALUES
('Русский','Является государственным языком РФ и Беларуси. Используется во всех странах СНГ'),
('Английский','Занимает первое место в мире по числу говорящих. Является абсолютным международным языком'),
('Испанский','Является одним из самых распространнёх языков в мире. На нём говорит почти вся Латинская Америка'),
('Французский','Имеет прекрасное звучание. Используется во Франции, Канаде и многих странах Африки'),
('Грузинский','Является государственным языком Грузии'),
('Немецкий','Является государственным языком Германии, Австрии, Люксембурга, Швейцарии, Лихтенштейна'),
('Китайский','Является государственным языком Китая, имеет много носителей и практически нигде не используется'),
('Итальянский','Красивый язык, используемый только в Италии'),
('Арабский','Является госудаственным многих стран мира '),
('Португальский','Является государственным языком Португалии и Бразилии'),
('Турецкий','Является государственным языком Турции. Также используется в Азербайджане'),
('Греческий','Является государственным языком Греческий. Нигде больше не используется');
CREATE TABLE composition_languages(
    id_country INT REFERENCES country(id_country),
    id_language INT REFERENCES languages(id_language)
);
INSERT INTO composition_languages(id_country,id_language)
VALUES
(1,1),(1,2),
(2,1),(2,2),(2,5),
(3,1),(3,2),
(4,1),
(5,2),(5,3),
(6,2),(6,8),
(7,2),
(8,2),(8,12),
(9,2),(9,6),
(10,2),
(11,2),(11,11),
(12,2),(12,9),
(13,2),(13,10),
(14,2),(14,4);
CREATE TABLE Tour(  
    id_tour SERIAL PRIMARY KEY,
    quantity_free_places SMALLINT,
    city VARCHAR(20),
    hotel VARCHAR(20),
    price_per_adult INT,
    price_per_child INT,
    duration SMALLINT,
    date_of_departure DATE,
    id_food INT REFERENCES Food(id_food),
    id_discount INT REFERENCES Discount(id_discount),
    id_country INT REFERENCES Country(id_country)
);
CREATE TABLE Sale(
    id_sale SERIAL PRIMARY KEY,
    date_sale DATE,
    sum_money INT,
    id_tour INT REFERENCES Tour(id_tour),
    id_client INT REFERENCES Client(id_client),
    id_employee INT REFERENCES Employee(id_employee)
);
CREATE TABLE Refund(
    id_sale INT REFERENCES Sale(id_sale),
    date_refund DATE,
    cause VARCHAR(100),
    sum_money INT,
    id_employee INT REFERENCES Employee(id_employee)
);
CREATE TABLE Composition_sale(
    id_client INT REFERENCES Client(id_client),
    id_sale INT REFERENCES Sale(id_sale)
);

SELECT id_client,FIO,pers_document,birth_date,phone_number FROM client
WHERE FIO LIKE '%га%';

SELECT languages.name_language FROM languages
INNER JOIN composition_languages ON languages.id_language=composition_languages.id_language
INNER JOIN country ON composition_languages.id_country=country.id_country
WHERE country.name_country='Франция';

SELECT * FROM client
WHERE DATE_PART('year',now()::date)-DATE_PART('year', client.birth_date::date) < 18;

UPDATE client SET phone_number=NULL where DATE_PART('year',now()::date)-DATE_PART('year', client.birth_date::date) < 18;

SELECT fio, birth_date, degree_of_relative, relativies.id_client FROM relativies
LEFT JOIN client on client.id_client=relativies.id_client_child;
SELECT relativives.id_client_child, relativies.degree_of_relative, relativies.id_client, client.fio FROM relativies
INNER JOIN client on client.id_client=relativies.id_client_child
WHERE client.id_client=155;

Select relativies.id_client, relativies.id_client_child, fio, birth_date, relativies.degree_of_relative from relativies
INNER JOIN client on client.id_client = relativies.id_client_child
WHERE relativies.id_client = 6;

Select *  from client
where phone_number='-';

Select name_country,currency,name_language from country
INNER JOIN composition_languages on country.id_country = composition_languages.id_country
INNER JOIN languages on languages.id_language = composition_languages.id_language;