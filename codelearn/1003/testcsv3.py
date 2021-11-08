nobel_winners = [
{'category': 'Physics',
'name': 'Albert Einstein',
'nationality': 'Swiss',
'sex': 'male',
'year': 1921},
{'category': 'Physics',
'name': 'Paul Dirac',
'nationality': 'British',
'sex': 'male',
'year': 1933},
{'category': 'Chemistry',
'name': 'Marie Curie',
'nationality': 'Polish',
'sex': 'female',
'year': 1911}
]

import csv
fieldnames = list(nobel_winners[0].keys())
fieldnames.sort()

with open('nobel_winners2.csv','w',newline='') as fw:
    writer = csv.DictWriter(fw,fieldnames=fieldnames)
    writer.writeheader()
# 1.
    # writer.writerows(nobel_winners)
# 2.
    for w in nobel_winners:
        writer.writerow(w)