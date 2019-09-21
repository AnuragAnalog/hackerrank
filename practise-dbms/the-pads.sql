-- Database Used: OCCUPATIONS1(occupations1.sql)

select concat(Name,"(",substring(Occupation,1,1),")")
from OCCUPATIONS
order by Name;
select concat("There are a total of ",count(*)," ",lower(Occupation),"s.") as a
from OCCUPATIONS
group by Occupation
order by count(*), Occupation;