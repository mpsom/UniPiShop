from flask import request, jsonify, Response
import json
import requests
from bs4 import BeautifulSoup
from app_api.model import server
from urllib.parse import urlencode as urlencode

@server.route("/scrapingxal", methods=["POST"])
def scraping_xal():
    name=request.get_json()
    params={"sq":request.get_json()}
    url="https://xalkiadakis.gr/search?"+ urlencode(params)
    print(name, url)
    return jsonify({"name":name, "url":url})

