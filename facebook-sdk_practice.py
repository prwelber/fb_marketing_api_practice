import facebook
import requests
import os

access_token = os.environ['ACCESS_TOKEN']

adset = '6033443163806'

graph = facebook.GraphAPI(access_token)
result = graph.get_object(adset)

print(result)
    

