from urllib.parse import urlencode
from time import sleep
import requests
import random
from bs4 import BeautifulSoup
from flask import jsonify, request

from app_api.model import server


@server.route("/scrapingbazaar", methods=["POST"])
def scraping_bazaar():
    name = request.get_json()
    params = {"route": "product/search", "search": name}
    url = "https://www.bazaar-online.gr/index.php?" + urlencode(params)

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
    container = soup.find("div", id="product-search")
    product = container.find("div", class_="product-thumb") if container else None

    if product is not None:
        image_div = product.find("div", class_="image")
        if image_div is not None:
            a = image_div.find("a")
            img = a.find("img") if a is not None else None
            if a and img is not None:
                image = img["src"]
                url = a["href"]
            else:
                image = "Δεν βρέθηκε εικόνα"
    else:
        return jsonify({"message": "Δεν βρέθηκε προϊόν!"})

    # Τιμή
    price = soup.select_one("div.price")
    if price is not None:
        price_div = price.find("div", class_="price_wrapper")
        if price_div and price_div.contents:
            price = price_div.find(string=True, recursive=False).strip()
        else:
            price = "Δε βρέθηκε τιμή"

    # Περιγραφή
    page = s.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    card_body = soup.select_one("div#collapse-custom-4 > div.card-body")
    if card_body is not None:
        h3 = card_body.find("h3")
        if h3 is not None:
            h3.extract()
        description = card_body.get_text(strip=True)
        print(description)
    else:
        description = "Δεν βρέθηκε περιγραφή"

    print(f"Product: {url} \n Image: {image}\n Price: {price} \n Description: {description}")

    sleep(random.uniform(2, 5))
    print(image, price, description,"βγαινω απο το market call")
    return jsonify({"Εικόνα": image,
                    "Τιμή": price,
                    "Περιγραφή": description})
