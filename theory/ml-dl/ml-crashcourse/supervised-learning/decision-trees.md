# 2.3.1 Decision Tree Classifier

Decision Trees are "White Box" models that mimic human logic. They break complex datasets into a series of simple, binary (Yes/No) questions to reach a final classification.

---

## 1. The Strategy: "Greedy Purity"

A Decision Tree is **Greedy**. At every step, it looks for the single question that will make the resulting groups as **Pure** as possible.

- **Pure Group:** Every member belongs to the same class (e.g., All "Yes").
- **Impure Group:** A messy mix of classes (e.g., 50% "Yes", 50% "No").

---

## 2. The Math: Measuring Chaos

To find the "Purest" split, we need a way to measure the "Messiness" of a group.

### A. Entropy ($H$)
Entropy measures the amount of disorder or uncertainty in the data.
$$H(S) = \sum_{i=1}^{c} -p_i \log_2 p_i$$
- **Entropy = 0:** The group is perfectly pure (no chaos).
- **Entropy = 1:** The group is a perfect 50/50 mix (maximum chaos).

### B. Information Gain ($IG$)
Information Gain is the **reduction in entropy** achieved by splitting the data on a specific feature.
$$IG(\text{Feature}) = \text{Entropy(Before)} - \text{Entropy(After Split)}$$
**The Goal:** The AI calculates IG for every feature and picks the one with the **highest** value as the split point.

### C. Gini Impurity (The Industry Shortcut)
Most libraries (like Scikit-Learn) use Gini by default because it's faster to calculate (no logarithms).
$$Gini = 1 - \sum p_i^2$$
It gives nearly identical results to Entropy but requires less computational power.

---

## 3. The Overfitting Trap: Why trees need "Gardening"

If left alone, a Decision Tree will grow until every single data point is in its own private leaf. It will **memorize** the training data (Overfitting) and fail on new data.

### The Solution: Pruning
| Method | Strategy | Analogy |
| :--- | :--- | :--- |
| **Pre-Pruning** | Stop growth early using hyperparameters (**Max Depth**, **Min Samples Split**). | Setting a word limit *while* writing an essay. |
| **Post-Pruning** | Let the tree grow fully, then cut back branches that don't add enough value (using **Cost-Complexity Pruning**). | Writing a long draft and then *surgically deleting* the fluff later. |

---

## 4. Pros and Cons

### Pros:
- **Interpretability:** You can literally read the tree like a flowchart.
- **No Scaling Required:** Unlike KNN or SVM, trees don't care about the range of your numbers.
- **Handles Mixes:** Works with both categorical and numerical data out of the box.

### Cons:
- **High Instability:** Change one data point, and the entire tree might change its structure.
- **Greedy Nature:** It might miss better global patterns because it only focuses on the best split *right now*.

---

## Example Walkthrough
See exactly how the math builds a tree using the [Play Tennis Dataset: Step-by-Step](sample-application-dt.md).

---

## Navigation
- [<- Back to KNN](knn.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
- [2.3.2 Decision Tree Regression ->](decision-tree-regression.md)
