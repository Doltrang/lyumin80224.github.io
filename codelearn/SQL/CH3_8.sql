#select concat(left(ename,1)),lower(substring(ename,2)) #首字原為大寫可不轉換
#select concat(upper(left(ename,1)),lower(substring(ename,2)))#將首字轉換為大寫，第2字開始轉換為小寫並連接輸出
select concat(upper(left(ename,1)),lower(right(ename,length(ename)-1))) #不使用substring
from cmdev.emp