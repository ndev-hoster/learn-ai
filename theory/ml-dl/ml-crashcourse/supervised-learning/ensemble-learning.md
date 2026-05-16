# 2.3.3 Introduction to Ensemble Learning

Ensemble Learning is the process of combining multiple individual models (often called "Weak Learners") to create one single "Strong Learner." 

The core philosophy is simple: **The wisdom of the crowd is more accurate than the individual expert.**

---

## 1. Why Ensemble? (Bias vs. Variance)

Individual models like Decision Trees are often prone to high error. Ensemble methods use two distinct strategies to fix this:

| Philosophy | Technique | Parallel/Sequential | Primary Goal | Champion Algorithm |
| :--- | :--- | :--- | :--- | :--- |
| **Bagging** | Bootstrap Aggregating | **Parallel** | Reduce **Variance** (Overfitting) | **Random Forest** |
| **Boosting** | Sequential Improvement | **Sequential** | Reduce **Bias** (Underfitting) | **XGBoost / AdaBoost** |

---

## 2. Bagging (Bootstrap Aggregating)

**The Logic:** Build many independent models at the same time and average their results.
- **The "Bag":** Uses **Bootstrapping** (sampling with replacement) to give each model a slightly different version of the training data.
- **Aggregation:** Combines the predictions via **Voting** (Classification) or **Averaging** (Regression).
- **Result:** Individual "mistakes" cancel each other out, leading to a much more stable and robust model.

---

## 3. Boosting (The Specialists)

**The Logic:** Build models one after another. Each new model focuses **only** on the mistakes made by the previous ones.
- **Sequential:** Model #2 is trained on the "Hard Cases" that Model #1 missed.
- **Weighting:** Data points that were misclassified are given "higher weight" to ensure the next model pays attention to them.
- **Result:** You start with a simple model and slowly "tutor" it into a highly accurate, complex model.

---

## 4. Summary: Which one when?

- **Use Bagging (Random Forest)** if your model is too complex and is **Overfitting** the training data.
- **Use Boosting (XGBoost)** if your model is too simple and is **Underfitting** (missing the trend).

---

## Navigation
- [<- Back to Decision Tree Regression](decision-tree-regression.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
- [2.3.4 Random Forest ->](random-forest.md)
