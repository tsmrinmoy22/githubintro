import schedule
import time

cnt=0
def job():
    global count
    cnt+=1
    print("Hello Scraper")

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    if cnt>4:
        break
