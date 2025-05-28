import uuid


class Products:
    def __init__(self, category, name, price, description, image):
        self.category = category
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.id = str(uuid.uuid4())

    # συγκριση τιμων των δυο αντικειμενων. Επιστρεφει true ή false
    def __eq__(self, other):
        return self.id == other.id

    # τυπωνει με f-string τη σειρα που θελουμε να εμφανιζεται.
    def __str__(self):
        return f"{self.id} - {self.name} in {self.category} with ({self.price})"

    # εμφανίζεται ένα αντικείμενο όταν το τυπώνεις για debugging ή μέσα σε λίστα ή στο terminal. πχ. [Products('abc123', 'Μήλα', '2.05', 'Ελληνικά μήλα στάρκινγκ από τη Καστοριά.', 'Φρούτα και λαχανικά', 'C:/Users/psoma...' )]
    def __repr__(self):
        return f"Products('{self.id}', '{self.name}', '{self.price}', '{self.description}', '{self.category}', '{self.image}' )"

    # Μετατρέπει το αντικείμενο σε λεξικό για χρηση: ως JSON από ένα API ,αποθηκευση σε βάση δεδομένων,jsonify() στο Flask,"flat" μορφή. Χρήσιμο γιατι .to_dict() το κάνει εύκολα serializable σε JSON
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image,
        }

    # παίρνει ένα λεξικό (dictionary) και ενημερώνει/δημιουργεί το αντικείμενο με βάση τις τιμές του λεξικού, αν δεν εχει αφήνει τις υπαρχουσες. H .get ειναι μεθοδος λεγικου αρα το data πρεπει να ειναι λεξικο
    def from_dict(self, data):
        self.id = data.get("id") if data.get("id") is not None else self.id
        self.name = data.get("name") if data.get("name") is not None else self.name
        self.description = (
            data.get("description")
            if data.get("description") is not None
            else self.description
        )
        self.image = data.get("image") if data.get("image") is not None else self.image
        self.price = data.get("price") if data.get("price") is not None else self.price
    
    def test(self,):
        return (self.name)