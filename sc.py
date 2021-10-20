import schedule
import time
def job():
    print("aaa")

schedule.every().day.at("17:39").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)