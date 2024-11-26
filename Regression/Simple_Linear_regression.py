import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create the dataset
# Years of experience (X) and corresponding salaries (Y)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reshaped to 2D array for scikit-learn
y = np.array([40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000])

# Step 2: Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 3: Make predictions (e.g., predicting salary for 11 years of experience)
predicted_salary = model.predict([[11]])

# Print the prediction for 11 years of experience
print(f"Predicted salary for 11 years of experience: ${predicted_salary[0]:,.2f}")

# Step 4: Plot the data points and the regression line
plt.scatter(X, y, color='blue', label='Actual Data')  # Plot the actual data points
plt.plot(X, model.predict(X), color='red', label='Regression Line')  # Plot the regression line
plt.title("Simple Linear Regression: Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.legend()
plt.grid(True)
plt.show()
