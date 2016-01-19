from facebookads.api import FacebookAdsApi
from facebookads.objects import AdUser, Campaign, AdAccount, AdSet
from facebookads import FacebookSession, FacebookAdsApi, objects
import os

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
my_access_token = 'CAAN4vFUE2ZAgBALsZALHEGJQSEHXi0ETZBbGN5wn4FIVpG1czX99dCkE7AyxyQ5fGXE1cAGZB4HA1UEqtQu8xhCNaOlExMykDHsNl0K3NxeYoadfgSGmJVfQbp2jLHmlRZB2Mn942xGUdQuzBZAKHmIlrgHd6lMtpRgT3g21miZCkIYbXtZB7qfT7T25RxyYpOCV97wviGMHsdDbe3Sqvo1J' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

"""
17
University of Louisville
id num: act_1006561952727232
18
Ruffino Canada
id num: act_999404050109689
19
Damp Rid
id num: act_946663412050420
20
Stoli Canada
id num: act_971018509614910
21
Beau tea Bar
id num: act_916124548437640
22
Pop Crush
id num: act_933960369987391
23
Ravage
id num: act_984030844980343
27
Mouton Cadet
id num: act_946615285388566
28
Alaska NEA
id num: act_894519797264782
30
Syosset School Board
id num: act_957863184263776
31
Virtual360NY
id num: act_863163410400421
32
Rosatello
id num: act_915039361879492
"""

def get_adsets_from_adaccount(account_id):
    account = AdAccount(account_id)
    fields = [
        AdSet.Field.name,
    ]
    adsets = account.get_ad_sets(fields=fields)
    return adsets

# ad_sets = get_adsets_from_adaccount(933960369987391)
# print(ad_sets)

def get_adsets(adset_id):
    adset = AdSet(adset_id)
    fields = [
        AdSet.Field.name,
    ]
    adset.remote_read(fields=fields)
    return adset

print(get_adsets(6038392137438))



"""
is it possible that I have to do adset.get_insights??
something to think about here
"""