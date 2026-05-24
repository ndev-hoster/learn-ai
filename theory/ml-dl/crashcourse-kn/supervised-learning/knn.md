# 2.2.4 K-Nearest Neighbors (KNN)

K-Nearest Neighbors (KNN) is one of the most intuitive and simple algorithms in Machine Learning. It is a **Non-Parametric** and **Lazy Learning** algorithm used for both **Classification** and **Regression**.

---

## 1. The Intuition: "Tell me who your friends are..."

The core idea behind KNN is simple: **Similar things exist in close proximity.**

Imagine you move to a new neighborhood. You don't know the local culture yet, but you see that your 5 closest neighbors all drive electric cars. You can safely assume that the "vibe" of this area is pro-electric. 

- **In Classification:** You look at the $K$ closest neighbors and take a **Majority Vote**. If most are "Blue," you are "Blue."
- **In Regression:** You look at the $K$ closest neighbors and take the **Average** of their values. If their average house price is $500k, yours is predicted to be $500k.

---

## 2. The Ruler: Distance Metrics

To find "Neighbors," we need a way to measure distance.

### A. Euclidean Distance ($L_2$ Norm)
The most common "straight-line" distance.
$$d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$

### B. Manhattan Distance ($L_1$ Norm)
The "Taxicab" distance. Used when you can only move in grid-like paths (like city blocks).
$$d(p, q) = \sum_{i=1}^{n} |p_i - q_i|$$
1
### C. Minkowski Distance (The General Formula)
This is a generalized distance metric. By changing the value of $p$, you get different metrics:
$$d(p, q) = \left( \sum_{i=1}^{n} |p_i - q_i|^p \right)^{1/p}$$
- If $p=1$, it is **Manhattan Distance**.
- If $p=2$, it is **Euclidean Distance**.

---

## 3. The "Lazy Learner" (Computational Complexity)

KNN is called a **Lazy Learner** because it doesn't actually "learn" or build a model during the training phase. It just "memorizes" the training data.

| Phase | Complexity | What's happening? |
| :--- | :--- | :--- |
| **Training** | $O(1)$ | Literally nothing. The data is just stored in memory. |
| **Prediction** | $O(n \cdot d)$ | For *every* new point, the AI must calculate the distance to *every single* point ($n$) across all features ($d$). |

**The Tax:** While training is instant, predicting becomes incredibly slow as your dataset grows.

---

## 4. The Goldilocks Problem: Choosing K

Choosing the value of $K$ is the most important part of tuning KNN.

- **If $K$ is too small (e.g., $K=1$):** The model is too "twitchy." It will react to every single outlier or piece of noise. This is **Overfitting** (High Variance).
- **If $K$ is too large (e.g., $K=100$):** The model becomes too "blurry." It ignores local patterns and just predicts whatever the majority of the whole dataset is. This is **Underfitting** (High Bias).

> **Pro Tip:** A common rule of thumb is to set $K = \sqrt{n}$ (where $n$ is the number of data points) and to pick an **odd number** to avoid tie-breaks in voting.

---

## 5. Critical Step: Feature Scaling

Because KNN relies entirely on distance, the **scale** of your numbers matters immensely.

**The Problem:** Imagine you are comparing people based on **Age** (0-100) and **Annual Income** ($0-$1,000,000).
In the Euclidean formula, a difference of $1,000 in income will completely "swamp" a difference of 50 years in age. The AI will think income is the only thing that matters.

**The Solution:** You must **Normalize** or **Standardize** your data so that all features are on a similar scale (e.g., 0 to 1).

---

## 6. The Curse of Dimensionality

KNN hates "Empty Space." As you add more features (dimensions), the volume of the search space grows exponentially. 

In high-dimensional space (e.g., 100 features), all data points become "lonely" and far apart. Even the "nearest" neighbor might be miles away, making the "similarity" logic of KNN fall apart.

---

## 7. Pros and Cons

### Pros:
- **Simple & Intuitive:** No complex math involved in "learning."
- **Versatile:** Works for both Classification and Regression.
- **No Assumptions:** It doesn't assume your data follows a specific distribution (unlike Linear Regression).

### Cons:
- **Slow Prediction:** Gets slower as you add more data.
- **Memory Intensive:** You must keep the *entire* dataset in RAM.
- **Sensitive to Outliers:** Especially with a small $K$.

---

## Example Walkthrough
Ready to see the math in action? Check out the [Mystery Snack Challenge: KNN Step-by-Step](sample-application-knn.md).

---

## Navigation
- [<- Back to Naive Bayes](naive-bayes.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
- [2.3.1 Decision Trees ->](decision-trees.md)
