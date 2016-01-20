"""
allowed accounts for app:
<AdAccount> {
    "age": 179.93262731481,
    "amount_spent": "42500",
    "id": "act_997253660324728",
    "name": "American Vintage",
    "owner": "678433138873450"

     <AdAccount> {
    "age": 105.865,
    "amount_spent": "514980",
    "id": "act_1031447726905321",
    "name": "Varidesk",
    "owner": "678433138873450"

    Kim Crawford
    act_807247179325378

    <AdAccount> {
    "age": 298.89887731481,
    "amount_spent": "869565",
    "id": "act_933960369987391",
    "name": "Pop Crush",
    "owner": "678433138873450"

    <AdAccount> {
    "age": 50.080706018519,
    "amount_spent": "6537887",
    "id": "act_1013209698729124",
    "name": "Constellation Canada",
    "owner": "678433138873450"
"""


from facebookads.api import FacebookAdsApi
from facebookads.objects import AdUser, Campaign, AdAccount, AdSet
from facebookads import FacebookSession, FacebookAdsApi, objects
import os

my_app_id = os.environ['APP_ID']
my_app_secret = os.environ['APP_SECRET']
my_access_token = 'CAAN4vFUE2ZAgBAO1GMrTP4dU0r57IZAZBsm2bEbyNHOZArQAqnKVMclEjIaKmjVBsZAMKGrzIZAXbscAe6vthkeLymFG2FCDlONI7KcQuLAjCRnI3HVwQejY7zr5dIZAmMYmiVa8AYZA65Cb0RkfJieOVbrzZC6wCiIoXZBunYjcZBHBB8gTtTkibJ27F3QmoUsXteK9ZClZBuoLQnIWjy0oiZA9Vu' #Your user access token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = AdUser(fbid='me')
fields = [
    AdAccount.Field.age, #amount of time it's been open, in days
    AdAccount.Field.name,
    AdAccount.Field.amount_spent,
    AdAccount.Field.owner,
]
my_accounts = me.get_ad_accounts(fields=fields)
# print(my_accounts)
num = 1
for acct in my_accounts:
    print(num)
    print(acct['name'])
    print("id num: %s" % acct['id'])
    num += 1




"""
prints this:
[<AdAccount> {
    "age": 33.881238425926,
    "amount_spent": "14149056",
    "id": "act_1024124827637611",
    "name": "Woodbridge DLX 2016",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 472.97993055556,
    "amount_spent": "0",
    "id": "act_829187503798012",
    "name": "(placeholder)",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_118226858553015",
    "name": "Philip Welber",
    "owner": "132110120498022"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_1031774830205944",
    "name": "Hewlett Packard",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_1063473403702753",
    "name": "FredLoya",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_1041967639186663",
    "name": "UofL Athletics",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_1052330698150357",
    "name": "WRR",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 228.88174768519,
    "amount_spent": "157362",
    "id": "act_971534009563360",
    "name": "Royal Ontario Museum",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 55.06349537037,
    "amount_spent": "4606396",
    "id": "act_1044635718919855",
    "name": "Russell Stover",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 105.865,
    "amount_spent": "514980",
    "id": "act_1031447726905321",
    "name": "Varidesk",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 211.07309027778,
    "amount_spent": "952677",
    "id": "act_981773618539399",
    "name": "Microsoft",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 244.93571759259,
    "amount_spent": "521651",
    "id": "act_963052403744854",
    "name": "Churchill Downs",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 179.93262731481,
    "amount_spent": "42500",
    "id": "act_997253660324728",
    "name": "American Vintage",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 179.92900462963,
    "amount_spent": "61151",
    "id": "act_997253460324748",
    "name": "Okanagan",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_943146492402112",
    "name": "DELETE",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 50.080706018519,
    "amount_spent": "6537887",
    "id": "act_1013209698729124",
    "name": "Constellation Canada",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_1006561952727232",
    "name": "University of Louisville",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_999404050109689",
    "name": "Ruffino Canada",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 259.07313657407,
    "amount_spent": "3200000",
    "id": "act_946663412050420",
    "name": "Damp Rid",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 229.99542824074,
    "amount_spent": "191515",
    "id": "act_971018509614910",
    "name": "Stoli Canada",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_916124548437640",
    "name": "Beau tea Bar",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 298.89887731481,
    "amount_spent": "869565",
    "id": "act_933960369987391",
    "name": "Pop Crush",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 188.97081018519,
    "amount_spent": "1738647",
    "id": "act_984030844980343",
    "name": "Ravage",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 0,
    "amount_spent": "0",
    "id": "act_914609801922448",
    "name": "Wine Social 2",
    "owner": "678433138873450"
}, <AdAccount> {
    "age": 256.91128472222,
    "amount_spent": "0",
    "id": "act_957390147644413",
    "name": "Brickwell",
    "owner": "678433138873450"
}]

1
Woodbridge DLX 2016
id num: act_1024124827637611
2
(placeholder)
id num: act_829187503798012
3
Philip Welber
id num: act_118226858553015
4
Hewlett Packard
id num: act_1031774830205944
5
FredLoya
id num: act_1063473403702753
6
UofL Athletics
id num: act_1041967639186663
7
WRR
id num: act_1052330698150357
8
Royal Ontario Museum
id num: act_971534009563360
9
Russell Stover
id num: act_1044635718919855
10
Varidesk
id num: act_1031447726905321
11
Microsoft
id num: act_981773618539399
12
Churchill Downs
id num: act_963052403744854
13
American Vintage
id num: act_997253660324728
14
Okanagan
id num: act_997253460324748
15
DELETE
id num: act_943146492402112
16
Constellation Canada
id num: act_1013209698729124
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
24
Wine Social 2
id num: act_914609801922448
25
Brickwell
id num: act_957390147644413
26
Make Your Date
id num: act_813352932048136
27
Mouton Cadet
id num: act_946615285388566
28
Alaska NEA
id num: act_894519797264782
29
DELETE
id num: act_958925550824206
30
Syosset School Board
id num: act_957863184263776
31
Virtual360NY
id num: act_863163410400421
32
Rosatello
id num: act_915039361879492
33
100% Cork
id num: act_859789240737838
34
Ashley
id num: act_847543851962377
35
Pan Am Games
id num: act_820092818040814
36
Dreaming Tree
id num: act_833425423374220
37
wine.social
id num: act_905853179464777
38
Lincoln
id num: act_815622175154545
39
Franciscan
id num: act_852503464799749
40
AGO
id num: act_813910548659041
41
MyFace
id num: act_901566989893396
42
Svedka
id num: act_886755114707917
43
S_DFL Party
id num: act_815458645170898
44
100% Cork
id num: act_859790500737712
45
Marathon Ventures
id num: act_830940790289350
46
Simi
id num: act_852245011492261
47
Ford
id num: act_871618469554915
48
RMPS
id num: act_800317280018368
49
Toasted Head
id num: act_714007831982647
50
Palm Bay
id num: act_760673993982697
51
Nobilo
id num: act_815532661830163
52
S_Sara Gelser1
id num: act_824197254297037
53
Joe Gallegos
id num: act_837095103007252
54
Ashley Home
id num: act_847549505295145
55
Voices
id num: act_783121651737931
56
WIHS
id num: act_833301290053300
57
Clos Du Bois
id num: act_813429925373770
58
Houston Hall
id num: act_712692835447480
59
Milestone Wines
id num: act_843446492372113
60
UnitedMethodistChurch
id num: act_721788747871222
61
Gilt
id num: act_718179964898767
62
BlackBox
id num: act_1380947658816783
63
MarkWestDLX
id num: act_728442070539223
64
Cape Cod
id num: act_682881168428647
65
CityOfPhoenix
id num: act_705723046144459
66
Flatiron Hall
id num: act_766956763354420
67
Heartland Brewery
id num: act_727245510658879
68
SCRealtors
id num: act_704663432917087
69
Port Chester Hall
id num: act_712621555454608
70
ThornyRose
id num: act_1378201735758977
71
LouAna
id num: act_1381618325397926
72
OCAD
id num: act_678438115539619
73
TommyWells
id num: act_705699889480108
74
Marie's Dressing
id num: act_1378391212402760
75
TSAmtrak
id num: act_100994386773062
76
Deans
id num: act_1374502039449882
77
HomeDepot
id num: act_101467763371270
78
Yenta
id num: act_100465720125538
79
MikesHard
id num: act_101639669931786
80
Luchese
id num: act_1052227944827299
81
MarkWestDLX2016
id num: act_968506049866156
82
UofLouisville
id num: act_1015519135164847
83
Code Redd
id num: act_903086166408145
84
Tom Gore
id num: act_903219059728189
85
Robert Mondavi Winery
id num: act_832124100171019
86
Ruffino
id num: act_867733226610106
87
Trust for Public Land
id num: act_808396535877109
88
Kim Crawford
id num: act_807247179325378
89
Mizzen+Main
id num: act_829220923794670
90
Rex Goliath
id num: act_805588439491252
91
Arbor Mist
id num: act_800316826685080
92
Hitachi
id num: act_791535684229861
93
Woodbridge
id num: act_800317096685053
94
MarkWest
id num: act_1374542932792679
95
ConstellationBrands
id num: act_728442737205823
96
Estancia
id num: act_1381091345468800
97
DavidBarton
id num: act_1381807678724601
98
FarmRich
id num: act_717213121662118
99
Mondavi2
id num: act_108294695945331
100
The Trust for Public Land
id num: act_106149062841250
101
Targeted Social
id num: act_1301844886508449
[Finished in 1.9s]

"""
