from urllib.parse import urlencode
from time import sleep
import requests
import random
from bs4 import BeautifulSoup
from flask import jsonify, request
from app_api.model import server

@server.route("/scrapingmarketin", methods=["POST"])
def scraping_mrktin():
    name = request.get_json()
    params = {"Title": name}
    url = "https://www.market-in.gr/el-gr/ALL?" + urlencode(params)

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ]

    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': 'el-GR,el;q=0.9,en;q=0.8',
        'Referer': 'https://www.google.com/',
    }
    s = requests.Session()
    page = s.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    print(page.status_code, url)
    sleep(random.uniform(2, 5))

    # Url περιγραφής και εικόνας
    link = soup.select_one("a.product-thumb")
    if link is not None:
        img = link.find('img')
        if img is not None:
            url = link['href']
            image = img['src']
            if not image.startswith('http'):
                image = "https://www.market-in.gr" + image

        else:
            return jsonify({"message": "Δεν βρέθηκε εικόνα!"})
    else:
        return jsonify({"message": "Δεν βρέθηκε προϊόν!"})
    # Τιμή
    price = soup.select_one("div.new-price-wrapper")
    if price is not None:
        price_span = price.find("span", class_="new-price")
        if price_span:
            price = price_span.get_text(strip=True)

    # Περιγραφή
    page = s.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    des = soup.find("div", class_="product-description-short")
    if des is not None:
        h4 = des.find("h4")
        if h4 and h4.next_sibling:
            description = h4.next_sibling.strip()
        else:
            description = des.get_text(separator=" ", strip=True)
    else:
        description = "Δεν βρέθηκε περιγραφή."
    sleep(random.uniform(2, 5))

    print(f"Product: {url} \n Image: {image}\n Price: {price} \n Description: {description}")
    return jsonify({"Εικόνα": image,
                    "Τιμή":price,
                    "Περιγραφή": description})
