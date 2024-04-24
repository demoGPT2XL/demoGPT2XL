from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/migueldeguzmandev/GPT2XL_RLLMv18-3"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def home():
    output = None
    if request.method == 'POST':
        input_text = request.form['input_text']
        output = query({"inputs": input_text})
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
