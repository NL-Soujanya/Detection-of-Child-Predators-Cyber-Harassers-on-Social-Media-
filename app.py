
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained classifier and vectorizer
with open('svm_classifier.pkl', 'rb') as f:
    classifier = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_spam():
    message = request.form['message']
    message_vec = vectorizer.transform([message])
    prediction = classifier.predict(message_vec)[0]
    result = 'spam' if prediction == 1 else 'Not spam'
    
    return render_template('results.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)