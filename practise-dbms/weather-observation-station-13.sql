-- Database Used: STATION(station.sql)

select round(sum(LAT_N), 4)
from STATION
where LAT_N between 38.7880 and 137.2345;