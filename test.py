from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["MyUniPiStore"]
products = db["StoreGoods"]
check = products.find_one({"image": {"$ne": None}})

for product in products.find():
    if product.get("image") is None:
        if product.get("image") == check:
            print(product["name"])
