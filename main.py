import json
import random
import time
import tweepy
from pytz import timezone
from datetime import datetime
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
    morning = ["02", "03", "04", "05"]
    night = ["15", "16", "17", "18"]
    types = list(data.keys())
    now_utc = datetime.now(timezone('UTC'))
    time = now_utc.strftime("%H")
    day = now_utc.strftime("%A")
    if time in morning:
        type = "أذكار الصباح"
    elif time in night:
        type = "أذكار المساء"
    elif time == "09" and day.lower() == "friday":
        print("يوم الجمعة، جار تغريد سورة الكهف")
        api.update_status("‏‎#سورة_الكهف ‎#يوم_الجمعه pic.twitter.com/7TvzlEoQhj‎‎‎")
    else:
        type = random.choice(['تسابيح', 'أدعية قرآنية', 'أدعية الأنبياء'])
    random_azkar = random.choice(data[types[types.index(type)]])
    category = random_azkar["category"]
    zekr = random_azkar["zekr"]
    #عدد حروف الذِكر
    l = len(zekr)
    print(l)
#في حالة ان الذكر اكثر من ٢٦٠ حرف  يتم الاختيار مره اخرى لان تويتر لا يقبل اكثر من ٢٨٠ حرف
    if l > 280:
        return main()
    #استبدال المسافه بـ _ 
    category_hashtag = category.replace(" ", "_")
    #صيغة التغريدة النهائية
    fulltweet = f"{zekr}\n\n#{category_hashtag}\n#اذكار"
    #نشر الذكر في تويتر
    api.update_status(fulltweet)
    print(f"تم التغريد\nالتغريدة : {fulltweet}\nانتظار نصف ساعة...")
   
#تكرار مع انتظار ١٨٠٠ ثانية يساوي نصف ساعة
while True:
    main()
    time.sleep(1800)
