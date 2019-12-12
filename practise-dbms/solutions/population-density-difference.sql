-- Database Used: CITY2(city2.sql)

select ((select max(POPULATION) from CITY) - (select min(POPULATION) from CITY));