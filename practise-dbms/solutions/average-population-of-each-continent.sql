-- Databases Used: city, country

select cou.CONTINENT, floor(avg(cty.POPULATION))
from CITY as cty
inner join COUNTRY as cou on cou.CODE = cty.COUNTRYCODE
group by cou.CONTINENT;