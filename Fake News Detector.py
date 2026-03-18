import streamlit as st
import pickle
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# -------------------------------
# Dummy Training Data (Replace later with real dataset)
# -------------------------------
texts = [
    "Breaking news: government announces new policy",
    "Scientists discovered a new species in Amazon",
    "Click here to win money now!!!",
    "You won lottery claim now",
    "Fake news spreading about celebrities death",
    "Official report released by government"
]

labels = [1, 1, 0, 0, 0, 1]  # 1 = Real, 0 = Fake

# -------------------------------
# Train Model
# -------------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, labels)

# -------------------------------
# Suspicious Words List
# -------------------------------
suspicious_words = [
    "win", "lottery", "click", "urgent", "free", "money",
    "claim", "now", "shocking", "breaking", "!!!"
]

# -------------------------------
# Function to Highlight Words
# -------------------------------
def highlight_text(text):
    words = text.split()
    highlighted = ""

    for word in words:
        if word.lower() in suspicious_words:
            highlighted += f"**:red[{word}]** "
        else:
            highlighted += word + " "
    return highlighted

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detector")
st.write("Enter a news headline or content to check if it's Fake or Real.")

user_input = st.text_area("✍️ Enter News Text")

if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Transform input
        input_vector = vectorizer.transform([user_input])

        # Prediction
        prediction = model.predict(input_vector)[0]
        probability = model.predict_proba(input_vector)[0]

        # Output
        if prediction == 1:
            st.success("✅ This looks like REAL news")
            st.write(f"Confidence: {round(max(probability)*100, 2)}%")
        else:
            st.error("🚨 This looks like FAKE news")
            st.write(f"Confidence: {round(max(probability)*100, 2)}%")
        st.subheader("🔍 Suspicious Words Highlighted")
        highlighted_text = highlight_text(user_input)
        st.markdown(highlighted_text)
        #to run this code, save it as Fake News Detector.py and run it using streamlit run Fake News Detector.py in terminal.