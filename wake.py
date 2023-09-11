import schedule as sc
import requests
import time

def wake() : 
    res1 = requests.get("https://newzone.onrender.com")
    res2 = requests.get("https://convertly.onrender.com")
    print(res1)
    print(res2)


wake()
sc.every(10).minutes.do(wake)
while True:
    sc.run_pending()
    time.sleep(1)



