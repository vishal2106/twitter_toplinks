from django.http import JsonResponse
import json
import twitter
from requests_oauthlib import OAuth1Session
from urllib.parse import urlsplit
import operator
from .models import *
from dateutil.parser import parse
from datetime import datetime
from pytz import timezone
import pytz

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
TWITTER_REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
TWITTER_ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

def request_oauth_token(request):
    request_token = OAuth1Session(
        client_key=CONSUMER_KEY, client_secret=CONSUMER_SECRET, callback_uri="http://localhost:3000/tweets"
    )
    data = request_token.get(TWITTER_REQUEST_TOKEN_URL)

    if data.status_code == 200:
        request_token = str.split(data.text, '&')
        oauth_token = str.split(request_token[0], '=')[1]
        oauth_callback_confirmed = str.split(request_token[2], '=')[1]
        return JsonResponse({
            "oauth_token": oauth_token,
            "oauth_callback_confirmed": oauth_callback_confirmed,
        })
    else:
        return JsonResponse({
            "oauth_token": None,
            "oauth_callback_confirmed": "false",
        })


def request_access_token(request):
    oauth_token = OAuth1Session(
        client_key=CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=request.GET.get("oauth_token"),
    )
    data = {"oauth_verifier": request.GET.get("oauth_verifier")}
    response = oauth_token.post(TWITTER_ACCESS_TOKEN_URL, data=data)
    access_token = str.split(response.text, '&')
    access_token_key = str.split(access_token[0], '=')[1]
    access_token_secret = str.split(access_token[1], '=')[1]
    api = twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret,
    )
    timeline = api.GetHomeTimeline(count=200)

    tweets_val =[]
    top_users = []
    top_links = []
    topUsers={}
    topLinks ={}

    for i,t in enumerate(timeline):
        timeline[i] = json.loads(json.dumps(t._json))
        try:
            if type(timeline[i]['entities']['urls'][0]['expanded_url'])==str:
                
                name = timeline[i]['user']['name']
                if name in topUsers.keys():
                    topUsers[name]+=1
                else:
                    topUsers[name]=1

                url = urlsplit(timeline[i]['entities']['urls'][0]['expanded_url']).netloc
                if url in topLinks.keys():
                    topLinks[url]+=1
                else:
                    topLinks[url]=1
                
                updated_date = parse(timeline[i]['created_at'])
                tweets_values ={
                "name": timeline[i]['user']['name'],
                "text": timeline[i]['text'],
                "url": timeline[i]['entities']['urls'][0]['expanded_url'],
                "date": updated_date,
                "img": timeline[i]['user']['profile_image_url_https']
                }
                tweets_val.append(tweets_values)
        except:
            pass
    ##Saving to MongoDB Atlas
    try:
        response = Tweets(timeline).save()
    except:
        print("Error in saving data to Cloud")

    topUsers = sorted(topUsers.items(), key=operator.itemgetter(1), reverse=True)
    topLinks = sorted(topLinks.items(), key=operator.itemgetter(1), reverse = True)

    for i in topUsers:
        top ={
            "name": i[0],
            "count": i[1]
        }
        top_users.append(top)
    
    for i in topLinks:
        top ={
            "url": i[0],
            "count": i[1]
        }
        top_links.append(top)
    
    return JsonResponse({
        "tweets": tweets_val,
        "topUsers": top_users,
        "topLinks": top_links
    })
