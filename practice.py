from facebookads.api import FacebookAdsApi
from facebookads.objects import AdUser, Campaign, AdAccount, AdSet
from facebookads import FacebookSession, FacebookAdsApi, objects

#Initialize a new Session and instanciate an Api object


my_access_token = 'CAAVLUoRrZBPUBAK9sokJX2nLXaRkvGtn8OaqQ3dQ7HvYGnKtZApxVx6TRggnYvpHUawUHkOiZC97t8ibN1E3sfbrPlpp3GeOmx1BSAwg3HChZARFliLEoIOfQainDTMFP4ZAXfoMqZAKFKF1f2VR1i093lOjlJe0nXtVU3McIEJMZCv0ZAALvo32KaC9HZCZBKXtViMG4BOkRpqBaeESC5SYPx' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

#me = AdUser(fbid='me')
#print('next print is me')
#print(me)
#my_accounts = me.get_ad_accounts()
#acct_id = my_accounts[0]['account_id']
#account = AdAccount(acct_id)
#print('no error yet')
#adsets = account.get_ad_sets(fields=[AdSet.Field.name])

#for adset in adsets:
#    print(adset[AdSet.Field.name])

#adsets = account.get_ad_sets(fields=[AdSet.Field.name])
#print('next print is adset in adsets')
#for adset in adsets:
#    print(adset[AdSet.Field.name])

"""
i think this doesn't work because I don't have any add
accounts. if i were using TS's account I would probably have
numerous accounts...not sure

Settings for this were:
require app secret: Yes
Allow api access to app settings: Yes
Client Oauth login: Yes
Migrations: on
"""









