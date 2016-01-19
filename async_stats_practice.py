from facebookads.api import FacebookAdsApi
from facebookads.objects import AdUser, Campaign, Insights
from facebookads import FacebookSession, FacebookAdsApi, objects
import os
import time

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
my_access_token = 'CAAVLUoRrZBPUBAE9o9MSwetl6nH6jarPQdK7miXganZBmh2CX23vlNFQ4pzvCX8FnmqKuBD4pQCDxkkae2FqZCaxbuwI8qC97Vvqc2nFPsT93AKTYYc65D0NRZB1ywyiPcZBuf1xaMPWwfaaMy99pGSbONl1XDXKePPFcxkWqTckB5eNm5FtAkP4j3JUBSqSPXVUXOwVju8t1hetLzbZCe' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)



campaign = Campaign('6039958653409')
params = {
    'level': Insights.Level.campaign,
}
async_job = campaign.get_insights(params=params, async=True)

async_job.remote_read()

while async_job['async_percent_completion'] < 100:
    time.sleep(1)
    async_job.remote_read()

print(async_job.get_result())

"""
returns this:

[<Insights> {
    "actions": [
        {
            "action_type": "comment",
            "value": 19
        },
        {
            "action_type": "photo_view",
            "value": 389
        },
        {
            "action_type": "post",
            "value": 30
        },
        {
            "action_type": "post_like",
            "value": 598
        },
        {
            "action_type": "page_engagement",
            "value": 1036
        },
        {
            "action_type": "post_engagement",
            "value": 1036
        }
    ],
    "app_store_clicks": 0,
    "buying_type": "AUCTION",
    "call_to_action_clicks": 0,
    "campaign_id": "6039958653409",
    "cost_per_action_type": [
        {
            "action_type": "comment",
            "value": 34.324736842105
        },
        {
            "action_type": "photo_view",
            "value": 1.676529562982
        },
        {
            "action_type": "post",
            "value": 21.739
        },
        {
            "action_type": "post_like",
            "value": 1.0905852842809
        },
        {
            "action_type": "page_engagement",
            "value": 0.62950772200772
        },
        {
            "action_type": "post_engagement",
            "value": 0.62950772200772
        }
    ],
    "cost_per_estimated_ad_recallers": 0.088972714870396,
    "cost_per_inline_link_click": 0,
    "cost_per_inline_post_engagement": 0.63440661478599,
    "cost_per_total_action": 0.62950772200772,
    "cost_per_unique_action_type": [
        {
            "action_type": "comment",
            "value": 38.362941176471
        },
        {
            "action_type": "photo_view",
            "value": 1.7117322834646
        },
        {
            "action_type": "post",
            "value": 21.739
        },
        {
            "action_type": "post_like",
            "value": 1.1053728813559
        },
        {
            "action_type": "page_engagement",
            "value": 0.64063850687623
        },
        {
            "action_type": "post_engagement",
            "value": 0.64063850687623
        }
    ],
    "cost_per_unique_click": 0.51595727848101,
    "cpm": 4.1149228022134,
    "cpp": 6.3766316304082,
    "ctr": 0.87892535128621,
    "date_start": "2016-01-06",
    "date_stop": "2016-01-07",
    "deeplink_clicks": 0,
    "estimated_ad_recall_rate": 7.1669518455145,
    "estimated_ad_recall_rate_lower_bound": 0.00097775604986556,
    "estimated_ad_recall_rate_upper_bound": 26.39941334637,
    "estimated_ad_recallers": 7330,
    "estimated_ad_recallers_lower_bound": 1,
    "estimated_ad_recallers_upper_bound": 27000,
    "frequency": 1.5496357858714,
    "impressions": "158489",
    "inline_link_clicks": 0,
    "inline_post_engagement": 1028,
    "reach": 102275,
    "social_clicks": 0,
    "social_impressions": 0,
    "social_reach": 0,
    "spend": 652.17,
    "total_action_value": 0,
    "total_actions": 1036,
    "total_unique_actions": 1018,
    "unique_actions": [
        {
            "action_type": "comment",
            "value": 17
        },
        {
            "action_type": "photo_view",
            "value": 381
        },
        {
            "action_type": "post",
            "value": 30
        },
        {
            "action_type": "post_like",
            "value": 590
        },
        {
            "action_type": "page_engagement",
            "value": 1018
        },
        {
            "action_type": "post_engagement",
            "value": 1018
        }
    ],
    "unique_clicks": 1264,
    "unique_ctr": 1.2358836470301,
    "unique_impressions": 102275,
    "unique_link_clicks_ctr": 0,
    "unique_social_clicks": 0,
    "unique_social_impressions": 0,
    "website_clicks": 1512
}]
"""