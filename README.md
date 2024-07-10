Detection of Child Predators & Cyber Harassers on Social Media

Project Overview:
The Detection of Child Predators & Cyber Harassers on Social Media project aims to enhance online safety by identifying harmful or suspicious messages. This system leverages machine learning techniques to analyze messages and determine whether they are potentially dangerous or fake, thus protecting users from cyber predators and harassment.

Features:

Message Analysis: Users can input a message, and the system will analyze it to determine if it is suspicious or fake.
Real-Time Detection: The system provides immediate feedback on the nature of the message, helping users to quickly identify potential threats.
Machine Learning Model: Utilizes a pre-trained machine learning model to classify messages based on their content.
Usage:
Once the application is running, users can input a message into the system. The application will then process the message and display whether it is considered fake or harmful.

User:
Enter the message to be analyzed.
Receive an immediate response indicating whether the message is suspicious or safe.

System Requirements:
Operating System: Windows, macOS, or Linux
Browser: Latest version of Google Chrome, Mozilla Firefox, or Microsoft Edge
Python Environment: Python 3.x with necessary libraries (Flask, Pickle, Scikit-learn, etc.)

Implementation:
Frontend:
index.html: The main page where users can input messages for analysis.

Backend:
app.py: Flask application to handle user inputs and interact with the machine learning model.
svm_classifier.pkl: Pre-trained Support Vector Machine (SVM) model for message classification.
vectorizer.pkl: Vectorizer for transforming text data into feature vectors.
