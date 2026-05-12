# Multi-class Classification Examples (Logistic Regression)

This file provides concrete examples of how Logistic Regression is extended to handle multiple classes (more than 2).

---

## Example 1: One-vs-Rest (OvR) - "The Fruit Classifier"

Imagine you want to classify images into three categories: **Apple**, **Banana**, and **Orange**.

### The Setup:
You train **three separate** binary Logistic Regression models:

1.  **Model A (Apple vs. All):** Trained to distinguish Apples (Class 1) from everything else (Banana/Orange = Class 0).
2.  **Model B (Banana vs. All):** Trained to distinguish Bananas (Class 1) from everything else (Apple/Orange = Class 0).
3.  **Model C (Orange vs. All):** Trained to distinguish Oranges (Class 1) from everything else (Apple/Banana = Class 0).

### The Prediction:
You have a new image. You run it through all three models:
- Model A says: $P(\text{Apple}) = 0.12$
- Model B says: $P(\text{Banana}) = 0.85$
- Model C says: $P(\text{Orange}) = 0.40$

**Result:** The algorithm selects **Banana** because it has the highest probability score.

---

## Example 2: Multinomial (Softmax) - "The Direct Approach"

Instead of separate binary models, Softmax calculates all class probabilities simultaneously in a single mathematical step.

### 1. Under the Hood: One Weight Vector per Class
In the binary case, we had one set of weights ($\beta$) to decide between 0 and 1. In Multinomial Regression, the model learns a **unique set of weights for every class**.

If we have features like **Color**, **Weight**, and **Texture**:
- $\beta_{Apple}$ learns what an Apple looks like.
- $\beta_{Banana}$ learns what a Banana looks like.
- $\beta_{Orange}$ learns what an Orange looks like.

### 2. Generating the "Logits" ($z$)
For a new fruit, we multiply its features by each weight vector to get a raw "score" (called a **Logit**):
- $z_{Apple} = \beta_{Apple} \cdot X = 2.0$
- $z_{Banana} = \beta_{Banana} \cdot X = 5.0$
- $z_{Orange} = \beta_{Orange} \cdot X = 1.0$

### 3. The Two-Step Softmax Transformation
Softmax turns these raw scores into probabilities using a two-step process:

#### Step A: Exponentiation ($e^z$)
We raise $e$ to the power of each score. 
1. $e^{2.0} \approx \mathbf{7.39}$
2. $e^{5.0} \approx \mathbf{148.41}$
3. $e^{1.0} \approx \mathbf{2.72}$

**Why do this?** 
- It makes all values **positive** (you can't have negative probability).
- It **amplifies the leader**. Notice how the score of 5 was 2.5x larger than 2, but after exponentiation, 148 is **20x larger** than 7. This helps the model "make a decision."

#### Step B: Normalization ($\sum$)
We divide each result by the total sum of all results ($7.39 + 148.41 + 2.72 = 158.52$).

- $P(\text{Apple}) = 7.39 / 158.52 \approx \mathbf{0.046}$
- $P(\text{Banana}) = 148.41 / 158.52 \approx \mathbf{0.936}$
- $P(\text{Orange}) = 2.72 / 158.52 \approx \mathbf{0.017}$

**Result:** The probabilities sum to exactly **1.0**.

---

## 4. How the Model Learns: Categorical Cross-Entropy

To improve, the model uses **Categorical Cross-Entropy**. While it looks complex with its double summation, it's actually quite simple due to **One-Hot Encoding**.

### The Expanded Formula:
$$J(\beta) = -\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{C} y_{ij} \log(\hat{y}_{ij})$$

### Breaking it down (The "One-Hot" Trick):
1.  **$y_{ij}$ (The Ground Truth):** This is a vector of 0s and 1s. For a **Banana**, $y$ looks like this: $[0, 1, 0]$ (Apple=0, Banana=1, Orange=0).
2.  **The Summation:** The formula sums over every class ($j$). However, since $y_{ij}$ is **zero** for all classes except the correct one, all those terms disappear!
3.  **The Result:** For any single data point, the formula "collapses" into:
    $$Loss = -(1 \cdot \log(P_{\text{correct class}}))$$

### Calculation Example:
Using our **Banana** prediction from earlier:
- **Actual Class:** Banana ($y = [0, 1, 0]$)
- **Predicted Probabilities:** $[\hat{y}_{Apple}=0.046, \hat{y}_{Banana}=0.936, \hat{y}_{Orange}=0.017]$

$$Loss = -[ (0 \cdot \log(0.046)) + (1 \cdot \log(0.936)) + (0 \cdot \log(0.017)) ]$$
$$Loss = -\log(0.936) \approx \mathbf{0.066}$$

**Observation:** The model is "happy" because the loss is near zero. If the model had predicted a low probability for Banana (e.g., $0.1$), the $-\log(0.1)$ would have been **2.30**, signaling to the algorithm that it needs to make a big adjustment to its weights.

---

## Navigation
- [<- Back to Main Index](../../README.md)
- [<- Back to Logistic Regression](logistic-regression.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
