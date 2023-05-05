import requests
import os
from dotenv import load_dotenv

load_dotenv()

req_cat = {
    "Eat and Drink" : "100",
    "Entertainment" : "200,300",
    "Transport" : "400-4100",
    "Leisure" : "500",
    "Shopping": "600",
    "Services": "700",
    "Facilities": "800", 
}

def get(distance):
    url = 'https://browse.search.hereapi.com/v1/browse?apiKey=' + os.getenv('HERE_API_KEY') + '&at=28.636507423890134,77.29259567115122&categories=900-9300-0221&limit=100&r='+str(distance)
    response = requests.request("GET",url)
    resp = response.json()
    coord = set()
    for x in resp['items']:
        coord.add((x['access'][0]['lat'], x['access'][0]['lng'], x['title']))
    return coord

def get_cat(x,y,category):
    url = 'https://browse.search.hereapi.com/v1/browse?apiKey='+ os.getenv('HERE_API_KEY') + '&at='+str(x)+','+str(y)+'&categories='+category+'&in=circle:'+str(x)+','+str(y)+';r=500&limit=100'
    response = requests.request("GET",url)
    resp = response.json()
    return len(resp['items'])

def get_final(x,y,distance):
    url = 'https://browse.search.hereapi.com/v1/browse?apiKey=' + os.getenv('HERE_API_KEY') + '&at='+str(x)+','+str(y)+'&categories=900-9300-0221&limit=100&r='+str(distance)
    response = requests.request("GET",url)
    resp = response.json()
    coord = set()
    for x in resp['items']:
        coord.add((x['access'][0]['lat'], x['access'][0]['lng'], x['title']))
    return coord
