import json
import random
import time
import tweepy
from config import api
from pytz import timezone
from datetime import datetime


#داله الأذكار
def load_prayers():
    with open("azkar.json", "r") as read_file:
        data = json.load(read_file)
    return data

#داله اختيار ذكر عشوائي
def select_random_prayer(data):
    #تصنيف أوقات الصباح والليل
    #بتستخدم لتحديد وقت اختيار اذكار الصباح او اذكار المساء
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
        type = "أذكار الجمعة"
    else:
        type = random.choice(['تسابيح', 'أدعية قرآنية', 'أدعية الأنبياء'])
    return random.choice(data[types[types.index(type)]])

def tweet_prayer(api, prayer):
    category = prayer["category"]
    zekr = prayer["content"]
    l = len(zekr)
    if l > 280:
        return tweet_prayer(api, select_random_prayer(load_prayers()))
    category_hashtag = category.replace(" ", "_")
    fulltweet = f"{zekr}\n\n#{category_hashtag}\n#اذكار"
    api.update_status(fulltweet)
    print(f"تم التغريد\nالتغريدة : {fulltweet}\nانتظار نصف ساعة...")

#الداله الرئيسية
def main():    
    while True:
        try:
            prayer = select_random_prayer(load_prayers())
            tweet_prayer(api, prayer)
        except Exception as err:
            print(f"Error: {err}")
        time.sleep(30 * 60)

if __name__ == "__main__":
    main()