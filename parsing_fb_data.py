import json

f = open('test2.json', 'r')
parsed = json.load(f)

"""
Examples of how to navigate the JSON object
"""

print(parsed['data'][0]['name'])
# --> Kim Crawford 2016 Page Post #79

print(parsed['data'][0]['targetingsentencelines']['targetingsentencelines'][0])
# --> {'children': ['United States'], 'content': 'Location:'}
print(parsed['data'][0]['targetingsentencelines']['targetingsentencelines'][1])
# --> {'children': ['People who like Kim Crawford Wines'], 'content': 'Connections:'}
print(parsed['data'][0]['targetingsentencelines']['targetingsentencelines'][2])
# --> {'children': ['21 - 65+'], 'content': 'Age:'}

print(str(parsed['data'][0]['targeting']['age_min']) + ' - ' + str(parsed['data'][0]['targeting']['age_max']))
# --> 21 - 65


for x in parsed['data']:
    print('name of the adset is %s, the min age targeted was %d, and the location was %s' % (x['name'], x['targeting']['age_min'], x['targetingsentencelines']['targetingsentencelines'][0]['children'][0]))







# for item in parsed['data']:
#     print(item['name'])










f.close()
