# Deep Dive: Mathematical Proof of Bayes' Theorem

Bayes' Theorem is not just an arbitrary formula; it is a direct consequence of the definition of **Conditional Probability**.

---

## 1. The Starting Point: Joint Probability

The probability of two events $A$ and $B$ both happening (their intersection) can be written in two ways:

1.  **$P(A \cap B) = P(A|B) \cdot P(B)$**
    - (The probability of $A$ given $B$, times the probability of $B$)
2.  **$P(A \cap B) = P(B|A) \cdot P(A)$**
    - (The probability of $B$ given $A$, times the probability of $A$)

---

## 2. The Derivation

Since both expressions equal the same joint probability $P(A \cap B)$, we can set them equal to each other:

$$P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

To isolate $P(A|B)$ (the Posterior), we simply divide both sides by $P(B)$:

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

---

## 3. Breaking Down the Intuition

- **The Symmetry:** The derivation shows that Bayes' Theorem is just a way of "flipping" conditional probabilities. 
- **The Normalizer ($P(B)$):** This term ensures that the resulting probability is scaled correctly between 0 and 1. In Naive Bayes, since $P(B)$ (the evidence) is the same for all classes being compared, we often ignore it during the calculation and just look for the highest numerator.

---

## Navigation
- [<- Back to Main Index](../../README.md)
- [<- Back to Naive Bayes](naive-bayes.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
