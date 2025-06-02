from pymongo import MongoClient
import uuid

client = MongoClient("mongodb://localhost:27017/")
db = client["MyUniPiStore"]
products = db["StoreGoods"]

products_to_insert = [
    {
        "_id": str(uuid.uuid4()),
        "name": "MELISSA Μακαρόνια Νο6 500g",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Ζυμαρικά",
        "description": "Ζυμαρικά από 100% ελληνικό σιμιγδάλι σκληρού σιταριού.",
        "price": 0.64,
        "image": "/static/images/products/melissa_spaghetti.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "Παπαδοπούλου Digestive Μπισκότα Vegan ",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Μπισκότα, Σοκολάτες & Ζαχαρώδη",
        "description": "Μπισκότα με αλεύρι ολικής άλεσης.",
        "price": 2.15,
        "image": "/static/images/products/digestive.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "CRUNCH Σοκολάτα Γάλακτος ",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Σοκολάτες",
        "description": "Σοκολάτα γάλακτος με τραγανούς κόκκους δημητριακών. Χωρίς γλουτένη.",
        "price": 2.15,
        "image": "/static/images/products/crunch.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "ΑΛΛΑΤΙΝΗ Αλεύρι για Όλες τις Χρήσεις",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Αλεύρι & Σιμιγδάλι",
        "description": "Αλεύρι για όλες τις χρήσεις.",
        "price": 1.18,
        "image": "/static/images/products/alevri.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "BEN'S ORIGINAL Ρύζι Basmati",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Ρύζι",
        "description": "Αφράτοι κόκκοι ρυζιού σε μαγειρικό σακουλάκι για ευκολία στο μαγείρεμα με διακριτική γεύση και φυσικό λευκό χρώμα. Χωρίς γλουτένη. Κατάλληλο για χορτοφάγους.",
        "price": 4.00,
        "image": "/static/images/products/bens_rice.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "3 ΑΛΦΑ Ρύζι Basmati Ινδίας",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Ρύζι",
        "description": "Ρύζι Μπασμάτι αρωματικό ρύζι για κάθε χρήση, με ιδιαίτερη γεύση. Χρησιμοποιείται για πιλάφι και για εξωτικές συνταγές.",
        "price": 3.30,
        "image": "/static/images/products/3alfa_basmati.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "DIMFIL Bio Farma Κάσιους Ωμό Βιολογικό Χωρίς αλάτι",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Ξηροί καρποί & Σνακ",
        "description": "Αρίστης ποιότητας κάσιους άψητα βιολογικής καλλιέργειας με υπέροχη γεύση.",
        "price": 4.96,
        "image": "/static/images/products/biofarma_kasious.jpg"
    },
    {
        "_id": str(uuid.uuid4()),
        "name": "LAY'S Στο Φούρνο Πατατάκια με Αλάτι",
        "category": "Τρόφιμα παντοπωλείου",
        "subcategory": "Πατατάκια, Γαριδάκια & άλλα Σνακ",
        "description": "Σνακ από πατάτα με αλάτι.",
        "price": 1.50,
        "image": "/static/images/products/lays.jpg"
    }

]

# Bulk insert
result = products.insert_many(products_to_insert)

print(f"Inserted {len(result.inserted_ids)} products.")
