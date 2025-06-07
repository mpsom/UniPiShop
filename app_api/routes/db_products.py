from pymongo import MongoClient
from flask import request, jsonify, Response
import json

from app_api.model import server

client = MongoClient("mongodb://localhost:27017/")

db = client["MyUniPiStore"]
products = db["StoreGoods"]


# Insert product
# Create Operation
@server.route("/insertproduct", methods=["POST"])
def insert_product():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content", status=500, mimetype="application/json")
    if data == None:
        return Response("bad request", status=500, mimetype="application/json")
    if (
            not "name" in data
            or not "category" in data
            or not "subcategory" in data
            or not "description" in data
            or not "price" in data
            or not "image" in data
    ):
        return Response(
            "Not all information included", status=500, mimetype="application/json"
        )

    if products.count_documents({"name": data["name"]}) > 0:
        return Response(
            "A product with the same name already exists",
            status=200,
            mimetype="application/json",
        )
    else:
        product = {
            "name": data["name"],
            "category": data["category"],
            "subcategory": data["subcategory"],
            "description": data["description"],
            "price": data["price"],
            "image": data["image"]
        }

        # Add product to the "products" database
        products.insert_one(product)
        return Response(
            "It was added to the product database", status=200, mimetype="application/json"
        )


# Read operations
# Get all products
@server.route("/productsamount", methods=["GET"])
def get_products_count():
    number_of_products = products.count_documents({})
    return jsonify({"Number of products": number_of_products})


# Find product by name
@server.route("/getproduct/<string:name>", methods=["GET"])
def get_product_by_name(name):
    if name == None:
        return Response("Bad request", status=500, mimetype="application/json")

    filtered_products = [
        {
            "_id": str(p["_id"]),
            "name": p["name"],
            "category": p["category"],
            "subcategory": p["subcategory"],
            "description": p["description"],
            "price": p["price"],
            "image": p["image"],
        }

        for p in products if name.lower() in p["name"].lower()
    ]
    if filtered_products:
        return jsonify(filtered_products)

    return Response("No product found", status=500, mimetype="application/json")


# Επιστροφη ολων των προιοντων
@server.route("/getallproducts", methods=["GET"])
def get_all_products():
    all_products = []
    for product in products.find():
        all_products.append({
            "_id": str(product["_id"]),
            "name": product["name"],
            "category": product["category"],
            "subcategory": product["subcategory"],
            "description": product["description"],
            "price": product["price"],
            "image": product["image"]
        })
    return jsonify(all_products)

