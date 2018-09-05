import config, requests, json

def search(query,IsPublisherId=None,categoryId=None,start=None, sort=None, order=None, numItems=None, format=None, responseGroup=None, facet=None, facetFilter=None, facetRange=None):
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
    r = requests.get('http://api.walmartlabs.com/v1/search', params=payload)

    parsedJson = json.loads(r.content)
    count = 0
    for item in parsedJson['items']:
        print(count,item['name'])
        count += 1