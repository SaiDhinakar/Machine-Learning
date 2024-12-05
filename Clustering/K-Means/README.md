---

# K-Means Clustering Algorithm

## **Overview**
K-Means is an **unsupervised machine learning algorithm** used for clustering. It organizes data points into \(k\) distinct clusters, where \(k\) is a predefined number. The goal is to minimize the variance within each cluster and maximize the variance between clusters.

In simple terms, K-Means identifies groups in data such that points in the same group are more similar to each other than to those in other groups.

---

## **How K-Means Works**

### **1. Initialize Centroids**
- Randomly select \(k\) points in the dataset as the initial centroids (cluster centers).
  
### **2. Assign Points to Clusters**
- For each data point, compute its distance to all centroids.
- Assign the point to the cluster with the nearest centroid.

### **3. Update Centroids**
- For each cluster, calculate the new centroid as the **mean** of all points in that cluster.  
  The formula for the new centroid in a cluster is:
  \[
  \mu_i = \frac{1}{|C_i|} \sum_{x \in C_i} x
  \]
  - \(\mu_i\): New centroid of cluster \(i\).
  - \(C_i\): Set of points in cluster \(i\).
  - \(|C_i|\): Number of points in cluster \(i\).
  - \(x\): Data points in the cluster.

### **4. Repeat Until Convergence**
- Steps 2 and 3 are repeated until:
  1. Centroids do not change significantly.
  2. A maximum number of iterations is reached.

---

## **Mathematical Objective**
The goal of K-Means is to minimize the following **within-cluster sum of squared errors (WCSS):**
\[
J = \sum_{i=1}^{k} \sum_{x \in C_i} \| x - \mu_i \|^2
\]
- \(\| x - \mu_i \|\): Distance between a data point \(x\) and the centroid \(\mu_i\).

---

## **Visualization**
Below is a step-by-step representation of K-Means clustering on a 2D dataset:

---

## **Advantages of K-Means**
1. **Simple and fast:** Efficient for large datasets.
2. **Scalable:** Performs well with higher-dimensional data.
3. **Widely applicable:** Used in many fields like customer segmentation, image compression, and document clustering.

---

## **Limitations of K-Means**
1. **Requires \(k\) to be specified:** The number of clusters must be predetermined.
2. **Sensitive to initialization:** Poor initial centroids can lead to suboptimal clustering.
3. **Assumes spherical clusters:** Struggles with complex or overlapping clusters.
4. **Outlier sensitivity:** Outliers can significantly affect centroids.

---

## **Applications**
1. **Customer Segmentation:** Grouping customers based on purchasing behavior.
2. **Image Compression:** Reducing the number of colors in an image by clustering pixel colors.
3. **Anomaly Detection:** Identifying outliers as points that don't fit into any cluster.

---

## **Distance Metrics**
While K-Means typically uses **Euclidean distance**, other distance metrics like Manhattan or cosine similarity can also be used for specific datasets:
\[
\text{Euclidean Distance: } d = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}
\]

---

## **Output**
how to add image in markdown
![K-Means Clustering](https://imgs.search.brave.com/vIKg1VnoqVkKucm-5Vnx9LQqnQ17ouzZuTcHH1WJMik/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZWVrc2Zvcmdl/ZWtzLm9yZy93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMzAzMjAx/NzM5MTUvZG93bmxv/YWQtKDI4KS5wbmc)
