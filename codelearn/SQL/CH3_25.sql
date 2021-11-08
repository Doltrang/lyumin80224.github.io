select Region,sum(Population)
from world.country
group by Region
having sum(Population) > 1000000000
#select 欄位
#from 資料表
#where 條件1 [and/or] 條件2
#group by 分組欄位
#having 分組後條件
#order by 欄位 [asc/desc]
#limit 數字