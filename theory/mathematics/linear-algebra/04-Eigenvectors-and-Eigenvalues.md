# Chapter 4: Eigenvectors and Eigenvalues

## 1. Intuition: The "Stay" Vectors

In most linear transformations, vectors are knocked off their original span (the line they live on). **Eigenvectors** are the special exceptions—they are the vectors that remain on their original span during a transformation.

*   **Eigenvector:** The direction that stays the same. The vector only stretches or squashes along its line.
*   **Eigenvalue ($\lambda$):** The factor by which the eigenvector is scaled.
    *   $\lambda = 2$: The vector doubles in length.
    *   $\lambda = 0.5$: The vector is halved.
    *   $\lambda = -1$: The vector flips to the opposite side but stays on the same line.

Think of it as the "natural axes" of a transformation. If you can describe a transformation in terms of its eigenvectors, you are seeing the "bones" of the math.

---

## 2. Mathematical Formulation: The Characteristic Equation

To find eigenvectors, we start with the core definition:
$$ A\vec{v} = \lambda\vec{v} $$

We can rewrite this as:
$$ (A - \lambda I)\vec{v} = \vec{0} $$

For a non-zero vector $\vec{v}$ to satisfy this, the matrix $(A - \lambda I)$ must squash space into a lower dimension (it must be non-invertible). Therefore, its determinant must be zero:

$$ \det(A - \lambda I) = 0 $$

This is the **Characteristic Equation**. Solving this polynomial gives you the eigenvalues. Once found, you plug each $\lambda$ back into $(A - \lambda I)\vec{v} = \vec{0}$ to solve for the coordinates of the eigenvectors.

---

## 3. Example: $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$

**Step 1: Find Eigenvalues**
$$ \det \begin{bmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{bmatrix} = (3-\lambda)(2-\lambda) - 0 = 0 $$
$$ \lambda_1 = 3, \lambda_2 = 2 $$

**Step 2: Find Eigenvector for $\lambda_1 = 3$**
$$ (A - 3I)\vec{v} = \begin{bmatrix} 0 & 1 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies y = 0 $$
The eigenvector is any vector on the **X-axis** (e.g., $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$).

**Step 3: Find Eigenvector for $\lambda_2 = 2$**
$$ (A - 2I)\vec{v} = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies x + y = 0 \implies x = -y $$
The eigenvector is the line **$y = -x$** (e.g., $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$).

---

## 4. How many Eigenvalues do we get?

The number of eigenvalues depends on the **dimensions** of the matrix and the **nature** of the transformation.

### Intuition
If you think of eigenvectors as the "natural axes" of a transformation, an $n \times n$ matrix can have **up to $n$** of these axes.
*   **2D Space:** Usually 2 eigenvalues.
*   **3D Space:** Usually 3 eigenvalues.

### Mathematical Formulation
The number of eigenvalues is determined by the **Fundamental Theorem of Algebra**. For an $n \times n$ matrix, the Characteristic Equation $\det(A - \lambda I) = 0$ is a **polynomial of degree $n$**. A polynomial of degree $n$ always has **exactly $n$ roots** (counting repeats and including complex numbers).

### Common Scenarios

1.  **Distinct Real Eigenvalues:** (See the example in Section 3).

2.  **Complex Eigenvalues:** Common in **rotations**. Since no real line stays put during a 90° rotation, the math results in complex numbers. 

3.  **Repeated Eigenvalues: The Case of "Missing" Eigenvectors**
    Even if an eigenvalue is repeated, you may not get multiple eigenvector directions.
    
    *   **Uniform Scaling ($2\times$):** $A = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$
        *   **Characteristic Eq:** $\det \begin{bmatrix} 2-\lambda & 0 \\ 0 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 = 0 \implies \lambda = 2, 2$.
        *   **Evidence (The Proof):** For a vector to be an eigenvector, it must satisfy $A\vec{v} = \lambda\vec{v}$. Let's test an arbitrary vector $\begin{bmatrix} x \\ y \end{bmatrix}$:
            $$ \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + 0y \\ 0x + 2y \end{bmatrix} = \begin{bmatrix} 2x \\ 2y \end{bmatrix} = 2 \begin{bmatrix} x \\ y \end{bmatrix} $$
            Since this holds true for **any** values of $x$ and $y$, every single vector in the plane remains on its span. We have a repeated eigenvalue ($\lambda=2$) with **infinitely many** eigenvector directions.
        
    *   **Shear Matrix (Defective):** $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$
        *   **Characteristic Eq:** $(1-\lambda)^2 = 0 \implies \lambda = 1, 1$ (Repeated).
        *   **Finding Vectors:** $(A - 1I)\vec{v} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies y = 0$.
        *   **Evidence:** The ONLY eigenvector is the X-axis. Even though the math "expected" two roots, the transformation physically collapsed the second direction onto the first. This matrix is **not diagonalizable**.

---

## 5. ML Connection

*   **Principal Component Analysis (PCA):** PCA works by finding the eigenvectors of the data's covariance matrix. These eigenvectors (Principal Components) represent the directions of maximum variance.
*   **PageRank:** Google's original algorithm treats the internet as a giant matrix. The most "important" pages are the components of the eigenvector associated with the largest eigenvalue of that matrix.
*   **Graph Theory:** Eigenvalues of graph Laplacians are used in spectral clustering to find communities in networks (like social groups or molecular structures).

---

## 5. Edge Cases / Failure Modes

*   **Rotation (No Real Eigenvectors):** A pure 90° rotation knocks every vector off its span. The characteristic equation will have no real roots (only complex numbers).
*   **Shear (Missing Eigenvectors):** In a shear transformation, multiple eigenvectors might "collapse" into one. These matrices are not diagonalizable.
*   **Identity Matrix:** Every single vector is an eigenvector with $\lambda = 1$. Space isn't "changed" in any specific direction.

---

[Previous Chapter](./03-Change-of-Basis.md) | [Next Chapter](./05-Eigenbasis-and-Diagonalization.md)
