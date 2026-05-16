# Walkthrough: The Mystery Snack Challenge (KNN)

In this example, we will manually calculate the distance to classify a new "Mystery Snack" using the K-Nearest Neighbors algorithm.

---

## 1. The Dataset
We have 5 snacks already categorized by two features: **Sweetness** and **Crunchiness** (on a scale of 1-10).

| Snack | Sweetness ($x$) | Crunchiness ($y$) | Category |
| :--- | :--- | :--- | :--- |
| **Apple** | 8 | 9 | Fruit |
| **Bacon** | 1 | 2 | Meat |
| **Grapes** | 9 | 1 | Fruit |
| **Carrot** | 2 | 8 | Veggie |
| **Steak** | 1 | 1 | Meat |

---

## 2. The Prediction Task
A new snack has arrived!
- **Sweetness:** 7
- **Crunchiness:** 7

**What is its category?** We will use **$K=3$** and **Euclidean Distance**.

---

## 3. Step 1: Calculate Euclidean Distances
The formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

| Snack | Calculation | Distance |
| :--- | :--- | :--- |
| **Apple** | $\sqrt{(7-8)^2 + (7-9)^2} = \sqrt{(-1)^2 + (-2)^2} = \sqrt{1+4}$ | **2.23** |
| **Bacon** | $\sqrt{(7-1)^2 + (7-2)^2} = \sqrt{(6)^2 + (5)^2} = \sqrt{36+25}$ | **7.81** |
| **Grapes** | $\sqrt{(7-9)^2 + (7-1)^2} = \sqrt{(-2)^2 + (6)^2} = \sqrt{4+36}$ | **6.32** |
| **Carrot** | $\sqrt{(7-2)^2 + (7-8)^2} = \sqrt{(5)^2 + (-1)^2} = \sqrt{25+1}$ | **5.09** |
| **Steak** | $\sqrt{(7-1)^2 + (7-1)^2} = \sqrt{(6)^2 + (6)^2} = \sqrt{36+36}$ | **8.48** |

---

## 4. Step 2: Sort and Rank
We rank the snacks from closest (smallest distance) to furthest.

1.  **Apple** (2.23)
2.  **Carrot** (5.09)
3.  **Grapes** (6.32)
4.  **Bacon** (7.81)
5.  **Steak** (8.48)

---

## 5. Step 3: Majority Vote ($K=3$)
We take the top 3 closest neighbors and look at their categories:

1.  **Apple** -> Fruit
2.  **Carrot** -> Veggie
3.  **Grapes** -> Fruit

**The Tally:**
- Fruit: 2 votes
- Veggie: 1 vote

---

## 6. The Final Decision
Because Fruit has the majority of the 3 closest neighbors, the AI classifies the Mystery Snack as a **Fruit**.

---

## Navigation
- [<- Back to KNN Theory](knn.md)
- [^ Back to Chapter 2 Index](../c2-supervised-learning.md)
