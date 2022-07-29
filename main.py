import json
import random
import time
import tweepy
#استبدل الاكس بالمفاتيح الخاصة بحسابك
#تجيب المفاتيح من هنا
#developer.twitter.com/apps
consumer_key = 'xxxxxxx'
consumer_secret = 'xxxxx'
access_token= "xxxxx"
access_secret = "xxxxxx"

#مصادقة لمكتبة tweepy مع twitter api ما يحتاج تغير فيها الا لو بتستعمل api v2
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def main():
    #فتح ملف الأذكار
    with open("azkar.json", "r") as read_file:
        data = json.load(read_file)
    #اختيار ذِكر عشوائي
    random_azkar = random.choice(data)
    category = random_azkar["category"]
    zekr = random_azkar["zekr"]
    #عدد حروف الذِكر
    l = len(zekr)
    print(l)
#في حالة ان الذكر اكثر من ١٦٠ حرف  يتم الاختيار مره اخرى لان تويتر لا يقبل اكثر من ١٨٠ حرف
    while l > 160:
        random_azkar = random.choice(data)
        category = random_azkar["category"]
        zekr = random_azkar["zekr"]
        l = len(zekr)
        print(l)
    #استبدال المسافه بـ _ 
    category_hashtag = category.replace(" ", "_")
    #صيغة التغريدة النهائية
    fulltweet = f"{zekr}\n\n#{category_hashtag}\n#اذكار"
    #نشر الذكر في تويتر
    api.update_status(fulltweet)
    print("تم التغريد\nالتغريدة : {fulltweet}\nانتظار نصف ساعة...")
   
#تكرار مع انتظار ١٨٠٠ ثانية يساوي نصف ساعة
while True:
    main()
    time.sleep(1800)
