import requests
import json

from app_shop.model import server

GROQ_API_KEY = "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"


@server.route("/aiprompt", methods=["GET"])
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

    print("\nPOST Request Status Code:", response_post.status_code)
    print("POST Request JSON Response:")
    answer = response_post.json()
    print(answer)
    return answer["choices"][0]["message"]["content"]

    q = "Πότε θα πάρω πτυχίο; Απάντησε με ένα αστείο τρόπο."
    a = groq(q)
    print(f"Q: {q}")
    print(f"A: {a}")
