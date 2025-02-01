from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('models/phishing_detector_model_ling.pkl')
vectorizer = joblib.load('models/vectorizer_ling.pkl')

# Function to check if an email is phishing or not
def check_email(email_body):
    email_vectorized = vectorizer.transform([email_body])
    prediction = model.predict(email_vectorized)
    return prediction[0]  # Model's prediction is already in the required format (e.g., 'phishing' or 'not phishing')

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to process the email input from the user
@app.route('/check_email', methods=['POST'])
def check_email_route():
    try:
        email_body = request.form['email_body']
        print("Received email body:", email_body)  # Debugging output to check what we received

        # Get the result from the model
        result = check_email(email_body)
        
        if result == 1:
            message = "This is a phishing email."
        else:
            message = "This is not a phishing email."
        
        return jsonify({'result': message})
    except Exception as e:
        return jsonify({'result': f"Error: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
