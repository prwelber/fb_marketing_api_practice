from facebookads.api import FacebookAdsApi
from facebookads import FacebookSession, FacebookAdsApi, objects
from facebookads.objects import Campaign, Insights, Ad
import os

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
# need to use access token for more_practice app
my_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)


"""
The below function gets ad information, not insights. This includes the creative id. Getting basic data, and
not insights is done through the .remote_read(fields=fields) call
"""
# Varidesk A - 6030758669406
def get_ad_info(ad):
    ad = Ad(ad)
    fields = [
        Ad.Field.id,
        Ad.Field.adset_id,
        Ad.Field.creative,
        Ad.Field.name,
        Ad.Field.conversion_specs,
        Ad.Field.created_time,
    ]
    ad.remote_read(fields=fields)
    return ad

info = get_ad_info(6025997618255)
print(info)

"""
Above function returns:
<Ad> {
    "adset_id": "6025968221255",
    "created_time": "2015-03-27T14:10:32-0400",
    "creative": {
        "id": "6025991716655"
    },
    "id": "6025997618255",
    "name": "PopCrush 2016 RHS"
}

or this:
<Ad> {
    "adset_id": "6030758660006",
    "conversion_specs": [
        {
            "action.type": [
                "link_click"
            ],
            "post": [
                "927957720630217"
            ],
            "post.wall": [
                "422448051181189"
            ]
        }
    ],
    "created_time": "2015-10-05T17:31:27-0400",
    "creative": {
        "id": "6032775709806"
    },
    "id": "6030758669406",
    "name": "Varidesk A"
}

or:
<Ad> {
    "adset_id": "6025968221255",
    "created_time": "2015-03-27T14:10:32-0400",
    "creative": {
        "id": "6025991716655"
    },
    "id": "6025997618255",
    "name": "PopCrush 2016 RHS"
}
"""


"""
The below function gets ad insights through the Ad insights edge. Thus the call .get_insights
"""
def get_ad_insights(ad):
    ad = Ad(ad)
    params = {
        'time_range': {
            'since': '2015-04-01',
            'until': '2015-04-03',
        },
        'time_increment': 1,
    }
    insights = ad.get_insights(params=params)
    return insights

# stats = get_ad_insights(6025997618255)
# print(stats)


"""
This prints out:
[<Insights> {
    "account_id": "933960369987391",
    "actions": [
        {
            "action_type": "link_click",
            "value": 136
        },
        {
            "action_type": "page_engagement",
            "value": 136
        },
        {
            "action_type": "post_engagement",
            "value": 136
        }
    ],
    "ad_id": "6025997618255",
    "adset_id": "6025968221255",
    "app_store_clicks": 0,
    "call_to_action_clicks": 0,
    "campaign_id": "6025968220255",
    "cost_per_action_type": [
        {
            "action_type": "link_click",
            "value": 0.43933823529412
        },
        {
            "action_type": "page_engagement",
            "value": 0.43933823529412
        },
        {
            "action_type": "post_engagement",
            "value": 0.43933823529412
        }
    ],
    "cost_per_estimated_ad_recallers": 0.019784768211921,
    "cost_per_inline_link_click": 0.44259259259259,
    "cost_per_inline_post_engagement": 0.44259259259259,
    "cost_per_total_action": 0.43933823529412,
    "cost_per_unique_action_type": [
        {
            "action_type": "link_click",
            "value": 0.45610687022901
        },
        {
            "action_type": "page_engagement",
            "value": 0.45610687022901
        },
        {
            "action_type": "post_engagement",
            "value": 0.45610687022901
        }
    ],
    "cost_per_unique_click": 0.49380165289256,
    "cpm": 0.95653565996958,
    "cpp": 1.1643088195175,
    "ctr": 0.2177219242776,
    "date_start": "2015-04-01",
    "date_stop": "2015-04-01",
    "deeplink_clicks": 0,
    "estimated_ad_recall_rate": 5.8848747028333,
    "estimated_ad_recall_rate_lower_bound": 0.0019486340075607,
    "estimated_ad_recall_rate_upper_bound": 18.473050391675,
    "estimated_ad_recallers": 3020,
    "estimated_ad_recallers_lower_bound": 1,
    "estimated_ad_recallers_upper_bound": 9480,
    "frequency": 1.2172142328228,
    "impressions": "62465",
    "inline_link_clicks": 135,
    "inline_post_engagement": 135,
    "reach": 51318,
    "relevance_score": {
        "negative_feedback": "LOW",
        "positive_feedback": "HIGH",
        "score": 8,
        "status": "OK"
    },
    "social_clicks": 0,
    "social_impressions": 0,
    "social_reach": 0,
    "spend": 59.75,
    "total_action_value": 0,
    "total_actions": 136,
    "total_unique_actions": 131,
    "unique_actions": [
        {
            "action_type": "link_click",
            "value": 131
        },
        {
            "action_type": "page_engagement",
            "value": 131
        },
        {
            "action_type": "post_engagement",
            "value": 131
        }
    ],
    "unique_clicks": 121,
    "unique_ctr": 0.23578471491484,
    "unique_impressions": 51318,
    "unique_link_clicks_ctr": 0.25527105499045,
    "unique_social_clicks": 0,
    "unique_social_impressions": 0,
    "website_clicks": 0,
    "website_ctr": [
        {
            "action_type": "link_click",
            "value": 0.2177219242776
        }
    ]
}, <Insights> {
    "account_id": "933960369987391",
    "actions": [
        {
            "action_type": "link_click",
            "value": 250
        },
        {
            "action_type": "page_engagement",
            "value": 250
        },
        {
            "action_type": "post_engagement",
            "value": 250
        }
    ],
    "ad_id": "6025997618255",
    "adset_id": "6025968221255",
    "app_store_clicks": 0,
    "call_to_action_clicks": 0,
    "campaign_id": "6025968220255",
    "cost_per_action_type": [
        {
            "action_type": "link_click",
            "value": 0.42456
        },
        {
            "action_type": "page_engagement",
            "value": 0.42456
        },
        {
            "action_type": "post_engagement",
            "value": 0.42456
        }
    ],
    "cost_per_estimated_ad_recallers": 0.018020373514431,
    "cost_per_inline_link_click": 0.42626506024096,
    "cost_per_inline_post_engagement": 0.42626506024096,
    "cost_per_total_action": 0.42456,
    "cost_per_unique_action_type": [
        {
            "action_type": "link_click",
            "value": 0.435
        },
        {
            "action_type": "page_engagement",
            "value": 0.435
        },
        {
            "action_type": "post_engagement",
            "value": 0.435
        }
    ],
    "cost_per_unique_click": 0.45165957446809,
    "cpm": 0.8101733468693,
    "cpp": 1.0597467949998,
    "ctr": 0.19311650344633,
    "date_start": "2015-04-02",
    "date_stop": "2015-04-02",
    "deeplink_clicks": 0,
    "estimated_ad_recall_rate": 5.8808259115779,
    "estimated_ad_recall_rate_lower_bound": 0.0009984424298095,
    "estimated_ad_recall_rate_upper_bound": 18.471184951476,
    "estimated_ad_recallers": 5890,
    "estimated_ad_recallers_lower_bound": 1,
    "estimated_ad_recallers_upper_bound": 18500,
    "frequency": 1.3080494428691,
    "impressions": "131009",
    "inline_link_clicks": 249,
    "inline_post_engagement": 249,
    "reach": 100156,
    "relevance_score": {
        "negative_feedback": "LOW",
        "positive_feedback": "HIGH",
        "score": 8,
        "status": "OK"
    },
    "social_clicks": 0,
    "social_impressions": 0,
    "social_reach": 0,
    "spend": 106.14,
    "total_action_value": 0,
    "total_actions": 250,
    "total_unique_actions": 244,
    "unique_actions": [
        {
            "action_type": "link_click",
            "value": 244
        },
        {
            "action_type": "page_engagement",
            "value": 244
        },
        {
            "action_type": "post_engagement",
            "value": 244
        }
    ],
    "unique_clicks": 235,
    "unique_ctr": 0.23463397100523,
    "unique_impressions": 100156,
    "unique_link_clicks_ctr": 0.24361995287352,
    "unique_social_clicks": 0,
    "unique_social_impressions": 0,
    "website_clicks": 0,
    "website_ctr": [
        {
            "action_type": "link_click",
            "value": 0.19082658443313
        }
    ]
}, <Insights> {
    "account_id": "933960369987391",
    "actions": [
        {
            "action_type": "link_click",
            "value": 283
        },
        {
            "action_type": "page_engagement",
            "value": 283
        },
        {
            "action_type": "post_engagement",
            "value": 283
        }
    ],
    "ad_id": "6025997618255",
    "adset_id": "6025968221255",
    "app_store_clicks": 0,
    "call_to_action_clicks": 0,
    "campaign_id": "6025968220255",
    "cost_per_action_type": [
        {
            "action_type": "link_click",
            "value": 0.49141342756184
        },
        {
            "action_type": "page_engagement",
            "value": 0.49141342756184
        },
        {
            "action_type": "post_engagement",
            "value": 0.49141342756184
        }
    ],
    "cost_per_estimated_ad_recallers": 0.022039619651347,
    "cost_per_inline_link_click": 0.49491103202847,
    "cost_per_inline_post_engagement": 0.49491103202847,
    "cost_per_total_action": 0.49141342756184,
    "cost_per_unique_action_type": [
        {
            "action_type": "link_click",
            "value": 0.50025179856115
        },
        {
            "action_type": "page_engagement",
            "value": 0.50025179856115
        },
        {
            "action_type": "post_engagement",
            "value": 0.50025179856115
        }
    ],
    "cost_per_unique_click": 0.53903100775194,
    "cpm": 0.95394556329913,
    "cpp": 1.2960615831951,
    "ctr": 0.1941228118312,
    "date_start": "2015-04-03",
    "date_stop": "2015-04-03",
    "deeplink_clicks": 0,
    "estimated_ad_recall_rate": 5.8805986840879,
    "estimated_ad_recall_rate_lower_bound": 0.00093194907830236,
    "estimated_ad_recall_rate_upper_bound": 18.452591750387,
    "estimated_ad_recallers": 6310,
    "estimated_ad_recallers_lower_bound": 1,
    "estimated_ad_recallers_upper_bound": 19800,
    "frequency": 1.3586326443123,
    "impressions": "145784",
    "inline_link_clicks": 281,
    "inline_post_engagement": 281,
    "reach": 107302,
    "relevance_score": {
        "negative_feedback": "LOW",
        "positive_feedback": "MEDIUM",
        "score": 7,
        "status": "OK"
    },
    "social_clicks": 0,
    "social_impressions": 0,
    "social_reach": 0,
    "spend": 139.07,
    "total_action_value": 0,
    "total_actions": 283,
    "total_unique_actions": 278,
    "unique_actions": [
        {
            "action_type": "link_click",
            "value": 278
        },
        {
            "action_type": "page_engagement",
            "value": 278
        },
        {
            "action_type": "post_engagement",
            "value": 278
        }
    ],
    "unique_clicks": 258,
    "unique_ctr": 0.24044286220201,
    "unique_impressions": 107302,
    "unique_link_clicks_ctr": 0.25908184376806,
    "unique_social_clicks": 0,
    "unique_social_impressions": 0,
    "website_clicks": 0,
    "website_ctr": [
        {
            "action_type": "link_click",
            "value": 0.1941228118312
        }
    ]
}]
[Finished in 1.3s]

"""

