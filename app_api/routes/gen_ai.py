import requests #Χρήση για αιτήματα (requests) προς άλλους servers
import json

from flask import jsonify, request # αντικείμενο της Flask για τον server για διάβασμα τι έστειλε κάποιος client

from app_api.model import server

# Unused AI-API keys
# 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
# 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
# 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


GROQ_API_KEY = "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"


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
    json_data = json.dumps(post_data)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }
    response_post = requests.post(post_url, data=json_data, headers=headers)

    # print("\nPOST Request Status Code:", response_post.status_code)
    # print("POST Request JSON Response:")
    answer = response_post.json()
    print(answer)
    return answer["choices"][0]["message"]["content"]


# Κλήση από την frontend εφαρμογή με για το τελικό καλάθι και POST AI prompt
@server.route("/finalcart", methods=["POST"])
def get_cart():
    user_cart = request.get_json()  # Επικοινωνία με το F-end για το τελικό καλάθι
    product_names = [item["name"] for item in user_cart] # Δημιουργία λίστας με τα ονόματα απο το λεξικό
    print(product_names)
    q1= "Δώσε μου συνταγή για τα προϊόντα: " + " ".join(product_names)
    q2 = "Βαθμολόγησε διατροφικά τις επιλογές μου: " +" ".join(product_names)
    print(q2)
    a1 = groq(q1)
    a2 = groq(q2)
    print(a1, a2)

    return jsonify({"Συνταγή": a1}, {"Αξιολόγηση": a2}), 200






