from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import csv
import re 
import requests
import requests
from collections import defaultdict
try:
    import json
except ImportError:
    import simplejson as json

def remove_handles(input_txt):
    pattern = "@[\w]*"
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt

def find_sentiment(input_txt):
    text_analytics_base_url = "https://centralindia.api.cognitive.microsoft.com/text/analytics/v2.0/"
    subscription_key = '389726ec04f84154b12f7facf1ae1a05'
    sentiment_api_url = text_analytics_base_url + "sentiment"
    documents = {'documents' : [{'id': '1', 'language': 'en', 'text': input_txt}]}
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()
    return sentiments

def find_phrases(input_txt):
    text_analytics_base_url = "https://centralindia.api.cognitive.microsoft.com/text/analytics/v2.0/"
    subscription_key = '389726ec04f84154b12f7facf1ae1a05'
    phrases_api_url = text_analytics_base_url + "keyPhrases"
    documents = {'documents' : [{'id': '1', 'language': 'en', 'text': input_txt}]}
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(phrases_api_url, headers=headers, json=documents)
    phrases = response.json()
    return phrases

def find(city):
    disasters = ["Flood","Tsunami","Earthquake","Rain","Cyclone","Storm","Hurricane","Landslide","Waves","Famine","Violence","Riot"]
    pos = {}
    neg = {}
    for disaster in disasters:
        pos[disaster] = 0
        neg[disaster] = 0

    ACCESS_TOKEN = '1051698216943550465-t6GwP9uoXLn6ACR6xNPjaLY2JKFNLA'
    ACCESS_SECRET = '74vXoNq76SDLl6c4zvO4zRaHHX6SOvBFLrz7RFSTHLi9D'
    CONSUMER_KEY = 'Jw1rUipyiUZnIaJBTAawMDDFk'
    CONSUMER_SECRET = 'ZQBJpB84GmRN9mx8RA8T2bVIbHlfCPUfdSWl6T0xXEid9xDQcO'

    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    t = TwitterStream(auth=oauth)
    
    iterator = t.statuses.filter(track=city, language="en")
    
    count = 10
    rows=[]
    missed=0
    for tweet in iterator:
        if(count<1):
                break
        count = count-1
        text=(tweet['text'])
        text.replace('(', '')
        text.replace(')', '')
        text.replace('"', '')
        text.replace("'", '')
        text.replace('\\', '')
        text = remove_handles(text)

        phrases = find_phrases(text)
        for item in phrases['documents'][0]['keyPhrases']:
            for check in disasters:
                if(check.lower() == item.lower()):
                    sentiment = find_sentiment(text)
                    if sentiment['documents'][0]['score'] > 0.45:
                        pos[check] += 1
                    else:
                        neg[check] += 1
    
    return pos,neg    


def main():
    new_dic = defaultdict(dict)
    dec_dic = defaultdict(dict)

    disasters = ["Flood","Tsunami","Earthquake","Rain","Cyclone","Storm","Hurricane","Landslide","Waves","Famine","Violence","Riot"]
    
    cities = ["Mumbai","Chennai","Kolkata","Delhi"]
    
    for city in cities:
        for disaster in disasters:
            new_dic[city][disaster] = 0

    for city in cities:
        for disaster in disasters:
            dec_dic[city][disaster] = 0

    while(1):
        rows = []
        for city in cities:
            temp = []
            temp.append(city)
            pos,neg = find(city)
            print(city)
            for disaster in disasters:
                if(pos[disaster] > dec_dic[city][disaster]):
                    temp.append("decreasing")
                elif(neg[disaster] > new_dic[city][disaster]):
                    temp.append("increasing")
                else:
                    temp.append("Almost constant")

                if(neg[disaster] > 1.8*new_dic[city][disaster]):
                    temp.append("High Risk")
                elif(neg[disaster] > 1.4*new_dic[city][disaster]):
                    temp.append("Moderate Risk")

                else:
                    temp.append("Low Risk")

                new_dic[city][disaster] = neg[disaster]
                dec_dic[city][disaster] = pos[disaster]

            rows.append(temp)
            print(city)
        with open('result.csv',"w+") as file:
            wr=csv.writer(file)
            wr.writerows(rows)


if __name__ == '__main__':
    main()