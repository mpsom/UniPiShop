from pymongo import MongoClient
import uuid
client = MongoClient("mongodb://localhost:27017/")
db = client["MyUniPiStore"]
products = db["StoreGoods"]


products_to_insert = [
  {
    "_id": str(uuid.uuid4()),
    "name": "Watermelon",
    "category": "Fruits & vegies",
    "subcategory": "Fruits",
    "description": "asdadasdadadads",
    "price": 7.12,
    "image": "static/images/products/watermelon.jpg"
  },




]



# Bulk insert
result = products.insert_many(products_to_insert)

print(f"Inserted {len(result.inserted_ids)} products.")