import json
import random
import time
import tweepy
consumer_key = 'L35E1SwBQnLfRalLKx6YK5I6B'
consumer_secret = 'rtEh2fcOwC6eBlD0hefCaKVhtvf5LMb01gaAdJ33TGAP15aGfs'
access_token= "1499774234129743877-jTS39Twb6vYQ7q8sBYTbShBo49HOQt"
access_secret = "qVMMIsZnp0qHoMrdCEfAsbod9GJxkl6Q5GxHhPTykIhXF"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def main():
    with open("azkar.json", "r") as read_file:
        data = json.load(read_file)  
    t = random.choice(data)
    #print(t)
    category = t["category"]
    zekr = t["zekr"]
    l = len(zekr)
    print(l)
    while l > 160:
        t = random.choice(data)
        category = t["category"]
        zekr = t["zekr"]
        l = len(zekr)
        print(l)
    #print(category)
    #print(zekr)
    print("التصنيف : "+category+"\nالذكر : "+zekr+"\n")
    api.update_status("التصنيف : "+category+"\nالذكر : "+zekr+"\n#اذكار")
    print("Tweeted")
   

while True:
    main()
    time.sleep(1800)
