import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pickle
from flask import Flask, request, render_template

# Load the dataset
file_path = 'spam.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Drop unnecessary columns and rename the columns
data = data[['v1', 'v2']]
data.columns = ['label', 'text']

# Encode labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the SVM classifier
classifier = SVC(kernel='linear')
classifier.fit(X_train_vec, y_train)

# Evaluate the model
y_pred = classifier.predict(X_test_vec)
print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the trained classifier and vectorizer
with open('svm_classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)