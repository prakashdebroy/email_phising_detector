import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load the trained model and vectorizer
model = joblib.load('models/phishing_detector_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Function to check if an email is phishing or not
def check_email(email_body):
    email_vectorized = vectorizer.transform([email_body])
    prediction = model.predict(email_vectorized)
    return prediction[0]  # Model's prediction is already in the required format (e.g., 'phishing' or 'not phishing')

# Load the CSV file with emails to check
def check_emails_in_csv(csv_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Make sure there is a 'body' column in the dataset
        if 'body' not in df.columns:
            print("The dataset does not contain 'body' column.")
            return
        
        # Apply the check_email function to each email body in the dataframe
        df['prediction'] = df['body'].apply(check_email)
        
        # Print or save the results
        print(df[['sender', 'body', 'prediction']])
        output_path = 'checked/checked_emails.csv'
        df.to_csv(output_path, index=False)
        print(f"\nResults saved to {output_path}")
        
        # Count the number of phishing emails
        phishing_count = (df['prediction'] == 1).sum()
        print(f"\nTotal number of phishing emails found: {phishing_count}\n")
    except Exception as e:
        print(f"Error processing the file: {e}")

# Example usage
if __name__ == '__main__':
    csv_file = input("Enter the path to the email CSV file: ")
    check_emails_in_csv(csv_file)
