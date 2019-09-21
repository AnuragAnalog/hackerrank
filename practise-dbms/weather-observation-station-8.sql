-- Database Used: STATION(station.sql)

select distinct CITY
from STATION
where substring(CITY,1,1) in ('a','e','i','o','u') and substring(CITY,length(CITY),length(CITY)) in ('a','e','i','o','u');