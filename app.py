from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model_utils import SentimentModel

app = Flask(__name__)
CORS(app)
model = SentimentModel()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    label, score = model.predict(text)
    return jsonify({"label": label, "score": round(score, 2)})

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    text = data.get("text")
    label = data.get("label")
    model.update_model(text, label)
    return jsonify({"message": "Model updated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
