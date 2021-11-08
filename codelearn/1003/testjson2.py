import json
from datetime import datetime,date

def json_serial(obj):
    if isinstance(obj, (datetime,date)):
        return obj.isoformat()
    raise TypeError('Type {} not serizlize'.format(type(obj)))


print(datetime.now())
print(json.dumps(datetime.now().isoformat()))