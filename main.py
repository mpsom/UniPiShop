from app_shop.model import server
import app_shop.routes.db_products as mongo_products
import app_shop.routes.gen_ai as gen_ai
if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5050)
