# 3.1.2 Hierarchical Clustering

While K-Means requires you to guess the number of clusters ($K$) beforehand, **Hierarchical Clustering** builds a hierarchy of clusters from $K=N$ down to $K=1$, allowing you to choose the optimal grouping after the fact.

The most common approach in industry is **Agglomerative** (Bottom-Up) clustering.

---

## 1. The Agglomerative Algorithm
Instead of starting with random centers, Agglomerative Clustering treats every single data point as its own isolated cluster and slowly merges them.

1.  **Calculate the Distance Matrix:** Measure the distance between every cluster and every other cluster.
2.  **Merge:** Find the two clusters with the shortest distance between them and merge them into a single cluster.
3.  **Update Matrix:** Recalculate the distances between the new merged cluster and all the remaining clusters.
4.  **Repeat:** Continue steps 2 and 3 until all points are merged into 1 giant cluster.

---

## 2. Linkage Criteria (How to measure distance)
When comparing two clusters (e.g., Cluster A with 5 points, Cluster B with 10 points), how do you calculate the "distance" between them? The method you choose dictates the shape of your final clusters.

| Linkage Type | How it measures distance between Cluster A and Cluster B | Pros / Cons |
| :--- | :--- | :--- |
| **Single (Min)** | The distance between the **closest** two points (one from A, one from B). | **Con:** Prone to the **"Chaining Effect."** A single stray point can cause two massive, distinct clusters to merge prematurely. |
| **Complete (Max)** | The distance between the **furthest** two points (one from A, one from B). | **Pro:** Forces clusters to be highly compact and spherical. |
| **Average** | The average distance of all points in A to all points in B. | **Pro:** Robust to outliers and balances compactness with flexibility. |
| **Ward's Method** | It tests the merge and measures the increase in **Variance (WCSS)**. It chooses the merge that increases variance the least. | **Pro:** The default in most libraries (like Scikit-Learn). It is the most robust and creates the most evenly sized clusters. |

---

## 3. The Dendrogram
The Dendrogram is a tree-like diagram that records the history of every merge.
- **X-axis:** The individual data points.
- **Y-axis:** The Distance at which the merge occurred.

### How to read and cut it:
Instead of guessing $K$, you look at the Dendrogram and find the **tallest vertical line** that isn't interrupted by any horizontal merging lines.
- A tall vertical gap means the algorithm had to increase the distance threshold significantly to force the next merge. 
- This implies that the clusters existing below that gap are naturally distinct and separate.
- **The Rule:** Draw a horizontal line through the tallest vertical gap. The number of vertical lines it slices through is your optimal $K$.

---

## 4. Pros and Cons

### Pros
- **No guessing $K$:** You can visualize the entire hierarchy and choose the optimal cut.
- **Deterministic:** Unlike K-Means (which relies on random initialization), Agglomerative clustering will always yield the exact same result on the same data.

### Cons (The $O(N^3)$ Wall)
- **Computationally Expensive:** Creating and constantly updating the Distance Matrix is brutal on RAM and CPU. The time complexity is $O(N^3)$.
- **Verdict:** Use Hierarchical Clustering for datasets under ~10,000 rows. For massive datasets, you must use K-Means ($O(N)$ complexity).

---

## Example Walkthrough
See the step-by-step trace of a [Distance Matrix update and Dendrogram construction](sample-application-hierarchical.md).

---

## Navigation
- [<- Back to K-Means](k-means.md)
- [3.1.3 DBSCAN Clustering ->](dbscan.md)
