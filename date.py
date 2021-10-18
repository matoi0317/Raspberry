import datetime

dt_now = datetime.datetime.now()
datetime_web = dt_now.strftime("%Y年%m月%d日%H時%M分%S秒")
print(datetime_web)