import requests
import json
import os

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
# need to use access token for more_practice app
my_access_token = 'CAAN4vFUE2ZAgBANbcpNn6V8D6TDg90AURSp9AuV1PPSiELsXEVSS7QiQJZCqQFpNiie2WFKNHxeaENWtvZCfBRxS0ksBowEN5TQ6dcJaRL7Qw9b4uEm8Sml5xZBkBIEMlBXEpReAidHu6K7jdFMoe5aZBNmydl0bxXgLleZBZA6OZCIoDp2iCYLts7ySZBWgnRIpnWsuYhT5gpQSFxjXMfyEK' #Your user access token
# FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

graph_url_string = 'https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=fb_exchange_token&fb_exchange_token=%s' % (my_app_id, my_app_secret, my_access_token)

# token = requests.get(graph_url_string)
print(url_string)
print(token)
print(token.text)
print(token.headers)

# This was received on Jan 21, 2016
long_live_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG'

# Expires in 5183999 (in seconds, which equals 60 days)

"""
complete print out:
access_token=CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG&expires=5183999
HEADER:
{'X-FB-Trace-ID': 'BhX/PFE2zdl', 'X-FB-Debug': 'CdH3kEPI8nA0bxAos3zfVN/hgv2x06MCsLssiJpKFVrkr05ldTu2wtT0V3WR9Gc7pZx4PtzgJbmST6/NhM0h8w==', 'Cache-Control': 'private, no-cache, no-store, must-revalidate', 'Content-Length': '214', 'Access-Control-Allow-Origin': '*', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'Pragma': 'no-cache', 'Connection': 'keep-alive', 'Facebook-API-Version': 'v2.0', 'Date': 'Thu, 21 Jan 2016 18:32:02 GMT', 'X-FB-Rev': '2139660', 'Content-Type': 'text/plain; charset=UTF-8'}
"""
