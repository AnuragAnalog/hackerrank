-- Databases Used: CITY(city.sql), COUNTRY(country.sql)

select cty.NAME
from CITY as cty, COUNTRY as cou
where cou.CONTINENT = 'Africa' and cou.CODE = cty.COUNTRYCODE;
