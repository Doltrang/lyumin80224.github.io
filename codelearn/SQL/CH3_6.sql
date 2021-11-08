select concat(ename,",",job,1),concat_ws("#",ename,job,1),locate("s",ename)
from cmdev.emp