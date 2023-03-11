from threading import Thread
from time import time
import requests

def download(url, name):
    result = requests.get(url)

    f = open(name, 'wb')
    f.write(result.content)
    f.close()

urls = [
    ['https://cdn.dribbble.com/users/4610250/screenshots/15075736/media/1d96c3e223eef9b128beae05a6066074.png?compress=1&resize=1000x750&vertical=top','output/soduco.png'],
    ['https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Content-Card-Test-Surface-Laptop-5-Sandstone-02?wid=517&hei=293&fit=crop','output/micor.png'],
    ['https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/gldn-XSS-CP-Xbox-Series-S?wid=517&hei=293&fit=crop','output/asdsa.png'],
    ['https://dkstatics-public.digikala.com/digikala-adservice-banners/1dadfeb9b95e66e1f13deef93fa119d539ff52f2_1678117702.gif?x-oss-process=image','output/fdsf.png']
]

start_time = time()

threads = []
for url, name in urls:
    threads.append(Thread(target=download, args=[url, name]))
    # download(url, name)

for t in threads:
    t.start()

# for t in threads:
#     t.join()

threads[1].join()
threads[3].join()

end_time = time()
print(end_time-start_time)