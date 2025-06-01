from typing import List
from app_shop.model.products import Products


class Repository:
    def __init__(self) -> None:
        self._add_some_products()

    def _add_some_products(self):
        self.products: List[Products] = [
            Products(
                category="Προϊόντα ψυγειου",
                subcategory="Φρουτα και λαχανικά"
                name="Μήλα",
                price=2.05,
                description="Ελληνικά μήλα στάρκινγκ από τη Καστοριά.",
                image="C:/Users/psoma/Desktop/UniPiShop/static",
            ),
            Products(
                category="Γαλακτοκομικά και ειδη ψυγείου",
            
                name="Τυρί Τρικαλινό Ελαφρύ Φέτες",
                price=3.44,
                description="""Ελαφρύ τυρί Τρικαλινό, 4μηνης ωρίμανσης, με μόνο 10% λιπαρά. 
                                Ιδανικό για να το απολαύσετε σκέτο ή να δημιουργήσετε ελαφριές συνταγές.""",
                image="C:/Users/psoma/Desktop/UniPiShop/static",
            ),
            Products(
                category="Είδη προσωπικής περιποίησης",
                name="AIM | HERBAL | Οδοντόκρεμα Family Protection Herbal 75ml",
                description="""Active Fluoride & Ασβέστιο.Φόρμουλα που βοηθά στην ενδυνάμωση των δοντιών επανορθώνοντας ακόμα και τις μικρές αόρατες ενδείξεις τερηδόνας που προκαλούνται
                                από κρυμμένα οξέα σακχάρων** πριν μετατραπούν σε τερηδόνα με αποτέλεσμα 10x πιο δυνατά δόντια.""",
                image="C:/Users/psoma/Desktop/UniPiShop/static",
                price=1.26,
            ),
        ]

    # το παρακάτω ειναι  list comprehension, συνοπτικός τρόπος να δημιουργίας λίστων στην Python. [<έκφραση> for <μεταβλητή> in <λίστα> if <συνθήκη>]
    def _find_product_by_id(self, id: str) -> Products | None:
        products = [product for product in self.products if product.id == id]
        if len(products) == 0:
            return None
        return products[0]
        # Γράφεται και έτσι
        #    products = []
        #    for product in self.products:
        #      if product.id == id:
        #      products.append(product)"""

    def add_product(self, product: Products) -> None:
        self.products.append(product)

    # Το lambda δημιουργεί ανώνυμες συναρτήσεις — δηλαδή μικρές συναρτήσεις χωρίς όνομα που χρησιμοποιούνται "στο πόδι. Η map() εφαρμόζει μια συνάρτηση σε κάθε στοιχείο μιας λίστας (ή οποιαδήποτε επαναληψιμου στοιχείου)
    def get_product(self) -> list[Products]:
        return list(map(lambda x: x.to_dict(), self.products))

    def get_product_by_id(self, id: str) -> Products | None:
        product = self._find_product_by_id(id)
        if product is not None:
            return product
        return None

    def update_product(self, id: str, data) -> bool:
        product = self._find_product_by_id(id)
        if product is not None:
            product.from_dict(data)
            return True
        return False

    def delete_product(self, id: str) -> bool:
        product = self._find_product_by_id(id)
        if product is not None:
            self.products.remove(product)
            return True
        return False
