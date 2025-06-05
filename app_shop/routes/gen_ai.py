import requests
import json

from flask import jsonify, request

from app_shop.model import server

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

    #print("\nPOST Request Status Code:", response_post.status_code)
    #print("POST Request JSON Response:")
    answer = response_post.json()
    print(answer)
    return answer["choices"][0]["message"]["content"]


@server.route("/finalcart", methods=["POST"])
def get_cart():
    global user_cart
    user_cart=request.get_json()
    #print(user_cart)
    product_names=[item ["name"]for item in user_cart]
    print(product_names)
    q2= "δωσε μου συνταγη για τα προϊόντα" + ":".join(product_names)
    q3 = "Βαθμολόγησε διατροφικά τις επιλογες μου" + ":".join(product_names)
    print(q3)
    a2 = groq(q2)
    a3 = groq(q3)
    print(a2,a3)
    # print(
    #     f"Q2: {q2}, \n=============================================================\n Q3: {q3}")
    # print(
    #     f"A2: {a2}, \n=============================================================\n A3: {a3}")
    return "Cart successfully posted", 200







# @server.route("/aiprompt", methods=["GET"])
# def aiprompt():
#     q = "Πότε θα πάρω πτυχίο; Απάντησε με ένα αστείο τρόπο."
#     a = groq(q)
#     return jsonify({
#         "question": q,
#         "answer": a
#     })
