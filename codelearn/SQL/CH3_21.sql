select *
from cmdev.emp;
select job,sum(salary) "薪資成本",
count(*) "員工數", max(salary) "最高薪", min(salary) "最低薪", avg(salary) `平均薪資`
from cmdev.emp
group by job
order by `平均薪資` desc