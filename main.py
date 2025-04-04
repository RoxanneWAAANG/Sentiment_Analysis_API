import numpy as np
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pickle
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn


dataset_url = 'https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv'
df = pd.read_csv(dataset_url)

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W', ' ', text)  # Remove all special characters
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
    return text

df['tweet'] = df['tweet'].apply(preprocess_text)

X = df['tweet']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sentiment_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english')),
    ('classifier', MultinomialNB())
])

sentiment_pipeline.fit(X_train, y_train)

y_pred = sentiment_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

model_filename = 'sentiment_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(sentiment_pipeline, file)

print("Model saved successfully!")

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(request: SentimentRequest):
    processed_text = preprocess_text(request.text)
    prediction = model.predict([processed_text])
    sentiment = "Positive" if prediction[0] == 1 else "Negative"
    return {"sentiment": sentiment}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
