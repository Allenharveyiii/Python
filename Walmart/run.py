import Walmart

#Walmart.search(query='Google Home')

thisDict = {
    'Test1': 1,
    'Test2': 2,
    'Test3': {
        'SubItem1': 1,
        'SubItem2': 2
    }
}
print(thisDict['Test3']['SubItem2'])