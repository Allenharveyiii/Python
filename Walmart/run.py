from Walmart import Walmart as Wal
import json
#Walmart.search(query='Google Home')

w = Wal();

parsedJson = json.loads(w.search('ipod').content)
for item in parsedJson['items']:
    print('Name: {}'.format(item['name']))
    try:
        print('MSRP: {}'.format(item['msrp']))
    except:
        print('MSRP: None')
    print('\n')
#print(w.productLookup())
