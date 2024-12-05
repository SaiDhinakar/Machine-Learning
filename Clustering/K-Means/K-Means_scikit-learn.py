from sklearn.cluster import KMeans
import random
import matplotlib.pyplot as plt

# Sample 2D dataset
X = [[random.randrange(-500, 500), random.randrange(-500, 500)] for _ in range(200)]  # Create a list of 2D points

k = 3  # Number of clusters

# Fit the KMeans model
model = KMeans(n_clusters=k, random_state=42)
model.fit(X)  # Pass the 2D dataset

# Get the cluster labels and centroids
cluster = model.labels_
centroids = model.cluster_centers_

# Plot the points with cluster colors
plt.scatter([point[0] for point in X], [point[1] for point in X], c=cluster, cmap='viridis', label='Data Points')
# Plot the centroids
plt.scatter([centroid[0] for centroid in centroids], [centroid[1] for centroid in centroids], 
            color='red', marker='*', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.show()
