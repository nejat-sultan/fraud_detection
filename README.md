Detection of Fraud Cases
This project aims to detect fraudulent transactions through comprehensive data analysis, preprocessing, feature engineering, model building, training, and model explainability. The tasks are broken down into distinct phases to ensure a systematic approach.

Task 1: Data Analysis and Preprocessing

- Handling Missing Values
Impute or drop missing values to maintain data integrity.
- Data Cleaning
Remove duplicates to ensure data quality.
Correct data types for consistency.
- Exploratory Data Analysis (EDA)
Univariate Analysis: Analyzing individual feature distributions.
Bivariate Analysis: Studying the relationships between pairs of features.
- Merge Datasets for Geolocation Analysis
Convert IP addresses to integer format for analysis.
Merge Fraud_Data.csv with IpAddress_to_Country.csv to include geolocation information.
- Feature Engineering
Compute Transaction Frequency and Velocity for better fraud detection.
Create Time-Based Features such as:
hour_of_day
day_of_week
- Normalization and Scaling
Normalize and scale numerical features to ensure consistent input for machine learning models.
- Encode Categorical Features
Convert categorical features into numerical representations for model training.

Task 2: Model Building and Training

- Data Preparation
Feature and Target Separation: Separate features and the target variable for training.
Train-Test Split: Split data into training and testing sets for evaluation.
- Model Selection
Experiment with multiple models to identify the best-performing one.
- Model Training and Evaluation
Train models on both credit card and fraud data datasets.
Evaluate models to determine accuracy, precision, recall, and other metrics.
- MLOps Steps
Implement Versioning and Experiment Tracking using tools like Mlflow.
Track experiments, log parameters, metrics, and version models for reproducibility.


Task 3: Model Explainability

Using SHAP for Explainability
SHAP values provide a unified measure of feature importance, explaining the contribution of each feature to predictions.
SHAP Plots:
Summary Plot: Overview of the most important features.
Force Plot: Visualizes the contribution of features for individual predictions.
Dependence Plot: Shows the relationship between a feature and the model output.
Using LIME for Explainability
LIME explains individual predictions by approximating the model locally with an interpretable model.
LIME Plots:
Feature Importance Plot: Highlights the most influential features for specific predictions
