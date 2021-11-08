SELECT `縣市`,sum(`確定病例數`) "確診總數"
from mydb.covid
GROUP BY `縣市`
ORDER BY sum(`確定病例數`) asc
limit 5