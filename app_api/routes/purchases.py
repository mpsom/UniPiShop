from pymongo import MongoClient
from flask import request, jsonify, Response
import json


from app_api.model import server

# Συλλογή για τις αγορές

client = MongoClient("mongodb://localhost:27017/")
db = client["MyUniPiStore"]

purchases = db["Purchases"]


# Endpoint για καταχώρηση αγοράς
@server.route("/purchase", methods=["POST"])
def submit_purchase():
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("Bad JSON content", status=400, mimetype="application/json")

    if not data or "timestamp" not in data or "items" not in data:
        return Response("Missing required fields", status=400, mimetype="application/json")

    purchases.insert_one(data)

    return Response("Purchase recorded successfully", status=200, mimetype="application/json")

# Μέθοδος GET για όλο το ιστορικό αγορών
@server.route("/purchasehistory", methods=["GET"])
def get_history():
    try:

        all_purchases = list(purchases.find({}, {"_id": 0}))

        return jsonify(all_purchases), 200
    except Exception as e:
        return jsonify({"Δεν υπάρχει ιστορικό": str(e)}), 500
