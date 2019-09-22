-- Database Used: STATION(station.sql)

select round(min(LAT_N), 4)
from STATION
where LAT_N > 38.7780;