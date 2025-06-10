import requests
import json
from flask import jsonify, request
from app_api.model import server

# Κλειδί GROQ API
GROQ_API_KEY = "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"

# Συνάρτηση που καλεί το AI API με το κατάλληλο prompt
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
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }

    try:
        response_post = requests.post(post_url, json=post_data, headers=headers)
        data = response_post.json()

        print("🟡 AI response:", data)

        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]

        if "error" in data:
            return f"❌ AI Error: {data['error'].get('message', 'Άγνωστο σφάλμα')}"

        return "❌ Δεν επιστράφηκε απάντηση από το AI."

    except Exception as e:
        print("🔴 Σφάλμα σύνδεσης ή αποκωδικοποίησης:", e)
        return "❌ Πρόβλημα επικοινωνίας με το AI σύστημα."

# Route για το τελικό καλάθι προϊόντων
@server.route("/finalcart", methods=["POST"])
def get_cart_response():
    user_cart = request.get_json()

    if not isinstance(user_cart, list):
        return jsonify({"error": "Bad format, expected a list of products"}), 400

    product_names = ", ".join([item.get("name", "") for item in user_cart])

    prompt_recipe = f"Δώσε μου συνταγή για τα προϊόντα: {product_names}"
    prompt_nutrition = f"Βαθμολόγησε διατροφικά τις επιλογές μου: {product_names}"

    response_recipe = groq(prompt_recipe)
    response_nutrition = groq(prompt_nutrition)

    return jsonify({
        "Συνταγή": response_recipe,
        "Αξιολόγηση": response_nutrition
    }), 200
