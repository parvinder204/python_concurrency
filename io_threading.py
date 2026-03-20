import threading
import requests
import time
import certifi

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
]

session = requests.Session()

def fetch(url):
    try:
        r = session.get(url, verify=certifi.where(), timeout=5)
        print(url, r.status_code)
    except Exception as e:
        print(url, "ERROR:", e)

start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Time:", time.time() - start)