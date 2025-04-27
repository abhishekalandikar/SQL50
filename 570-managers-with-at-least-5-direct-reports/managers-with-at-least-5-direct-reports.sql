select name 
from employee
where id in
(select managerid
from Employee
group by managerId
having count(*) >=5)
