from app_shop.model import server
import app_shop.routes.mongo_products as mongo_products

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5000)
