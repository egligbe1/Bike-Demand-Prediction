
# Bike Demand Prediction App | Machine Learning Project

Bicycles have been highly recommended as a means of transportation in most urban cities to control the increased environmental pollution resulting from the use of engine-powered vehicles. ]
This has led to the popularity of bike rental services nowadays.

However, operators of these bike rental services face the problem of accurately determining the number of bikes that will be in demand at any given time. At specific points in time, 
a customer may come to rent a bike, but there won't be any available at the station.
Therefore, I have developed a machine-learning prediction app that utilizes historical data on bike rentals to forecast the demand for bikes at various times of the day. 
Research has shown that weather and social conditions affect ride-sharing demand. 
Hence, the dataset used to model this prediction mainly contains weather factors such as rainfall, temperature, etc.
Link to dataset: https://shorturl.at/hqFGO

By leveraging machine learning algorithms, the app provides highly accurate predictions, enabling the operators to estimate the number of bikes that might be in demand at any given time.

Key Contributions:
- Preprocessed and performed Exploratory Data Analysis to understand the nature of demand using pandas.
- Trained and fine-tuned machine learning models to forecast bike demand accurately using Random Forest and XGBoost. XGBoost had the higher prediction accuracy (94%) and hence was used to create the prediction app.
- Developed an intuitive user interface, allowing users to input the time of the day and other factors to receive predictions on the number of bikes that might be in demand.
