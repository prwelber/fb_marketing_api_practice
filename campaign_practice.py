from facebookads.api import FacebookAdsApi
from facebookads import FacebookSession, FacebookAdsApi, objects
from facebookads.objects import Campaign, Insights, AdSet, Ad
import datetime
import os

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
my_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

# campaign id 6039958653409
camp_id = 6039958653409


def campaign_lookup(campaign_id):
    campaign = Campaign(campaign_id)
    fields = [
        Campaign.Field.name,
        Campaign.Field.effective_status,
        Campaign.Field.objective,
        Campaign.Field.account_id,
    ]
    campaign.remote_read(fields=fields)
    return campaign

# print(campaign_lookup(camp_id))

"""
prints out:
<Campaign> {
    "account_id": "807247179325378",
    "effective_status": "ACTIVE",
    "id": "6039958653409",
    "name": "Kim Crawford 2016 Page Post #75",
    "objective": "POST_ENGAGEMENT"
}

and to print that nicely:
for i in campaign:
  print('%s: %s' % (i, obj[i]))

"""

def get_campaign_insights(campaign_id):
    campaign = Campaign(campaign_id)
    insights = campaign.get_insights(fields=[
        Insights.Field.cpm,
        Insights.Field.spend,
        Insights.Field.campaign_name,
        Insights.Field.account_name,
        Insights.Field.ad_name,
        Insights.Field.adset_name,
    ])
    return insights

# print(get_campaign_insights(camp_id))

"""
above function returns:
[<Insights> {
    "account_name": "Kim Crawford",
    "campaign_name": "Kim Crawford 2016 Page Post #75",
    "cpm": 4.1149228022134,
    "date_start": "2016-01-06",
    "date_stop": "2016-01-07",
    "spend": 652.17
}]
"""


# This calls for all adsets under one campaign
def get_adsets_under_campaign(campaign_id):
    campaign = Campaign(campaign_id)
    fields = [
        AdSet.Field.id,
        AdSet.Field.account_id,
        AdSet.Field.name,
    ]
    adsets = campaign.get_ad_sets(fields=fields)
    return adsets

# print(get_adsets_under_campaign(camp_id))

"""
above function returns:
[<AdSet> {
    "account_id": "807247179325378",
    "id": "6039958654209",
    "name": "Kim Crawford 2016 Page Post #75"
}]
"""

def get_ads_under_campaign(campaign_id):
    campaign = Campaign(campaign_id)
    fields = [
        Ad.Field.id,
        Ad.Field.created_time,
        Ad.Field.name,
        Ad.Field.account_id,
    ]
    ads = campaign.get_ads(fields=fields)
    return ads

print(get_ads_under_campaign(camp_id))

"""
Above function returns:
[<Ad> {
    "account_id": "807247179325378",
    "created_time": "2015-12-23T07:56:57-0800",
    "id": "6039958655009",
    "name": "Kim Crawford 2016 Page Post #75"
}]
"""



# lookup campaign insights within timeframe
def campaign_stats_time_range(campaign_id):
    today = datetime.date.today()
    start_time = str(today - datetime.timedelta(weeks=1))
    end_time = str(today)
    campaign = Campaign(campaign_id)
    params = {
        'time_range': {
            'since': start_time,
            'until': end_time,
        },
        'fields': [
            Insights.Field.impressions,
            Insights.Field.unique_clicks,
            Insights.Field.reach,
            Insights.Field.account_name,
            Insights.Field.account_id,
            Insights.Field.cpm,
            Insights.Field.spend,
            Insights.Field.campaign_id,
            Insights.Field.campaign_name
        ],
    }
    insights = campaign.get_insights(params=params)
    return insights

# print(campaign_stats_time_range(camp_id))



"""
prints out:
[<Insights> {
    "account_id": "807247179325378",
    "account_name": "Kim Crawford",
    "campaign_id": "6039958653409",
    "campaign_name": "Kim Crawford 2016 Page Post #75",
    "cpm": 4.0528827150037,
    "date_start": "2015-12-31",
    "date_stop": "2016-01-07",
    "impressions": "141672",
    "reach": 98599,
    "spend": 574.18,
    "unique_clicks": 1137
}]

and to print that nicely:
for i in campaign:
  print('%s: %s' % (i, obj[i]))

"""

