select dayofyear(curdate()),dayofyear("2021-12-31"),
dayofyear(concat(year(curdate()),"-12-31")),
dayofyear("2024-12-31"),
dayofyear(concat(year(curdate()),"-12-31"))-dayofyear(curdate()),
datediff(concat(year(curdate()),"-12-31"),curdate()),
datediff("2024-7-26",curdate()),
adddate(curdate(),-1),
curdate()+8,
adddate(curdate(),8)