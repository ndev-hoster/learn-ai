# 2.3.2 Decision Tree Regression (DTR)

Decision Tree Regression is the "step-brother" of the classifier. Instead of predicting a category, it predicts a continuous numerical value using a "Staircase of Averages."

---

## 1. The Strategy: "Similarity over Purity"

In a Classifier, we want our groups to be **Pure** (all one category).
In a Regressor, we want our groups to be **Consistent** (all numbers should be very close to each other).

The AI's goal is to minimize **Variance** within every group.

---

## 2. The Math: Mean Squared Error (MSE)

Instead of Entropy or Gini, DTR uses **Mean Squared Error** to decide where to split the data.

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (Actual_i - \bar{y})^2$$

- **The Split Logic:** The AI tests every possible split point in your data. It calculates the MSE for both resulting groups and picks the split that results in the **lowest total MSE**.
- **The "Perfect" Split:** If a split results in a group where every single number is identical (e.g., all houses are exactly $300k), the MSE is **0**.

---

## 3. The Prediction: "The Leaf Average"

Once the tree is built, making a prediction is simple:
1.  A new data point travels down the tree (If/Else logic).
2.  It lands in a **Leaf Node**.
3.  The AI looks at all the training points that ended up in that same leaf and calculates their **Mean (Average)**.
4.  **The Result:** That average is your final prediction.

---

## 4. DTR vs. Linear Regression: The "Staircase" Problem

| Feature | Linear Regression | Decision Tree Regression |
| :--- | :--- | :--- |
| **Shape** | A smooth, continuous line. | A "blocky" staircase of discrete steps. |
| **Non-Linearity** | Struggles with sudden jumps. | Loves sudden jumps and "If/Then" logic. |
| **Extrapolation** | Can predict values higher than the training data (Follows the trend). | **Cannot Extrapolate.** It can never predict a value higher/lower than the ones it saw during training. |

---

## 5. Summary: When to use DTR?

**Use DTR when:**
- Your data has complex "If/Then" relationships (e.g., "If it's a holiday AND raining, wait time is 40 mins").
- You have a mix of categorical and numerical features.
- You don't need to predict values outside the range of your history.

**Avoid DTR when:**
- You need a smooth, continuous forecast (like predicting a child's height over time).
- You are trying to predict the future (Stock market, trends).

---

## Navigation
- [<- Back to Decision Tree Classifier](decision-trees.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
- [2.3.3 Intro to Ensemble Learning ->](ensemble-learning.md)
