import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Step 1: Load the dataset
csv_file = input("Enter the path to the dataset CSV file: ")
data = pd.read_csv(csv_file)

# Step 2: Data Preprocessing
# Extracting the relevant columns: 'body' and 'label'
X = data['body']
y = data['label']

# Step 3: Text Processing (Convert text to feature vectors)
# We will use CountVectorizer to convert the text data into numerical format
vectorizer = CountVectorizer(stop_words='english')

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Transform the text data into numerical vectors
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 6: Train a Naive Bayes Classifier (you can use any other classifier too)
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 7: Predict and evaluate the model
y_pred = model.predict(X_test_vec)

# Print the accuracy and classification report
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Save the model and the vectorizer
if not os.path.exists('models'):
    os.makedirs('models')

joblib.dump(model, 'models/phishing_detector_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("Model and vectorizer saved successfully.")