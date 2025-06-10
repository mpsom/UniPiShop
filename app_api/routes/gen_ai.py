import requests #Χρήση για αιτήματα (requests) προς άλλους servers
import json

from flask import jsonify, request # αντικείμενο της Flask για τον server για διάβασμα τι έστειλε κάποιος client

from app_api.model import server

# Unused AI-API keys

# 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
# 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


GROQ_API_KEY = "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"
GROQ_API_KEY = "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"

# Διαμόρφωση συνάρτησης για κλήση του AI API με το body που ορίζει
def groq(prompt):
    post_url = "https://api.groq.com/openai/v1/chat/completions"
    post_data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "temperature": 1,
        "max_completion_tokens": 1024,
        "top_p": 1,
        "stream": False,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer " + GROQ_API_KEY,
    }

    try:
        response_post = requests.post(post_url, json=post_data, headers=headers)
        data = response_post.json()
        print("🟡 AI response:", data)

        # Αν υπάρχει "choices", επιστρέφουμε το content
        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]

        # Αν υπάρχει σφάλμα
        if "error" in data:
            return f"❌ AI Error: {data['error'].get('message', 'Άγνωστο σφάλμα')}"

        return "❌ Δεν επιστράφηκε απάντηση από το AI."

    except Exception as e:
        print("🔴 Σφάλμα σύνδεσης ή αποκωδικοποίησης:", e)
        return "❌ Πρόβλημα επικοινωνίας με το AI σύστημα."

# Κλήση από την frontend εφαρμογή με για το τελικό καλάθι και POST AI prompt και επιστροφή απάντησης
@server.route("/finalcart", methods=["POST"])
def get_cart():
    user_cart = request.get_json()

    if not isinstance(user_cart, list):
        return jsonify({"error": "Bad format, expected a list of products"}), 400

    product_names = ", ".join([item.get("name", "") for item in user_cart])

    q1 = f"Δώσε μου συνταγή για τα προϊόντα: {product_names}"
    q2 = f"Βαθμολόγησε διατροφικά τις επιλογές μου: {product_names}"

    a1 = groq(q1)
    a2 = groq(q2)

    return jsonify({"recipe": a1, "nutrition": a2}), 200






