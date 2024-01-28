# Crop-Recommendation-System-App

## Introduction
This project presents a machine learning system designed to predict suitable crop types for specific environmental and soil conditions. Leveraging a Random Forest classifier, the system analyzes factors such as temperature, humidity, pH, rainfall, and soil nutrients (N, P, K) to provide crop recommendations, aiding farmers in making informed decisions.

## Technologies Used
- **Python**: For all data analysis and model development.
- **Pandas & NumPy**: For data handling and numerical computations.
- **Scikit-learn**: To implement the Random Forest algorithm and model evaluation.
- **Matplotlib & Seaborn**: For visualizing data and model performance.
- **Streamlit**: To build and deploy an interactive web application for the model.

## Features and Dataset
The dataset includes key environmental parameters and soil properties. Essential features are temperature, humidity, pH, rainfall, N, P, and K. Data preprocessing involved cleaning, normalization, and handling missing values to optimize the dataset for the machine learning model.

## Model Development and Results
The project utilized a Random Forest classifier, chosen for its effectiveness in handling complex datasets. The model achieved an accuracy of approximately 92.9%, with significant precision in predicting suitable crops. Key steps in the model's development included hyperparameter tuning and feature importance analysis.

<img width="337" alt="image" src="https://github.com/varun-crypto/Crop-Recommendation-System-App/assets/69026838/4b935c56-f75a-4d0e-868f-a9ff9cc7fb00">
<img width="336" alt="image" src="https://github.com/varun-crypto/Crop-Recommendation-System-App/assets/69026838/d7ac6909-02d7-445e-921d-c875725a7a1e">

![image](https://github.com/varun-crypto/Crop-Recommendation-System-App/assets/69026838/83ff2fb2-2316-4340-85f7-50d087774dd3)

## Web Application
The project features a Streamlit-based web application, enabling users to input environmental data and receive crop predictions in real-time. The app's user-friendly interface allows for easy interaction and demonstrates the model's practical application.

<img width="721" alt="image" src="https://github.com/varun-crypto/Crop-Recommendation-System-App/assets/69026838/44df5f78-6dc5-4734-a594-022546d1cd53">

## Challenges and Learnings
The project highlighted the importance of thorough data preprocessing and the impact of feature selection on model performance. Balancing technical model development with creating a user-centric web application was a valuable learning experience.

## Future Scope
Future improvements could include the integration of real-time environmental data sources and expansion of the model to include a broader range of crops and geographies.


