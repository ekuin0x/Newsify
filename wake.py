import schedule as sc
import requests
import time

def wake() : 
    

wake()
sc.every(10).minutes.do(wake)
while True:
    sc.run_pending()
    time.sleep(1)



