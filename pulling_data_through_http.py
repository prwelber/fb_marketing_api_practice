from facebookads.api import FacebookAdsApi
from facebookads import FacebookSession, FacebookAdsApi, objects
from facebookads.objects import Insights, Ad, AdCreative, AdAccount, Campaign, AdSet
import os
import requests
import json

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
# need to use access token for more_practice app
my_access_token = 'CAAN4vFUE2ZAgBAKu7jH6FpIyI7xAo2ZCIjFM1NfZC2seEDZBU1rQ0lyhZBjIvJwO6hTHIjnU3haDsmAaQx8F7wQmQcMPlZCyiYYBcFX0zFcNnUy71wmWkGjfvZAe1ta35hoLX5kOVmncLnHZBaoofCZCk1izTUpMThcs2mVOZAtkEKqGKseIZCFNqcZAAuMGMiOYCX48QqbkIe4T6SoNOrKKu3GC' #Your user access token
# FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

kim_crawford_acct_num = 807247179325378

r = requests.get('https://httpbin.org/get')
print(r.text)
print('\n')
for thing in r.headers:
    print("%s: %s" % (thing, r.headers[thing]))
print('\n')
for thing in r:
    print(thing)
print('\n')
print(r.json())
print('\n')

# ACCESS CAMPAIGN DATA

def get_campaign_info(camp_id):
    camp_url = 'https://graph.facebook.com/v2.5/%d?access_token=%s' % (camp_id, my_access_token)
    payload = {'fields': 'name, id, objective, start_time'}
    camp = requests.get(camp_url, params=payload)
    print(camp.text)
    return camp

get_campaign_info(6039958653409)

"""
the above get request returns:
{'id': '6039958653409', 'start_time': '2016-01-06T12:00:00-0800', 'name': 'Kim Crawford 2016 Page Post #75'}
--headers:
{'Facebook-API-Version': 'v2.5', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'X-FB-Trace-ID': 'AMtGbeuGN5C', 'Date': 'Wed, 20 Jan 2016 17:09:38 GMT', 'Content-Type': 'application/json; charset=UTF-8', 'ETag': '"3b388bf90d394f571af198db4662d43f381595c6"', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Access-Control-Allow-Origin': '*', 'X-FB-Debug': '18dh9EyRKBfxFwrCHm1UC2yNM8QsMHdI4M/qgGo/tni3n0Yejx5xtPE5hIAwaJVPthcV914JGfubYKl2cpFLgQ==', 'Content-Length': '103', 'X-FB-Rev': '2136283', 'Cache-Control': 'private, no-cache, no-store, must-revalidate'}

"""

# GET INSIGHTS ON CAMPAIGN
 #payload = {'fields': 'date_start,cpm,ctr,spend,campaign_id,reach'}
 #insights_url = 'https://graph.facebook.com/v2.5/6039958653409/insights?access_token=%s' % my_access_token
 #insights = requests.get(insights_url, params=payload)
 #insights = insights.json()
 #print(json.dumps(insights, indent=4, separators=(',',':')))

# ACCESS ADSET THROUGH CAMPAIGN

def get_adset_through_camp(camp_id):
    adsets_url = 'https://graph.facebook.com/v2.5/%d/adsets?access_token=%s' % (camp_id, my_access_token)
    payload = {'fields': 'name, id, campaign, lifetime_budget, end_time'}
    adsets = requests.get(adsets_url, params=payload)
    adsets = adsets.json()
    print(json.dumps(adsets, indent=4, separators=(',', ':')))
    return adsets

#adsets = get_adset_through_camp(6039958653409)
#adset_id = adsets['data'][0]['id']


# ACCESS AD THROUGH ADSET THROUGH CAMPAIGN

def get_ad_through_adset_from_campaign(camp_id):
    ad_url = 'https://graph.facebook.com/v2.5/%d/adsets?fields=name,id,campaign,end_time,lifetime_budget,ads{campaign_id,creative,adset,name,id,created_time,bid_amount}&access_token=%s' % (camp_id, my_access_token)
    ad_data = requests.get(ad_url)
    ad_data = ad_data.json()
    print(json.dumps(ad_data, indent=4, separators=(',', ':')))
    return ad_data

#ad_data = get_ad_through_adset_from_campaign(6039958653409)


