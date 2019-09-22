-- Database used: TRIANGLES(triangles.sql)

select if (A+B <= C, "Not A Triangle", if (A = B and B = C, "Equilateral", if (A = B or B = C or A = C, "Isosceles", "Scalene")))
from TRIANGLES;
