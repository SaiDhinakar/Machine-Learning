import random
import math
import matplotlib.pyplot as plt 

# Sample 2D dataset
X = [random.randrange(-500, 500) for _ in range(200)]
Y = [random.randrange(-500, 500) for _ in range(200)]

K = 3  # Number of clusters

# Initialize centroids randomly within the range of the data
centroids = [(random.randint(min(X), max(X)), random.randint(min(Y), max(Y))) for _ in range(K)]

def calculate_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def assign_points_to_clusters(X, Y, centroids):
    """Assign each data point to the nearest centroid."""
    clusters = [[] for _ in range(K)]
    for x, y in zip(X, Y):
        min_distance = float('inf')
        closest_centroid_idx = None
        for i, (cx, cy) in enumerate(centroids):
            distance = calculate_distance(x, y, cx, cy)
            if distance < min_distance:
                min_distance = distance
                closest_centroid_idx = i
        clusters[closest_centroid_idx].append((x, y))
    return clusters

def update_centroids(clusters):
    """Update centroids by calculating the mean of points in each cluster."""
    new_centroids = []
    for cluster in clusters:
        if cluster:  # Avoid empty clusters
            mean_x = sum(point[0] for point in cluster) / len(cluster)
            mean_y = sum(point[1] for point in cluster) / len(cluster)
            new_centroids.append((mean_x, mean_y))
        else:
            # Reinitialize centroid randomly if cluster is empty
            new_centroids.append((random.randint(-500, 500), random.randint(-500, 500)))
    return new_centroids

# Main K-Means loop
max_iters = 100
for iteration in range(max_iters):
    clusters = assign_points_to_clusters(X, Y, centroids)
    new_centroids = update_centroids(clusters)

    # Check for convergence
    if new_centroids == centroids:
        print(f"Converged after {iteration+1} iterations!")
        break
    centroids = new_centroids

# Output final clusters and centroids
print("Final Centroids:", centroids)
print("Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")


colors = ['b', 'r', 'g', 'y']

for idx, cluster in enumerate(clusters):
    x = [point[0] for point in cluster]
    y = [point[1] for point in cluster]
    plt.scatter(x, y, c=colors[idx])

    # Calculate the centroid of the cluster
    centroid_x = sum(x) / len(x)
    centroid_y = sum(y) / len(y)

    # Plot the centroid with yellow color
    plt.scatter(centroid_x, centroid_y, c='y', s=200, marker='*')  # s=200 makes the centroid marker larger

plt.show()