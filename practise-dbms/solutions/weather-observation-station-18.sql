-- Database Used: STATION(station.sql)

select round((max(LAT_N)-min(LAT_N)) + (max(LONG_W)-min(LONG_W)), 4)
from STATION;