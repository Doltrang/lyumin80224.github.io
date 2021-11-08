import csv
with open('nobel_winners2.csv','r') as fr:
    reader = csv.DictReader(fr)
    nobel_winners = list(reader)
    for w in nobel_winners:
        w['year']=int(w['year'])
    print(nobel_winners)