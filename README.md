## NEET Testline Quiz Performance Analysis and Rank Prediction

 ## Overview

This project analyzes student quiz performance and predicts their NEET rank based on historical quiz data. It also provides insights into weak topics, improvement trends, and potential college predictions.

## Features

Data Fetching: Retrieves quiz data from given API endpoints.

Performance Analysis: Identifies weak topics and improvement trends.

Rank Prediction: Uses a machine learning model to estimate a student's NEET rank.

College Prediction (Bonus): Suggests potential colleges based on predicted rank.

## Data Sources

The solution fetches data from the following endpoints:

Current Quiz Data: Quiz Endpoint

Quiz Submission Data: Quiz Submission Endpoint

Historical Quiz Data: Historical Quiz Endpoint

## Technologies Used

Python

Pandas

NumPy

Requests (API fetching)

Scikit-learn (Machine Learning)

Installation & Setup

Clone the repository:

git clone https://github.com/your-repo.git

Install required dependencies:

pip install -r requirements.txt

Run the script:

python analyze_quiz.py

## How It Works

Fetch Data: Retrieves quiz and historical performance data.

Analyze Performance: Computes weak topics and improvement trends.

Predict Rank: Uses Linear Regression to estimate NEET rank.

Predict College: Suggests a college based on the rank.

## Output

The script prints the following:

Weak topics requiring improvement

Trends in student performance

Predicted NEET rank

Suggested college based on the rank

## Future Improvements

Implement a more advanced model (e.g., Random Forest, Neural Networks).

Enhance accuracy with additional features like time taken per question.

Develop a web dashboard for better data visualization.

## License

This project is open-source and available under the MIT License.
