-- Database Used: STATION(station.sql)

select round(max(LAT_N), 4)
from STATION
where LAT_N < 137.2345;