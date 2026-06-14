# Optimizers — Navigating the Loss Landscape

The **Optimizer** is the algorithm responsible for updating the weights and biases of the network based on the gradients calculated during backpropagation. Its goal is to navigate the high-dimensional loss landscape and find the global minimum as quickly and stably as possible.

---

## 1. The Foundation: Gradient Descent (GD)

Gradient Descent is the vanilla algorithm. It calculates the gradient over the **entire dataset** before taking a single step.

**The Update Rule:**
$$ w_{t+1} = w_t - \eta \cdot \nabla J(w_t) $$
*(Where $\eta$ is the learning rate, and $\nabla J(w_t)$ is the gradient of the loss function $J$ with respect to weight $w$).*

### Stochastic Gradient Descent (SGD)
Calculating the gradient over 1 million images for a single step is too slow. **SGD** calculates the gradient on a single random sample (or a small "mini-batch") and updates the weights immediately.

*   **Pros:** Much faster iterations; can escape shallow local minima due to noise.
*   **Cons:** The path to the minimum is incredibly noisy and zig-zags wildly because each batch pulls the gradient in a slightly different direction.

### Visualizing GD vs SGD

> **Batch Gradient Descent (GD)** takes a smooth, direct path to the center but requires processing the entire dataset per step.
> ![GD Visualization](media/gd.gif)

> **Mini-Batch SGD** takes a noisy, drunken path but computes each step much faster.
> ![SGD Visualization](media/sgd.gif)

---

## 2. Solving the "Ravine" Problem: Momentum & NAG

A major flaw of standard SGD is how it handles "ravines" — areas where the loss surface is very steep in one dimension but flat in another. SGD will violently oscillate up and down the steep walls while making agonizingly slow progress along the flat bottom.

### Momentum
Momentum solves this by simulating physics. Instead of updating weights based solely on the *current* gradient, it adds a fraction of the *previous* update vector.

**The Update Rule:**
$$ v_t = \gamma v_{t-1} + \eta \nabla J(w_t) $$
$$ w_{t+1} = w_t - v_t $$
*(Where $\gamma$ is the momentum term or "friction", usually set to $0.9$. $v_t$ is the velocity).*

**Why it works:** The oscillating gradients (left/right) mathematically cancel each other out, while the consistent gradients (forward) accumulate, accelerating the optimizer along the flat ravine.

> **Momentum** accelerating through the landscape, overshooting slightly, but correcting smoothly.
> ![Momentum Visualization](media/momentum.gif)

### Nesterov Accelerated Gradient (NAG)
Momentum is blind. It calculates the velocity, rolls forward, and *then* checks the gradient. If it's rolling down a hill and suddenly hits a sharp uphill, it takes a massive step uphill before realizing its mistake.
NAG is "smart momentum". It calculates where the momentum *will* take it, checks the gradient *there* (looking ahead), and makes the correction.

**The Update Rule:**
$$ v_t = \gamma v_{t-1} + \eta \nabla J(w_t - \gamma v_{t-1}) $$
$$ w_{t+1} = w_t - v_t $$

> **NAG** anticipates the bottom of the bowl and slows down earlier, preventing the massive overshoots seen in standard Momentum.
> ![NAG Visualization](media/nag.gif)

---

## 3. Solving Sparse Features: Adagrad & RMSprop

Momentum fixes the direction, but what about the step size (Learning Rate)?
In text data, the word "the" appears constantly (dense), while "xylophone" appears rarely (sparse). If we use a global learning rate $\eta$, weights for "the" will overshoot, while weights for "xylophone" will barely learn. We need an **Adaptive Learning Rate**.

### Adagrad (Adaptive Gradient Algorithm)
Adagrad scales the learning rate for each weight individually. It divides the learning rate by the square root of the accumulated sum of squared gradients for that specific weight.

**The Update Rule:**
$$ G_t = G_{t-1} + (\nabla J(w_t))^2 $$
$$ w_{t+1} = w_t - \frac{\eta}{\sqrt{G_t + \epsilon}} \cdot \nabla J(w_t) $$
*(Where $\epsilon$ is a tiny number to prevent division by zero).*

**The Problem:** Because $G_t$ accumulates *every* past gradient, it only grows. Eventually, the denominator becomes so massive that the learning rate shrinks to exactly zero, and the network stops learning entirely.

> **Adagrad** taking aggressive early steps, but slowing down as the accumulated gradient history forces the learning rate to shrink.
> ![AdaGrad Visualization](media/adagrad.gif)

### RMSprop (Root Mean Square Propagation)
Invented by Geoffrey Hinton (and famously published in a Coursera lecture rather than a paper), RMSprop fixes Adagrad's dying learning rate.
Instead of an infinite sum, it uses an **Exponentially Weighted Moving Average (EWMA)** of the squared gradients. It "forgets" the distant past.

**The Update Rule:**
$$ E[g^2]_t = \beta E[g^2]_{t-1} + (1 - \beta)(\nabla J(w_t))^2 $$
$$ w_{t+1} = w_t - \frac{\eta}{\sqrt{E[g^2]_t + \epsilon}} \cdot \nabla J(w_t) $$

> **RMSprop** dynamically scaling its learning rate without grinding to a halt. Notice how it takes a distinct, direct path regardless of scale.
> ![RMSprop Visualization](media/rmsprop.gif)

---

## 4. The King of Optimizers: Adam

**Adam (Adaptive Moment Estimation)** combines the brilliant ideas of both previous systems:
1.  **First Moment (Momentum):** A moving average of the raw gradients (builds velocity).
2.  **Second Moment (RMSprop):** A moving average of the squared gradients (scales learning rate).

**The Math:**
Calculate moving averages:
$$ m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla J(w_t) \quad \text{(Momentum)} $$
$$ v_t = \beta_2 v_{t-1} + (1 - \beta_2) (\nabla J(w_t))^2 \quad \text{(RMSprop)} $$

Because $m_t$ and $v_t$ are initialized at $0$, they are heavily biased toward zero in the early steps. Adam explicitly corrects this **bias**:
$$ \hat{m}_t = \frac{m_t}{1 - \beta_1^t} $$
$$ \hat{v}_t = \frac{v_t}{1 - \beta_2^t} $$

**The Final Update Rule:**
$$ w_{t+1} = w_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \cdot \hat{m}_t $$

> **Adam** perfectly combining velocity and adaptive scaling to slice straight into the global minimum. This is the default optimizer for 99% of Deep Learning models.
> ![Adam Visualization](media/adam.gif)

---

## Navigation
- [<- Back to Loss Functions](04_Loss_Functions.md)
- [Forward to Artificial Neural Networks (ANN) Practical ->](06_ANN_Practical.md)
