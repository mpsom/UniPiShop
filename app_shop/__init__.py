from flask import Flask

server = Flask(__name__)

from app_shop.routes import rts_products