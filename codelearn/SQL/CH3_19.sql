select *,
case
	when salary >=3000 then "高"
    when salary >=2000 then "中"
	else "普"
end "薪資等級"
from cmdev.emp