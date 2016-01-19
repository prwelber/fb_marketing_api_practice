from facebookads.api import FacebookAdsApi
from facebookads import FacebookSession, FacebookAdsApi, objects
from facebookads.objects import Insights, Ad, AdCreative
import os

"""
Using this Ad for the practice
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


my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
# need to use access token for more_practice app
my_access_token = 'CAAN4vFUE2ZAgBAKSMW9O8u1khNOv3x2uZAVNUCm03u3GO9RAefXADtJkM4frMYx2dfmhPJ2lcLfgJ5pgAlnqSx5ZBD07ra381pT6LoJzE8qjJ0csNfzzcYlpjYtbJEOuLZCWQaZBniyDigCNoFt0H0NXDAupCHz6Ncpdrwwmt8dnT106chkTMZCFBeqldMGrztr6sn3VDAh1MMd5a3KbFk' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)


def get_ad_creative_data(adcreative):
    creative = AdCreative(adcreative)
    fields = [AdCreative.Field.name, AdCreative.Field.body, AdCreative.Field.image_url, AdCreative.Field.object_url, AdCreative.Field.adlabels, AdCreative.Field.call_to_action_type, AdCreative.Field.image_hash, AdCreative.Field.link_url, AdCreative.Field.title]
    creative.remote_read(fields=fields)
    return creative

creative_data = get_ad_creative_data(6025991716655)
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



