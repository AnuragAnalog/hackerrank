-- Database Used: STATION(station.sql)

select round(sqrt((max(LAT_N)-min(LAT_N))*(max(LAT_N)-min(LAT_N)) + (max(LONG_W)-min(LONG_W))*(max(LONG_W)-min(LONG_W))), 4)
from STATION;