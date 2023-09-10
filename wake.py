import schedule as sc
import requests
import time

def wake() : 
    res = requests.get("https://newzone.onrender.com")
    print(res)


sc.every(10).minutes.do(wake)
while True:
    sc.run_pending()
    time.sleep(1)



