from facebookads.api import FacebookAdsApi
from facebookads import FacebookSession, FacebookAdsApi, objects
from facebookads.objects import Insights, Ad, AdCreative
import os

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
# need to use access token for more_practice app
my_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)









