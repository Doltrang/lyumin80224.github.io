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

print(nobel_winners)
cols = list(nobel_winners[0].keys())
cols.sort()

# o = nobel_winners[0]
# print(o['category'])
# print(o['name'])
# print(o['nationality'])
# print(o['sex'])
# print(o['year'])
# print('forin',[o[col] for col in cols])

# print(cols)

with open('nobel_winners.csv','w') as fw:
    print(','.join(cols))
    fw.write(','.join(cols)+'\n')
    for o in nobel_winners:
        print(o)
        row = [ str(o[col]) for col in cols]
        print(','.join(row))
        fw.write(','.join(row)+'\n')