import json
data ={'A':123,'B':456}
with open('data.json','w') as f:
    json.dump(data,f)