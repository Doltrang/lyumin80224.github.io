select *,floor((rand()*10)+1) "隨機等級"
from cmdev.emp 
order by rand()
#0<= rand() <1
#0<= rand()*10 <10 #9.9999999999
#1<= rand()*10+1 <11 #10.999999999
#1<= floor((rand()*10)+1) <=10 