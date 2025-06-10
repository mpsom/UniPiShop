import uuid

from pymongo import MongoClient
from flask import request, jsonify, Response
import json

from app_api.model import server

client = MongoClient("mongodb://localhost:27017/")

db = client["MyUniPiStore"]
products = db["StoreGoods"]


# Insert product
# Δημιουργία
@server.route("/insertproduct", methods=["POST"])
def insert_product():
    # Request JSON data
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Μη σωστό περιεχόμενο json", status=500, mimetype="application/json")
    if data == None:
        return Response("Κενή φόρμα", status=500, mimetype="application/json")
    if (
            not "name" in data
            or not "category" in data
            or not "subcategory" in data
            or not "description" in data
            or not "price" in data
            or not "image" in data
    ):
        return Response(
            "Δεν παρέχονται όλες οι πληροφορίες", status=500, mimetype="application/json"
        )
# Έλεγχος για ύπαρξη προϊόντος με το δοθέν όνομα
    if products.count_documents({"name": data["name"]}) > 0:
        return Response(
            "A product with the same name already exists",
            status=200,
            mimetype="application/json",
        )
    else:
        product = {
            "_id": str(uuid.uuid4()),
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
            "Προστέθηκε στη βάση δεδομένων των προϊόντων", status=200, mimetype="application/json"
        )


# Read operations
# Συνολικός αριθμός προϊόντων
@server.route("/productsamount", methods=["GET"])
def get_products_count():
    number_of_products = products.count_documents({})
    return jsonify({"Η ποσότητα των προίόντων είναι: ": number_of_products})


# Αναζήτηση με όνομα
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

    return Response("Δε βρέθηκε προϊόν", status=500, mimetype="application/json")

# Επιστροφή όλων των προϊόντων
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

# Delete operation
# Διαγραφή προϊόντος
@server.route("/deleteproduct/<string:id>", methods=["DELETE"])
def delete_product(id):
    try:
        if id == None:
            return Response("Δεν καταχωρήθηκε προϊόν για διαγραφή", status=500, mimetype="application/json")
        else:
            res = products.find_one_and_delete({"_id": id})
        if res is not None:
            return Response("Διαγράφηκε το προϊόν", status=200, mimetype="application/json")
        else:
            return Response("Δεν υπάρχει προϊόν με αυτό το όνομα στη βάση δεδομένων", status=200, mimetype="application/json")
    except Exception as e:
        return Response(
            '{"error": "Προέκυψε σφάλμα στο server"}',
            status=500,
            mimetype="application/json")

# Update operation
# Ενημέρωση προϊόντος
@server.route("/updateproduct", methods=["PUT"])
def update_product():
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Μη σωστό περιεχόμενο json", status=500, mimetype="application/json")

    if data is None:
        return Response("Κενή φόρμα", status=500, mimetype="application/json")

    if "_id" not in data:
        return Response("Δεν παρέχεται _id προϊόντος", status=500, mimetype="application/json")

    # Έλεγχος ύπαρξης προϊόντος
    existing_product = products.find_one({"_id": data["_id"]})
    if not existing_product:
        return Response("Το προϊόν δεν βρέθηκε", status=404, mimetype="application/json")

    # Αφαίρεση
    update_data = data.copy()
    update_data.pop("_id", None)

    # Ενημερώνεις με ό,τι σου στείλει η φόρμα (χωρίς περιορισμό)
    if not update_data:
        return Response("Δεν δόθηκαν στοιχεία προς ενημέρωση", status=400, mimetype="application/json")

    result = products.update_one({"_id": data["_id"]}, {"$set": update_data})
    if result.modified_count == 0:
        return Response("Δεν έγινε καμία αλλαγή", status=200, mimetype="application/json")

    return Response("Το προϊόν ενημερώθηκε επιτυχώς", status=200, mimetype="application/json")




