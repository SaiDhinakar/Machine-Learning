import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a dataset with 5 features
X, y = make_classification(
    n_samples=100,  # Number of samples
    n_features=5,   # Total number of features
    n_informative=3,  # Informative features
    n_redundant=1,  # Redundant features
    n_repeated=0,   # No repeated features
    random_state=42
)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Logistic Regression classifier
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Create a 2D grid (mesh grid) for plotting decision boundaries
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))

# Create a grid with 5 features (add 3 features with default value, e.g., 0)
grid = np.c_[xx.ravel(), yy.ravel(), np.zeros(xx.ravel().shape[0]), np.zeros(xx.ravel().shape[0]), np.zeros(xx.ravel().shape[0])]

# Predict the class for each point in the grid
Z = model.predict(grid)

# Reshape the predictions back into the shape of the grid
Z = Z.reshape(xx.shape)

# Plot the decision boundary
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.RdYlBu)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.RdYlBu)
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
