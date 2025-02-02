# P.S 2: Email Phishing Detector

## Overview
The Email Phishing Detector is a machine learning-based application that identifies phishing emails using Natural Language Processing (NLP) and classification models. The project is implemented in Python, trained using scikit-learn, and deployed as a web application using Flask.

## Features
- **Email Analysis**: Detects whether the email is phishing email or not.
- **Dataset-based Analysis**: Allows users to analyze emails in bulk using datasets.
- **Web-based Interface**: User-friendly UI for easy interaction.

## Technology Stack
- **Programming Language**: Python
- **Machine Learning Library**: scikit-learn
- **Framework**: Flask (for web deployment)
- **Frontend**: HTML, CSS, JS (stored in `templates` and `static` folders)
- **Dataset Handling**: NLP techniques for text classification

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Flask
- scikit-learn
- Any required dependencies from `requirements.txt`

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/prakashdebroy/email_phising_detector.git
   cd email-phishing-detector
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Train the ML model (pre-trained model also included):
   ```sh
   python train_model.py
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
6. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
- Upload an email or input email body for analysis.
- The model will classify the email as **Phishing** or **Legitimate**.
- to train the model 

## Team DeauthDefy
##### - Prakash Debroy
##### - Anshul Rajkumar
##### - Priyanshu Sahoo