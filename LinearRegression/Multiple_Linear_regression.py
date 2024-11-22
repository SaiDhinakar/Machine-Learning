import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Create the dataset
data = {
    'Years_of_Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Education_Level': [3, 4, 5, 6, 7, 8, 9, 9, 10, 10],
    'Hours_Worked_Per_Week': [40, 42, 44, 45, 48, 50, 52, 53, 55, 60],
    'Salary': [40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
}

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Step 2: Separate the features (X) and the target variable (y)
X = df[['Years_of_Experience', 'Education_Level', 'Hours_Worked_Per_Week']]  # Features
y = df['Salary']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Evaluate the model using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 5: Plotting
# Plot relationship between Salary and each feature

# Plot 1: Salary vs Years of Experience
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.scatter(df['Years_of_Experience'], df['Salary'], color='blue', label='Actual Data')
plt.plot(df['Years_of_Experience'], model.predict(df[['Years_of_Experience', 'Education_Level', 'Hours_Worked_Per_Week']]), color='red', label='Fitted Line')
plt.title('Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.legend()

# Plot 2: Salary vs Education Level
plt.subplot(1, 3, 2)
plt.scatter(df['Education_Level'], df['Salary'], color='blue', label='Actual Data')
plt.plot(df['Education_Level'], model.predict(df[['Years_of_Experience', 'Education_Level', 'Hours_Worked_Per_Week']]), color='red', label='Fitted Line')
plt.title('Salary vs Education Level')
plt.xlabel('Education Level')
plt.ylabel('Salary ($)')
plt.legend()

# Plot 3: Salary vs Hours Worked Per Week
plt.subplot(1, 3, 3)
plt.scatter(df['Hours_Worked_Per_Week'], df['Salary'], color='blue', label='Actual Data')
plt.plot(df['Hours_Worked_Per_Week'], model.predict(df[['Years_of_Experience', 'Education_Level', 'Hours_Worked_Per_Week']]), color='red', label='Fitted Line')
plt.title('Salary vs Hours Worked Per Week')
plt.xlabel('Hours Worked Per Week')
plt.ylabel('Salary ($)')
plt.legend()

plt.tight_layout()
plt.show()

# 3D Plot of all three features
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Years_of_Experience'], df['Education_Level'], df['Salary'], color='blue', label='Actual Data')

# Create a meshgrid for the 3D surface plot
x_surf, y_surf = np.meshgrid(np.linspace(df['Years_of_Experience'].min(), df['Years_of_Experience'].max(), 100),
                             np.linspace(df['Education_Level'].min(), df['Education_Level'].max(), 100))
z_surf = model.predict(np.array([x_surf.ravel(), y_surf.ravel(), np.full_like(x_surf.ravel(), df['Hours_Worked_Per_Week'].mean())]).T).reshape(x_surf.shape)

ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5)
ax.set_xlabel('Years of Experience')
ax.set_ylabel('Education Level')
ax.set_zlabel('Salary')
ax.set_title('3D Surface Plot: Salary vs Years of Experience, Education Level')

plt.show()
