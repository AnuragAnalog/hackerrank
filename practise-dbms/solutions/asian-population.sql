-- Databases Used: city, country

select sum(cty.POPULATION)
from CITY as cty, COUNTRY as cou
where cou.CONTINENT = 'Asia' and cou.CODE = cty.COUNTRYCODE;