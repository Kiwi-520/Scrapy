# requests
import requests
import time

url = "https://news.ycombinator.com/"

proxy_ip = "132.145.93.138:1080"

headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    'accept-encoding' : 'gzip, deflate, br, zstd',
    'accept-language' : 'en-US,en;q=0.9,en-IN;q=0.8',
    'connection' : 'keep-alive'
}

proxies = {
    "http" :f'http://{proxy_ip}',
    "https" :f'http://{proxy_ip}',

}

session = requests.Session()
session.headers.update(headers)
session.proxies.update(proxies)


time.sleep(2)
response = session.get(url, timeout = 10)

print(response.status_code)

with open('file2.html' ,'w') as f:
    f.write(response.text) # stores the html as string
