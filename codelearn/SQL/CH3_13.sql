select concat(upper(left(ename,1)),lower(right(ename,length(ename)-1))), #不使用substring
left(lower(ename),1),lower(ename),upper(left(lower(ename),1)),
replace(lower(ename),left(lower(ename),1),upper(left(lower(ename),1)))
from cmdev.emp