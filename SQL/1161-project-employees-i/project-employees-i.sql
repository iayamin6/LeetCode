# Write your MySQL query statement below
select p.project_id, Round(AVG(experience_years),2) as average_years
from Project p
Inner Join Employee e
on p.employee_id = e.employee_id
group by p.project_id