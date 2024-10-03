from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Label mapping (you can customize this based on the model's output)
label_mapping = {
    "LABEL_0": "Negative",
    "LABEL_1": "Positive"
}

# Serve the HTML file for the root route
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to analyze sentiment
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')
    aspect = data.get('aspect')

    # Log received data
    print(f"Received text: {text}, aspect: {aspect}")

    # Load the sentiment model
    model = pipeline("text-classification", model="srimeenakshiks/aspect-based-sentiment-analyzer-using-bert")

    # Perform sentiment analysis
    results = model(f"{aspect}: {text}")
    sentiment_label = results[0]['label']  # Extract the sentiment label

    # Map the raw label to a human-readable sentiment
    sentiment = label_mapping.get(sentiment_label, "Unknown")

    # Log the sentiment result
    print(f"Sentiment: {sentiment}")

    return jsonify({
        'aspect': aspect,
        'sentiment': sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
