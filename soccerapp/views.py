from django.shortcuts import render

import requests
from datetime import datetime

# Create your views here.

def index(request):
    url = 'https://apiv3.apifootball.com/?action=get_events&from=2023-02-01&to=2023-02-07&league_id=164&APIkey=ba3ed274d9d1bc601524bf1422864036f2bfcacd977264d887fa1954bd9772e9'
    r = requests.get(url)
    jsonResp = r.json()
#    print(jsonResp)

    return render(request, 'soccerapp/index.html', {'jr': jsonResp})

def today(request):
    today = datetime.today().strftime('%Y-%m-%d')
    url = f'https://apiv3.apifootball.com/?action=get_events&from={today}&to={today}&league_id=164&APIkey=ba3ed274d9d1bc601524bf1422864036f2bfcacd977264d887fa1954bd9772e9'
    print(url)
    r = requests.get(url)
    jsonResp = r.json()

    return render(request, 'soccerapp/index.html', {'jr': jsonResp})