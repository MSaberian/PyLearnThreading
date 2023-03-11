from threading import Thread
import time
import requests

start_time = time.time()
def scrapper(url):
    result = requests.get(url)
    # print(result.text)

urls = ['https://google.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://sajjadaemmi.ir',
        'http://w3schools.com',
        'https://yahoo.com',
        'https://bing.com']

Threads = []
for url in urls:
    new_thread = Thread(target=scrapper, args=[url])
    Threads.append(new_thread)
    # scrapper(url)

for t in Threads:
    t.start()

for t in Threads:
    t.join()

end_time = time.time()

print(end_time-start_time)