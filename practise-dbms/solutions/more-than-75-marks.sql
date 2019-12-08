-- Database used: students

select Name
from STUDENTS
where Marks > 75
-- order by '%___', ID;
order by substring(Name, length(Name)-2,length(Name)), ID;