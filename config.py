import tweepy

"""
مفاتيح تويتر غير الاكس للمفاتيح حقت حسابك
تقدر تجيب مفاتيح لحسابك بتويتر من هنا
developer.twitter.com 
"""    
consumer_key = "xxxxxx"
consumer_secret = "xxxxxx"
access_token= "xxxxxx"
access_secret = "xxxxxx"

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)