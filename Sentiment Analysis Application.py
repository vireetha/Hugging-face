import requests
api_url = "https://api-inference.huggingface.co/models/Pradyumnan/sentiment-analysis"
headers = {"Authorization": f"Bearer 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"}
text = "I love this movie! It was fantastic."
response = requests.post(api_url, headers=headers, json={"inputs": text})
if response.status_code == 200:
    result = response.json()
    print(f"Sentiment: {result[0]['label']}, Score: {result[0]['score']}")
    print(f"Error:{response.status_code}")