score = int(input('請輸入成績:'))
if score>100 or score <0 :
    print('輸入錯誤')
elif score >= 90:
    print('及格，得到A')
elif score >= 80:
    print('及格，得到B')
elif score >= 70:
    print('及格，得到C')
elif score >= 60:
    print('及格，得到D')
else:
    print('不及格，得到F')