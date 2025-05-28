from flask import request
from app_shop import server
from app_shop.model.products import Products
from app_shop.repository import Repository
import jwt
import datetime

db=Repository()


@server.route("/products", methods=["GET"])
def products():
    id = request.args.get("id")
    if id is not None:
        products=db.get_product_by_id(id)
        return (products.to_dict(),200) if products else ("Product not found",404)
    else:
        products=db.get_product()
        return products,200
    
@server.route("/products", methods=["POST"])
def product():
    data=request.get_json()
    if data is None:
        return "Missing paraments"
    if not data.get("name") or not data.get("price") or not data.get("category") or not data.get("description") or not data.get("image"):
        return "Missing paraments", 400
    product= Products(data.get("name"), data.get("price"), data.get("category"), data.get("description"),  data.get("image") )
    db.add_product(product)
    return "CREATED", 201


@server.route("/products/<id>", methods=["DELETE"])
def delete_product(id):
    deleted=db.delete_product(id)
    return("OK", 200) if deleted else ("Product not found", 404)

@server.route("products/<id>", methods=["PUT"])
def update_product(id):
    data=request.get_json()