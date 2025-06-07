from urllib import response
from urllib.parse import urlencode as urlencode
from time import sleep
import requests
import random
from bs4 import BeautifulSoup

# def scraping_xal(name):
name = "ΦΑΡΜΑ ΑΝΤΩΝΑΚΗ Καπνιστή Μπριζόλα"
params = {"sq": name}
url = "https://xalkiadakis.gr/search?" + urlencode(params)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'el-GR,el;q=0.9,en;q=0.8',
    'Referer': 'https://www.google.com/',
}
s = requests.Session()
page = s.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
print(page.status_code,url, page.content)
sleep(random.uniform(2, 5))

# Url περιγραφής και εικόνας
link = soup.select_one("a", class_="product-image-link")
if link is not None:
    img = link.find('img', class_='product-image')
    if img is not None:
        url = link['href']
        image = img['src']
        print("Πρώτο product url:", url)
        print("Πρώτη εικόνα:", image)
    else:
        print("Δεν βρέθηκε εικόνα!")
else:
    print("Δεν βρέθηκε προϊόν!")




# Τιμή
price = soup.select_one("div", class_="price-margin")
if price is not None:
    price_div = price.find("div", class_="price")
    if price_div and price_div.contents:
        price = price_div.find(string=True, recursive=False).strip()

# Περιγραφή
page = s.get(url,headers=headers )
soup = BeautifulSoup(page.content, "html.parser")
description = soup.select("p", class_="single-product-text")

print(f"Product: {url} \n Image: {image}\n Price: {price} \n Description: {description}")


sleep(random.uniform(2, 5))