-- Databases Used: city, country

select cty.NAME
from CITY as cty, COUNTRY as cou
where cou.CONTINENT = 'Africa' and cou.CODE = cty.COUNTRYCODE;