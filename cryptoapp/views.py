import requests
from django.conf import settings
from django.shortcuts import render
def index(request):
    apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en').json()
    return render(request, 'index.html',{'apidata':apidata})