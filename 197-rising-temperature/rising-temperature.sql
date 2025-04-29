select w1.id
from Weather w1
join Weather w2
on datediff(w1.recorddate,w2.recorddate) = 1
where w2.temperature < w1.temperature