-- Database Used: employee1

select months*salary, count(*)
from Employee
group by months*salary
order by months*salary desc
limit 1;