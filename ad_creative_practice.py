from facebookads.api import FacebookAdsApi
from facebookads import FacebookSession, FacebookAdsApi, objects
from facebookads.objects import Insights, Ad, AdCreative
import os

"""
Using this Ad for the practice
<Ad> {
    "adset_id": "6039958654209",
    "created_time": "2015-12-23T07:56:57-0800",
    "creative": {
        "id": "6039958707009"
    },
    "id": "6039958655009",
    "name": "Kim Crawford 2016 Page Post #75"
}
"""


my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
# need to use access token for more_practice app
my_access_token = 'CAAN4vFUE2ZAgBAIeTGIB4ZCS61BoTFz0UXEDBivceAk686epdYJ5KKJvZAp4QqXVIwoM1ECOhgMDh5xHicblud2mHEsZAfhz0nWfDOjnZBwPGvcaaEZCytahrgomIEXQ3G5SuKqRPriiq6S8ZAkAqEOSxiZC3JbBZBqZCtbeXQu4UJFxMKCIEMtSo9gdP1DR5mp2ktZAVZANRpEoyCwN8GPyVW0G' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)


def get_ad_creative_data(adcreative):
    creative = AdCreative(adcreative)
    fields = [AdCreative.Field.name, 
              AdCreative.Field.body, 
              AdCreative.Field.image_url, 
              AdCreative.Field.object_url, 
              AdCreative.Field.adlabels, 
              AdCreative.Field.call_to_action_type, 
              AdCreative.Field.image_hash, 
              AdCreative.Field.link_url, 
              AdCreative.Field.title, 
              AdCreative.Field.template_url, 
    ]
    creative.remote_read(fields=fields)
    return creative

varidesk_creative_id = 6032775709806
popcrush_creative_id = 6025991716655
creative_data = get_ad_creative_data(popcrush_creative_id)
print(creative_data)



"""
This returns:
<AdCreative> {
    "body": "Win a vacation to Palm Springs, San Diego, or Lake Tahoe from PopCrush Wines! Enter now!",
    "id": "6025991716655",
    "image_hash": "410baf7addc749331cbe7e3edf360e33",
    "image_url": "https://scontent.xx.fbcdn.net/hads-xaf1/t45.1600-4/s110x80/10736793_6025968204455_1324170848_n.png",
    "name": "Win a trip to California!",
    "object_url": "http://wine.social/PopCrushLoveCA",
    "title": "Win a trip to California!"
}
"""


def thumbnail_url_dimensions(adcreative):
    creative = AdCreative(adcreative)
    fields = [AdCreative.Field.thumbnail_url, AdCreative.Field.body, AdCreative.Field.id, AdCreative.Field.name]
    params = {
        'thumbnail_width': 150,
        'thumbnail_height': 120,
    }
    creative.remote_read(params=params, fields=fields)
    return creative

# info = thumbnail_url_dimensions(6025991716655)
# print(info)

"""
Above function returns:
<AdCreative> {
    "body": "Win a vacation to Palm Springs, San Diego, or Lake Tahoe from PopCrush Wines! Enter now!",
    "id": "6025991716655",
    "name": "Win a trip to California!",
    "thumbnail_url": "https://external.xx.fbcdn.net/safe_image.php?d=AQCg4ty2n2653-Zh&w=150&h=120&url=https%3A%2F%2Fscontent.xx.fbcdn.net%2Fhads-xta1%2Ft45.1600-4%2F10550628_6025968204655_1209165442_n.jpg&cfs=1"
}
"""



