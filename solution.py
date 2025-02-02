import pandas as pd
import numpy as np
import requests
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# API Endpoints
QUIZ_ENDPOINT = "https://www.jsonkeeper.com/b/LLQT"  # Fixed SSL issue
QUIZ_SUBMISSION_ENDPOINT = "https://api.jsonserve.com/rJvd7g"
HISTORICAL_QUIZ_ENDPOINT = "https://api.jsonserve.com/XgAgFJ"

# Fetch Data
quiz_data = fetch_data(QUIZ_ENDPOINT)
quiz_submission_data = fetch_data(QUIZ_SUBMISSION_ENDPOINT)
historical_quiz_data = fetch_data(HISTORICAL_QUIZ_ENDPOINT)

# Convert historical data into DataFrame
historical_df = pd.DataFrame(historical_quiz_data)

def analyze_performance(history_df):
    required_columns = {"accuracy", "score"}
    if not required_columns.issubset(history_df.columns):
        print("Warning: Missing required columns for performance analysis.")
        return None, None
    
    history_df["accuracy"] = pd.to_numeric(history_df["accuracy"].astype(str).str.replace("%", "", regex=True), errors='coerce') / 100
    history_df = history_df.dropna(subset=["accuracy", "score"])
    
    weak_topics = history_df.groupby('score')['accuracy'].mean().sort_values().head(5)
    improvement_trends = history_df.groupby('score')['score'].mean()
    
    return weak_topics, improvement_trends

def predict_rank(history_df, latest_score):
    if {"score", "rank"}.issubset(history_df.columns):
        X = history_df[['score']].values
        y = history_df['rank'].values
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        model = LinearRegression()
        model.fit(X_scaled, y)
        
        latest_score_scaled = scaler.transform([[latest_score]])
        predicted_rank = model.predict(latest_score_scaled)
        
        return int(predicted_rank[0])
    else:
        print("Warning: Missing required columns for rank prediction.")
        return None

def predict_college(rank):
    if rank is None:
        return "Insufficient data to predict college."
    if rank < 5000:
        return "AIIMS Delhi, JIPMER, CMC Vellore"
    elif rank < 20000:
        return "Top Government Medical Colleges"
    else:
        return "Private Medical Colleges"

weak_topics, improvement_trends = analyze_performance(historical_df)
if weak_topics is not None and improvement_trends is not None:
    print("Weak Topics:\n", weak_topics)
    print("Improvement Trends:\n", improvement_trends)

latest_score = quiz_submission_data.get('score', 0)
predicted_rank = predict_rank(historical_df, latest_score)
if predicted_rank is not None:
    print(f"Predicted NEET Rank: {predicted_rank}")
    print(f"Suggested College: {predict_college(predicted_rank)}")
