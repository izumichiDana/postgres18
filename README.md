* `\c` - like cd and pwd 

* `\l `- shiw all bd

* `\dt`  - show all tablisy in bd

* `\du` - show all users

* `\q` - exit



`'CREATE DTABASE name_of_db'`- sozdaet bazzu dannyh 
```sql
`'CREATE TABLE name_of_table'` - (
    name_of_column1 data_type constraint,
    name_of_column2 data_type constraint,
    ... 
); -- sozdaet tablisu s pilyami
```
```sql
INSERT INTO name_of_table(name_of_column1,name_of_column2)
VALUES (val1,val2); - add zapisi v tablisu 

```
```sql
SELECT* FROM name_of_tabledostayot vse pola i zapisi iz tablisi
SELECT name_of_column1, name_of_column2 FROM name_of_table; dostaet ukazannye 
```

> primary kye (pk) - pervichnyi kluch 

> его мы указываем на те поля, которые должны бфть уникальнфми для того, потоm использовать в связях (например id)

> foreign key (fk) - внещний ключ 

>это ограничение , которое мы указываем на те поля , которые ссфлаются на pk в другой таблице , для создания связей 

``` sql
CREATE TABLE author (
    id serial primary key, 
    first_name varchar (50),
    last_name varchar (50)
)

CREATE TABLE book (
    id serial ,
    title varchar(100),
    published year 
    author_id int foreign key references author (id)

)
```

> JOIN - инструкция , которая в запросах  SELECT  брать данные из нескольких таблиц 

> INNER JOIN (JOIN)  - когда достаются  только те записи у которых есть полная связь 


``` sql
SELECT author.first_name, book.title
FROM author
JOIN  book ON author.id = book.author_id
```