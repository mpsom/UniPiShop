from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["MyUniPiStore"]
products = db["StoreGoods"]


products_to_insert = [
  {
    "name": "DOLE Bananas",
    "category": "Fresh Fruits & Vegetables",
    "subcategory": "Fruits",
    "description": "Bananas are rich in carbohydrates, plant fibers and trace elements, and contain vitamins (A, B6 & C), potassium, magnesium, copper and manganese.",
    "price": 1.85,
    "image": "static/images/products/bananas.jpg"
  },
  {
    "name": "Strawberries",
    "category": "Fresh Fruits & Vegetables",
    "subcategory": "Berries",
    "description": "Strawberries have many beneficial properties and are rich in vitamins (B & C), while also containing significant amounts of manganese, potassium, iron, and plant fibers.",
    "price": 3.78,
    "image": "static/images/products/straws.jpg"
  },
  {
    "name": "Watermelon",
    "category": "Fresh Fruits & Vegetables",
    "subcategory": "Melons & Watermelons",
    "description": "Watermelon is one of the most popular summer fruits. With few calories and a high water content (90%), it is ideal for hydrating the body. Rich in antioxidants, even the seeds have nutritional value.",
    "price": 0.95,
    "image": "static/images/products/watermelon.jpg"
  }
]


# Bulk insert
result = products.insert_many(products_to_insert)

print(f"Inserted {len(result.inserted_ids)} products.")