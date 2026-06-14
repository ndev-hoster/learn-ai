# Loss Functions — The Deep Dive

The Loss Function (or Cost Function) is the mathematical core of neural network training. It quantifies the difference between the network's prediction ($\hat{y}$) and the actual target ($y$). The entire goal of Backpropagation and Gradient Descent is to minimize this specific function.

Loss functions are strictly divided based on the task: **Regression** (predicting continuous values) vs. **Classification** (predicting discrete probabilities).

---

## 1. Regression Loss Functions

In regression, the network outputs a continuous number (e.g., house price, temperature).

### 1.1 Mean Squared Error (MSE / L2 Loss)
The absolute default for regression tasks.

$$ MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 $$

**Why it works:**
*   **Sign Elimination:** Squaring ensures negative errors (under-predictions) and positive errors (over-predictions) don't cancel each other out.
*   **Outlier Penalty:** Squaring disproportionately penalizes large errors. An error of $10$ adds $100$ to the loss, while an error of $0.1$ adds only $0.01$. The network will aggressively adjust weights to fix large mistakes.
*   **Smooth Gradients:** The derivative of $x^2$ is $2x$. As the error gets closer to $0$, the gradient naturally gets smaller. This means the network takes smaller, more precise steps as it approaches the global minimum, preventing it from overshooting.

### 1.2 Mean Absolute Error (MAE / L1 Loss)
Used when the dataset has many unpredictable outliers.

$$ MAE = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i| $$

**Why it works:**
*   **Robust to Outliers:** Because it doesn't square the error, an outlier of $10$ only adds $10$ to the loss (unlike $100$ in MSE). The network isn't forced to drastically shift its weights just to accommodate one weird data point.
*   **The Problem:** The derivative of $|x|$ is a constant (either $1$ or $-1$). Even when the error is tiny (e.g., $0.001$), the gradient size remains exactly the same. The network can continually "bounce" around the minimum and fail to converge perfectly without complex learning rate decay.

### 1.3 Huber Loss (Smooth L1 Loss)
The best of both worlds. It acts like MAE for large errors (outlier robust) and acts like MSE for small errors (smooth convergence).

$$
L_{\delta} = \begin{cases} 
\frac{1}{2}(y - \hat{y})^2 & \text{for } |y - \hat{y}| \le \delta \\
\delta|y - \hat{y}| - \frac{1}{2}\delta^2 & \text{for } |y - \hat{y}| > \delta 
\end{cases}
$$

*   $\delta$ (delta) is a hyperparameter that dictates where the function transitions from quadratic (MSE) to linear (MAE).

---

## 2. Classification Loss Functions

In classification, the network outputs probabilities (values between $0$ and $1$). 

### Why MSE Fails for Classification
If true $y=1$, and the model predicts $\hat{y}=0.01$ (a terrible prediction):
$$ MSE = (1 - 0.01)^2 = 0.9801 $$
The maximum possible error in MSE for probabilities is bounded at $1$. A loss of $0.98$ does not create a strong enough gradient to aggressively correct a network that is confidently wrong. Furthermore, applying MSE to outputs from a Sigmoid/Softmax activation results in a **non-convex** loss landscape (full of local minima where training gets stuck).

### 2.1 Binary Cross-Entropy (BCE / Log Loss)
Used for 2-class problems (e.g., Spam or Not Spam). The final layer must use a **Sigmoid** activation.

$$ BCE = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right] $$

**The "Automatic Switch" Mechanism:**
Because $y$ can only be $0$ or $1$, the equation elegantly collapses based on the truth:

*   **If $y = 1$:** The right side $(1-y)$ becomes $0$. The loss collapses to: **$- \log(\hat{y})$**
    *   If prediction is $0.99 \rightarrow -\log(0.99) \approx 0.01$ (low loss)
    *   If prediction is $0.01 \rightarrow -\log(0.01) \approx 4.60$ (massive penalty)
*   **If $y = 0$:** The left side $(y)$ becomes $0$. The loss collapses to: **$- \log(1 - \hat{y})$**
    *   If prediction is $0.01 \rightarrow -\log(1 - 0.01) = -\log(0.99) \approx 0.01$ (low loss)
    *   If prediction is $0.99 \rightarrow -\log(1 - 0.99) = -\log(0.01) \approx 4.60$ (massive penalty)

Logarithms approach infinity as the input approaches $0$. If the network confidently predicts the wrong class, the loss approaches infinity, generating massive gradients that force immediate correction.

### 2.2 Categorical Cross-Entropy (CCE)
Used for multi-class problems (e.g., predicting if an image is a Dog, Cat, or Bird). The final layer must use a **Softmax** activation (which outputs a probability distribution across all classes that sums to 1).

$$ CCE = - \sum_{c=1}^{M} y_{o,c} \log(\hat{y}_{o,c}) $$
*(where $M$ is the number of classes, $y$ is the binary indicator of the correct class, and $\hat{y}$ is the predicted probability for that class).*

**How it works:**
The true label $y$ must be **One-Hot Encoded**. 
E.g., if Cat is the correct class out of [Dog, Cat, Bird], $y = [0, 1, 0]$.
Because of the zeros in the one-hot array, the summation ignores all incorrect classes. The formula effectively collapses to taking the negative log of the probability assigned to the **correct class**.

*   If the model predicts $[0.1, \mathbf{0.8}, 0.1]$, Loss = $-\log(0.8) \approx 0.22$.
*   If the model predicts $[0.8, \mathbf{0.1}, 0.1]$, Loss = $-\log(0.1) \approx 2.30$.

### 2.3 Sparse Categorical Cross-Entropy
Mathematically identical to Categorical Cross-Entropy. 
*   **CCE** requires the target variable $y$ to be one-hot encoded arrays (e.g., `[0, 0, 1]`).
*   **Sparse CCE** allows the target variable $y$ to be raw integer labels (e.g., `Class 2`). It is a memory-saving optimization used in frameworks like TensorFlow/Keras when dealing with thousands of classes (like text vocabulary).

---

## 3. Deep Dive: The Mathematical Derivation of Cross-Entropy

*Why exactly do we use the logarithm? Where does the BCE formula actually come from?*

It doesn't come from trial and error. It is derived directly from probability theory using **Maximum Likelihood Estimation (MLE)**.

### Step 1: The Probability of a Single Prediction
If the network predicts a probability $\hat{y}$ that an image is a dog, then:
* Probability it is a dog = $\hat{y}$
* Probability it is NOT a dog = $(1 - \hat{y})$

We can write a single equation that gives us the probability of seeing the *actual* truth $y$ (where $y \in \{0,1\}$):
$$ P(y) = \hat{y}^y \cdot (1 - \hat{y})^{(1-y)} $$
*(Test it: if $y=1$, the equation gives $\hat{y}$. If $y=0$, it gives $1-\hat{y}$. Perfect.)*

### Step 2: The Likelihood of the Entire Dataset
We want to find weights that maximize the probability of our network correctly predicting the *entire* dataset simultaneously. Since individual predictions are independent, we multiply their probabilities together:
$$ L = \prod_{i=1}^{N} \hat{y}_i^{y_i} \cdot (1 - \hat{y}_i)^{(1-y_i)} $$

### Step 3: The Log Trick
Multiplying thousands of probabilities (like $0.8 \times 0.2 \times 0.99 \dots$) results in a number so infinitesimally small that computers suffer from **numerical underflow** (it just registers as $0$). 

To fix this, we take the natural logarithm ($\log$) of the entire equation. Because $\log$ is monotonically increasing, whatever maximizes $L$ will also maximize $\log(L)$. 

Taking the log turns products into sums, and exponents into multipliers:
$$ \log(L) = \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right] $$

### Step 4: From Maximizing Likelihood to Minimizing Loss
In Deep Learning, Optimizers are built to **minimize** functions (find the lowest point in the valley). We can't minimize a likelihood, but we *can* minimize the negative likelihood. 

We multiply the equation by $-1$, and divide by $N$ to get the average loss per sample:
$$ BCE = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right] $$

This proves that minimizing Binary Cross-Entropy is mathematically identical to finding the weights that are most likely to have generated the true dataset!

---

## Navigation
- [<- Back to Activation Functions](03_Activation_Functions.md)
- [Forward to Optimizers ->](05_Optimizers.md)
