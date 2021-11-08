select *,isnull(deptno),ifnull(deptno,"無部門") "部門"
from cmdev.emp