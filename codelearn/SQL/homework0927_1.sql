use mydb;
create TABLE covid(
	`確定病名` varchar(20),
    `發病年份` varchar(20),
    `發病月份` varchar(20),
    `縣市` varchar(20),
    `鄉鎮` varchar(20),
    `性別` varchar(20),
    `是否為境外移入` varchar(20),
    `年齡層` varchar(20),
    `確定病例數` int
)