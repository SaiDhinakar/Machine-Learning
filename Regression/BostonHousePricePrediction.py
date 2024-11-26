from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Load the Boston housing dataset
data = pd.read_csv("../Datasets/BostonHousing.csv")

# Separate the features (X) and target (y)
X = data.drop(columns=['medv'])  # Features (all columns except 'medv')
y = data['medv']  # Target: MEDV (median value of homes)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Example: New data points with same features as in the dataset
# Here, we are making up some new values for the features
new_data = [
    [0.1, 0, 7, 0, 0.5, 6, 30, 4, 1, 250, 15, 376, 5],   # New house with example feature values
    [0.2, 0, 6, 1, 0.4, 5, 25, 4.5, 2, 400, 14, 300, 8]    # Another new house example
]

# Convert new_data to a DataFrame with the same column names as the training data (features only)
new_data_df = pd.DataFrame(new_data, columns=X.columns)

# Predict using the trained model
predictions = model.predict(new_data_df)

# Output the predictions
for i, pred in enumerate(predictions):
    print(f"Prediction for new house {i+1}: ${pred * 1000:.2f}")  # multiply by 1000 to get the actual price in dollars
