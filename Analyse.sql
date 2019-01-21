create database google;
use google;

create table data(Category varchar(30),Rating float,Review int,Size_ varchar(10),Installs varchar(20),Type varchar(20),Price int,Content_rating varchar(20),Genres varchar(20),Last_Updated varchar(20),Current_Ver varchar(10),Android_Ver varchar(10))
row format delimited
fields terminated by ',';
load data inpath 'google/GooglePlay_App_review.csv' overwrite into table data;

create table Category_types(Category varchar(20),count_ int)
row format delimited
fields terminated by ',';
insert into table Category_types select Category,count(Category) from data group by(Category);
insert overwrite local directory '/home/edureka/Desktop/Data/Category' row format delimited fields terminated by ',' select * from Category_types;

create table Types(Type varchar(20),count_ int)
row format delimited
fields terminated by ',';
insert into table Types select Type,count(Type) from data group by(Type);
insert overwrite local directory '/home/edureka/Desktop/Data/Type' row format delimited fields terminated by ',' select * from Types;

create table Content(Content varchar(20),count_ int)
row format delimited
fields terminated by ',';
insert into table Content select Content_rating,count(Content_rating) from data group by(Content_rating);
insert overwrite local directory '/home/edureka/Desktop/Data/Content' row format delimited fields terminated by ',' select * from Content;

create table Genre(Genre varchar(20),count_ int)
row format delimited
fields terminated by ',';
insert into table Genre select Genres,count(Genres) from data group by(Genres);
insert overwrite local directory '/home/edureka/Desktop/Data/Genre' row format delimited fields terminated by ',' select * from Genre;
