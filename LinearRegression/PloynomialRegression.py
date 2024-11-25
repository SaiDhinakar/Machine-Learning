import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# Create sample dataset for multiple regression
np.random.seed(42)
n_samples = 100

# Generate features
X1 = np.random.uniform(0, 10, n_samples)
X2 = np.random.uniform(0, 10, n_samples)
# Create target with some noise
y = 2*X1 + 3*X2 + 5 + np.random.normal(0, 1, n_samples)

# Reshape for sklearn
X_multi = np.column_stack((X1, X2))

# Split data
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
    X_multi, y, test_size=0.2, random_state=42
)

# Polynomial Regression
print("\nPolynomial Regression:")
print("-" * 30)

# Generate non-linear data
X = np.linspace(0, 10, n_samples).reshape(-1, 1)
y = 3*X**2 + 2*X + 1 + np.random.normal(0, 10, (n_samples, 1))

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create polynomial features (degree=2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train polynomial regression model
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)

# Make predictions
y_pred_poly = poly_reg.predict(X_test_poly)

# Print results
print(f"Intercept: {poly_reg.intercept_[0]:.2f}")
print(f"Coefficients: {poly_reg.coef_[0]}")
print(f"R² Score: {r2_score(y_test, y_pred_poly):.4f}")
print(f"MSE: {mean_squared_error(y_test, y_pred_poly):.4f}")

# Visualize polynomial regression
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Test Data')

# Sort X values for smooth curve
X_sort = np.sort(X, axis=0)
X_sort_poly = poly.transform(X_sort)
y_smooth = poly_reg.predict(X_sort_poly)

plt.plot(X_sort, y_smooth, color='red', label='Polynomial Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Polynomial Regression (Degree 2)')
plt.legend()
plt.grid(True)
plt.show()

# Example predictions
print("\nExample Predictions:")
print("-" * 30)

# Polynomial Regression prediction
new_data_poly = np.array([[5]])
new_data_poly_transformed = poly.transform(new_data_poly)
pred_poly = poly_reg.predict(new_data_poly_transformed)
print(f"Polynomial Regression Prediction for X=5: {pred_poly[0][0]:.2f}")