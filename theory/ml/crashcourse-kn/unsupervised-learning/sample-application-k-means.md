# Walkthrough: K-Means Clustering (Manual Trace)

In this walkthrough, we will trace **two iterations** of the K-Means algorithm on a 2D coordinate dataset, including the **K-Means++** initialization math.

---

## 1. The Dataset
We have 6 points representing store locations in a small city. We want to find **K=2** retail hubs.

**Table 1: Input Coordinates**

| Point | X (Coord) | Y (Coord) |
| :--- | :--- | :--- |
| **P1** | 1 | 1 |
| **P2** | 2 | 1 |
| **P3** | 1 | 2 |
| **P4** | 5 | 5 |
| **P5** | 6 | 5 |
| **P6** | 5 | 6 |

---

## 2. Step 0: K-Means++ Initialization

We want to pick 2 centroids ($\mu_1, \mu_2$) that are spread out.

1.  **Select $\mu_1$:** We pick **P1 (1,1)** randomly.
2.  **Calculate $D(x)^2$ to $\mu_1$:**

**Table 2: Lottery Tickets for $\mu_2$**

| Point | Dist to $\mu_1$ ($D$) | $D^2$ (Tickets) | Prob of Selection |
| :--- | :--- | :--- | :--- |
| **P2** | $\sqrt{(2-1)^2 + (1-1)^2} = 1$ | **1** | $1 / 100 \approx 1\%$ |
| **P3** | $\sqrt{(1-1)^2 + (2-1)^2} = 1$ | **1** | $1 / 100 \approx 1\%$ |
| **P4** | $\sqrt{(5-1)^2 + (5-1)^2} = 5.6$ | **32** | $32 / 100 = 32\%$ |
| **P5** | $\sqrt{(6-1)^2 + (5-1)^2} = 6.4$ | **41** | $41 / 100 = 41\%$ |
| **P6** | $\sqrt{(5-1)^2 + (6-1)^2} = 6.4$ | **25** | $25 / 100 = 25\%$ |
| **Total** | - | **100** | **100%** |

**The Result:** Point **P5 (6,5)** wins the lottery and becomes **$\mu_2$**.
- $\mu_1 = (1, 1)$
- $\mu_2 = (6, 5)$

---

## 3. Iteration 1: Assignment

We measure the distance from every point to both centroids and assign to the nearest.

**Table 3: Iteration 1 Assignments**

| Point | Dist to $\mu_1$ (1,1) | Dist to $\mu_2$ (6,5) | Assigned Cluster |
| :--- | :--- | :--- | :--- |
| **P1** | 0.0 | 6.4 | **C1** |
| **P2** | 1.0 | 5.6 | **C1** |
| **P3** | 1.0 | 5.8 | **C1** |
| **P4** | 5.6 | 1.0 | **C2** |
| **P5** | 6.4 | 0.0 | **C2** |
| **P6** | 5.8 | 1.4 | **C2** |

---

## 4. Iteration 1: Centroid Update (Moving)

We calculate the **Mean** (Average) of each cluster to find the new centroid positions.

- **New $\mu_1$:** Average of {P1, P2, P3}
  - $X = (1+2+1)/3 = \mathbf{1.33}$
  - $Y = (1+1+2)/3 = \mathbf{1.33}$
- **New $\mu_2$:** Average of {P4, P5, P6}
  - $X = (5+6+5)/3 = \mathbf{5.33}$
  - $Y = (5+5+6)/3 = \mathbf{5.33}$

---

## 5. Iteration 2: Convergence Check

We repeat the assignment with the new coordinates: **$\mu_1=(1.33, 1.33)$** and **$\mu_2=(5.33, 5.33)$**.

```mermaid
graph TD
    S1[Start: P1, P5] --> A1[Assign C1:{P1,P2,P3} C2:{P4,P5,P6}]
    A1 --> M1[Move Centroids to 1.33 and 5.33]
    M1 --> A2[Re-Assign: No points change teams!]
    A2 --> Final((Convergence))
```

**Final Result:**
- **Cluster 1:** {P1, P2, P3} - Center: (1.33, 1.33)
- **Cluster 2:** {P4, P5, P6} - Center: (5.33, 5.33)

---

## Navigation
- [<- Back to Theory](k-means.md)
- [^ Back to Chapter 3 Index](../c3-unsupervised-learning.md)
