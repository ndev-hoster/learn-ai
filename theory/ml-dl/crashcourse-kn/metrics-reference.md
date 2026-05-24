# Mathematical Reference: Loss vs. Evaluation

This sheet separates functions by their role in the machine learning lifecycle.

---

## 1. Optimization (Loss Functions)
*These are used **internally** by algorithms during training to update weights/parameters. They must be differentiable.*

### Mean Squared Error (MSE)
$$Loss = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### Mean Absolute Error (MAE)
$$Loss = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

### Binary Cross-Entropy / Log Loss
$$Loss = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]$$

### Categorical Cross-Entropy (CCE)
Used for Multi-class classification (Softmax).
$$Loss = -\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{C} y_{ij} \log(\hat{y}_{ij})$$
- $n$: Number of samples.
- $C$: Number of classes.
- $y_{ij}$: 1 if sample $i$ belongs to class $j$, else 0 (One-Hot Encoded).
- $\hat{y}_{ij}$: The predicted probability for class $j$.

---

## 2. Evaluation (Performance Metrics)
*These are used **externally** to benchmark the final model. They provide a human-readable "grade."*

### R-Squared ($R^2$)
$$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

### Adjusted R-Squared
$$Adjusted R^2 = 1 - \left[ \frac{(1 - R^2)(n - 1)}{n - k - 1} \right]$$

### Root Mean Squared Error (RMSE)
$$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

### Accuracy
$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

### Precision
$$Precision = \frac{TP}{TP + FP}$$

### Recall
$$Recall = \frac{TP}{TP + FN}$$

### F1-Score
$$F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$

---

## Navigation
- [<- Back to Main Index](../README.md)
- [^ Back to Chapter 2 Index](c2-supervised-learning.md)
- [<- Back to Linear Regression](supervised-learning/linear-regression.md)
