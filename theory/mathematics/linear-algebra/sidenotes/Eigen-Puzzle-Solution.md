# Solution to the Eigen-Puzzle: The Fibonacci Matrix

### The Puzzle Setup
We are given the following matrix:
$$ A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} $$

---

### Part 1: Computing Powers by Hand
Let's start by computing the first few powers of $A$:
*   $A^1 = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$
*   $A^2 = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}$
*   $A^3 = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}$
*   $A^4 = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} 2 & 3 \\ 3 & 5 \end{bmatrix}$
*   $A^5 = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ 3 & 5 \end{bmatrix} = \begin{bmatrix} 3 & 5 \\ 5 & 8 \end{bmatrix}$

**The Pattern:** The entries of these matrices are exactly the **Fibonacci sequence** ($0, 1, 1, 2, 3, 5, 8 \dots$). 
Specifically, $A^n = \begin{bmatrix} F_{n-1} & F_n \\ F_n & F_{n+1} \end{bmatrix}$.

This happens because multiplying a vector $\begin{bmatrix} F_{n-1} \\ F_n \end{bmatrix}$ by $A$ gives $\begin{bmatrix} F_n \\ F_{n-1} + F_n \end{bmatrix} = \begin{bmatrix} F_n \\ F_{n+1} \end{bmatrix}$. The matrix mathematically encodes the Fibonacci rule: *"the next number is the sum of the previous two."*

---

### Part 2: Using the Eigenbasis
We want an efficient way to compute $A^n$. The puzzle gives us two eigenvectors:
$$ \vec{v}_1 = \begin{bmatrix} 2 \\ 1 + \sqrt{5} \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 2 \\ 1 - \sqrt{5} \end{bmatrix} $$

Let's find their corresponding eigenvalues. We know $A\vec{v} = \lambda\vec{v}$:
$$ \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \pm \sqrt{5} \end{bmatrix} = \begin{bmatrix} 1 \pm \sqrt{5} \\ 3 \pm \sqrt{5} \end{bmatrix} $$

If we factor out the eigenvalues, we get:
*   $\lambda_1 = \frac{1 + \sqrt{5}}{2}$ (This is the **Golden Ratio**, often denoted as $\phi \approx 1.618$)
*   $\lambda_2 = \frac{1 - \sqrt{5}}{2}$ (Let's call this $\psi \approx -0.618$)

Now we can set up our Diagonalization ($A = PDP^{-1}$):
$$ P = \begin{bmatrix} 2 & 2 \\ 1 + \sqrt{5} & 1 - \sqrt{5} \end{bmatrix} $$
$$ D = \begin{bmatrix} \frac{1 + \sqrt{5}}{2} & 0 \\ 0 & \frac{1 - \sqrt{5}}{2} \end{bmatrix} $$

To find $P^{-1}$, we use the $2 \times 2$ inverse rule ($\frac{1}{\det(P)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$):
$$ \det(P) = 2(1 - \sqrt{5}) - 2(1 + \sqrt{5}) = -4\sqrt{5} $$
$$ P^{-1} = \frac{-1}{4\sqrt{5}} \begin{bmatrix} 1 - \sqrt{5} & -2 \\ -(1 + \sqrt{5}) & 2 \end{bmatrix} = \frac{1}{4\sqrt{5}} \begin{bmatrix} -1 + \sqrt{5} & 2 \\ 1 + \sqrt{5} & -2 \end{bmatrix} $$

---

### Part 3: Computing $A^n$ and Binet's Formula
Using the power rule for diagonalized matrices:
$$ A^n = P D^n P^{-1} $$

We know that the top-right entry of $A^n$ is $F_n$. If we multiply out $P \begin{bmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{bmatrix} P^{-1}$ and look specifically at that top-right entry, the $2$'s cancel out beautifully, yielding **Binet's Formula** for the $n$-th Fibonacci number:

$$ F_n = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right) $$

### What does this formula tell us?
1. **$O(1)$ Computation:** You don't need to run a loop or compute all previous Fibonacci numbers to find the 1,000th one. You can just plug $n=1000$ directly into this formula.
2. **The Golden Ratio Connection:** Because $\left| \frac{1 - \sqrt{5}}{2} \right| \approx 0.618$, which is less than $1$, the second term $\left( \frac{1 - \sqrt{5}}{2} \right)^n$ rapidly shrinks to $0$ as $n$ gets larger. Therefore, the sequence is almost entirely driven by the first term (the Golden Ratio). This proves mathematically why the ratio between consecutive Fibonacci numbers approaches $\phi$. As $n$ approaches infinity, the second eigenvector's influence completely vanishes!