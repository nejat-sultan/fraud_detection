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
