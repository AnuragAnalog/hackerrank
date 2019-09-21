-- Database Used: STATION(station.sql)

select count(city) - count(distinct city)
from station;