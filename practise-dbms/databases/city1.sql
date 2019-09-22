create database if not exists hackerrank;
use hackerrank;

create table if not exists CITY1 
(
    ID int primary key,
    NAME varchar(17),
    COUNTRYCODE varchar(3),
    DISTRICT varchar(20),
    POPULATION int
);

insert into CITY1 values (6, "Rotterdam", "NLD", "Zuid-Holland", 593321);
insert into CITY1 values (3878, "Scottsdale", "USA", "Arizona", 202705);
insert into CITY1 values (3965, "Corona", "USA", "California", 124966);
insert into CITY1 values (3973, "Concord", "USA", "California", 121780);
insert into CITY1 values (3977, "Cedar Rapids", "USA", "Iowa", 120758);
insert into CITY1 values (3982, "Coral Springs", "USA", "Florida", 117549);
insert into CITY1 values (4054, "Fairfield", "USA", "California", 92256);
insert into CITY1 values (4058, "Boulder", "USA", "Colorado", 91238);
insert into CITY1 values (4061, "Fall River", "USA", "Massachusetts", 90555);
