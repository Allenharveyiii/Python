import config, requests

class Walmart:
    def __init__(self):
        self.URL = 'http://api.walmartlabs.com/v1'
        self.API_KEY = config.API_KEY

    def productLookup(self, IsPublisherId=None, format=None, ids=None, upc=None):
        payload = \
        {
            'apiKey': config.API_KEY,
            'IsPubisherId': IsPublisherId,
            'format': format,
            'ids': ids,
            'upc': upc
        }

        return requests.get(self.URL+'/items', payload)

    def search(self, query, IsPublisherId=None, categoryId=None, start=None, sort=None, order=None, numItems=None,
               format=None, responseGroup=None, facet=None, facetFilter=None, facetRange=None):
        payload = \
            {
                'apiKey': config.API_KEY,
                'query': query,
                'start': start,
                'IsPubisherId': IsPublisherId,
                'categoryId': categoryId,
                'sort': sort,
                'order': order,
                'numItems': numItems,
                'format': format,
                'responseGroup': responseGroup,
                'facet': facet,
                'facet.filter': facetFilter,
                'facet.range': facetRange
            }
        return requests.get(self.URL+'/search', params=payload)

    #def structureReturn(self, Json, query):
    #    parsedJson = json.loads(Json.content)
    #    returnDict = []
    #    count = 0
    #    for item in parsedJson['items']:
    #        returnDict += [[
    #            item['name'],
    #            item['salePrice'],
    #            item['upc'],
    #            item['availableOnline']
    #        ]]
    #        count += 1;
    #    return returnDict

    #def searchQuery(self, query, returnPattern, IsPublisherId=None, categoryId=None, start=None, sort=None, order=None, numItems=None,
    #           format=None, responseGroup=None, facet=None, facetFilter=None, facetRange=None):
    #    Json = Walmart.search(self, query, IsPublisherId, categoryId, start, sort, order, numItems, format, responseGroup, facet, facetFilter, facetRange)
    #
    #    return Walmart.structureReturn(self, Json, returnPattern)