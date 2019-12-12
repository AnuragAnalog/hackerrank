-- Database Used: EMPLOYEE1(employee1.sql)

select months*salary, count(*)
from Employee
group by months*salary
order by months*salary desc
limit 1;