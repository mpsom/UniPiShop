from app_api.model import server
import app_api.routes.db_products
import app_api.routes.gen_ai
import app_api.routes.purchases
import app_api.routes.scraping_marktin
import app_api.routes.scraping_bazaar
import app_api.routes.cart

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5050)
