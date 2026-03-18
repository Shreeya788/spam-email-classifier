# 📩 Spam Email Classifier
A simple machine learning web app that classifies messages as spam or not spam using a Multinomial Naive Bayes model — built with Python and deployed on Streamlit.
🔗 Live Demo: https://spam-email-classifier-ljldkqmrghdgzjfd4t55dg.streamlit.app/

# Preview 
<img width="1153" height="574" alt="image" src="https://github.com/user-attachments/assets/7caada2a-95d3-4535-9546-27fd4f1aeef8" />

## 🛠️ Built With
- Python
- Scikit-learn — Multinomial Naive Bayes model
- Streamlit — Web app interface
- Pickle — Model serialization

🚀 How It Works

1. User enters a message in the text box
2. The message is lowercased and vectorized using a trained CountVectorizer
3. The Naive Bayes model predicts whether it's spam or not
4. Result is displayed instantly

# 📁 Project Structure
```
spam-email-classifier/
├── app.py                            # Streamlit web app
├── spam-email-classifier.ipynb       # Model training script
├── model.pkl                         # Trained Naive Bayes model
├── vectorizer.pkl                    # Fitted vectorizer
├── requirements.txt                  # Dependencies
└── README.md
```

# 🧠 Model Details

| Detail          | Value                     |
|-----------------|---------------------------|
| Algorithm       | Multinomial Naive Bayes   |
| Vectorizer      | CountVectorizer           |
| Classification  | spam / not spam           |

# ⚙️ Run Locally 

1. Clone the repo
```
git clone https://github.com/Shreeya788/spam-email-classifier.git
```
```
cd spam-email-classifier
```

2. Install dependencies
```
pip install -r requirements.txt
```
4. Run the app
```
streamlit run app.py
```
# Dataset
[SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

