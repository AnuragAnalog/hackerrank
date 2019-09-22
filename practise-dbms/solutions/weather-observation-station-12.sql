-- Database Used: STATION(station.sql)

select distinct CITY
from STATION
where substring(CITY, length(CITY), length(CITY)) not in ('a','e','i','o','u') and substring(CITY, 1,1) not in ('a','e','i','o','u');