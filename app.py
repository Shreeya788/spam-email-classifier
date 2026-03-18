import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# UI
st.title("📩 Spam Email Classifier")

st.write("Enter a message to check whether it's spam or not.")

user_input = st.text_area("Message")

if st.button("Predict"):
    if user_input.strip() != "":
        # Preprocess (same as training)
        processed = user_input.lower()

        # Vectorize
        input_vec = vectorizer.transform([processed])

        # Predict
        result = model.predict(input_vec)

        # Output
        if result[0] == "spam":
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is NOT spam")
    else:
        st.warning("Please enter a message")