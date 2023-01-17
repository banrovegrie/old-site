## Linear Operators and Matrices

---

$$
⁍
$$

Now, see a linear operator is just a matrix. Suppose $A: V \to W$ and $|v_1\rangle, |v_2\rangle, ..., |v_m\rangle$ are basis of $V$ and $|w_1\rangle, |w_2\rangle, ..., |w_n\rangle$ is a basis of $W$ then,

$$
A|v_j\rangle = \Sigma_i A_{ij}|w_i\rangle 
$$

## Inner Products

---

Ok so imagine an operation $(\_ ,\_): V\times V \to \mathbb{C}$ such that the following shit holds ok?

1. $(|v\rangle, \Sigma_i \lambda_i|w_i\rangle) = \Sigma_i\lambda_i(|v\rangle, |w_i\rangle)$
2. $(|v\rangle, |w\rangle) = (|w\rangle, |v\rangle)^*$
3. $(|v\rangle, |v\rangle) \geq 0$ and $= 0$  iff $|v\rangle$

In finite dimensions, inner product space i.e., vector spaces equipped with inner prducts for all $|v\rangle \in$  vector space $=$  Hilbert Space

Consider $|i\rangle\ \&\ |j\rangle$ to be orthonormal basis, we have —

$$
\langle v|w \rangle = (\Sigma_i v_i|i\rangle, \Sigma_jw_j|j\rangle) = \Sigma_i \Sigma_j v_i^*w_j\delta_{ij} = \Sigma_iv_i^*w_i = |v\rangle^\dagger |w\rangle
$$

## Norm of a vector

---

$$
||v|| = \sqrt{\langle v|v \rangle}
$$

We can say that $|v\rangle$ is normalized iff $||v|| = 1$. 

A set of $|a_i\rangle$ vectors is orthonormal if $\langle a_i|a_j \rangle = \delta_{ij}$ i.e., $\forall\ i \neq j\ \langle a_i|a_j \rangle = 0$ and $\langle a_i|a_j \rangle = 1\ \forall\ i=j$.

## Gram Schmidt: for orthonormal basis

---

$$
|v_{k+1}\rangle =  \frac{|w_{k+1}\rangle - \Sigma_{i=1}^k \langle v_i | w_{k+1}\rangle |v_i\rangle}{|||w_{k+1}\rangle - \Sigma_{i=1}^k \langle v_i | w_{k+1}\rangle |v_i\rangle||},\ 
|v_1\rangle = |w_1\rangle/|||w_1 \rangle||
$$

## Outer Product

---

$$
|w\rangle \langle v|(|v'\rangle) = |w\rangle |v\rangle^\dagger |v'\rangle = |w\rangle \langle v|v' \rangle = \langle v|v' \rangle |w\rangle 
$$

- From this notion we obtain the completeness relation, $\Sigma_i |i\rangle \langle i| = I$.
- $A = I_wAI_v = \Sigma_{ij} |w_j\rangle\langle w_j|A|v_i\rangle\langle v_i| = \Sigma_{ij} \langle w_j|A|v_i\rangle|w_j\rangle\langle v_i|$
- Cauchy Schwarz: $\langle v|v \rangle \langle w|w \rangle \geq \langle v|w \rangle \langle w|v \rangle = |\langle v|w \rangle|^2$

## Hilbert Space

---

A Hilbert Space $\mathcal{H}$ is complete which means that every Cauchy sequence of vectors admits in the space itself. Under this hypothesis there exist Hilbert bases also known as complete orthonormal systems of vectors in $\mathcal{H}$.

For any orthonormal basis of $\mathcal{H}$, we have the following.

$$
\text{Orthonormality} \equiv\langle \psi_i|\psi_j\rangle = \delta_{ij}\\
\text{Completeness} \equiv\sum_{i} |\psi_i\rangle\langle\psi_i| = I
$$

## Eigenvectors and Eigenvalues

---

Under a given linear transformation $A$, $A|v\rangle = \lambda|v\rangle$  where $\exists\ |v\rangle$  s.t. they do not get shifted off their span.

All such vectors are referred as eigenvectors and $(A - \lambda I)|v\rangle = 0 \implies det|A-\lambda I| = 0$ gives all possible eigenvalue.

If all $λ_i ≥ 0$, it is positive semidefinite and if they are $> 0$, it is positive definite.

## Eigenspace

---

It is the space of all vectors with a given eigenvalue $\lambda$. When an eigenspace is more than one dimensional, we call it degenerate.

## Adjoints and Hermitian

---

Suppose $A: V \to V$ then $\exists\ A^\dagger: V \to V$ such that $\forall\ \vert v\rangle,\ \vert w\rangle \in V$ we have,

$$
(\vert v\rangle, A\vert w\rangle) = (A^\dagger \vert v\rangle, \vert w\rangle)
$$

This operator is called as the adjoint or Hermitian conjugate of the operator $A$.

$$
(\vert v\rangle, A\vert w\rangle) = \langle v\vert A\vert w\rangle = \bold{v}^\dagger A\bold{w} = (A^\dagger\bold{v})^\dagger\bold{w} = (A^\dagger\vert v\rangle, \vert w\rangle)
$$

- We have, $(AB)^\dagger = B^\dagger A^\dagger$
- $\vert v\rangle^\dagger = \langle v\vert$

### Some defintions

- Normal matrices: $AA^\dagger = A^\dagger A$
- Hermitian matrices: $A^\dagger = A$
- Unitary matrices: $AA^\dagger = I$
- A normal matrix is Hermitian if and only if it has real eigenvalues.
- If $\langle x| A|x\rangle \geq 0, \forall\ |x\rangle$ then $A$ is positive semi-definite and has positive eigenvalues.

### Some properties

- If a Hermitian matrix has positive eigenvalues then it is positive semi-definite.
- If $M = AA^\dagger$ then it is both Hermitian and positive semi-definite.
- All positive semi-definite operators are Hermitian, by definition.

## Spectral Decomposition

---

Definition: A linear operator is *diagonalizable* if and only if it is *normal*.

Some notes and derivation regarding the above:

$A\vec{v} = \lambda\vec{v} = \Sigma_i \lambda_{ij}\vec{q_i}$  where $q_i$'s are linearly independent eigenvalues of $A$.

$AQ = Q\Lambda$ where $Q = 
\begin{bmatrix}
    q_1&q_2 &\ldots&q_n
\end{bmatrix}
\implies A = Q{\Lambda}Q^{-1}$  

$A = IAI = (P+Q)A(P+Q) = PAP + QAP + PAQ + QAQ\\ \implies A = \lambda{P^2} + 0 + 0 + QAQ\\ \implies A = \lambda{P^2} + QAQ$

## Matrices and Vectors

---

In the following statements we are dealing with $\{\vert i\rangle\}$  as a ***orthonormal*** basis set.

$$
I = \Sigma \vert i\rangle\langle i\vert\\
\vert \psi \rangle = \Sigma \sigma_i\vert i\rangle, \text{ where } \sigma_i = \langle i\vert \psi\rangle\\

$$

Now, to represent a operator or linear transformation as matrix in orthonormal basis.

$$
A_{ij} = \langle i\vert A\vert j\rangle\\
A = \Sigma_{i, j} \langle i\vert A\vert j\rangle \vert i\rangle \langle j\vert\\
\text{tr}(A) = \Sigma_i \langle i\vert A\vert i\rangle
$$

Now diagonalization for any ***normal*** matrix.

$$
M = \Sigma_i \lambda_i \vert i\rangle \langle i\vert = \Sigma_i \lambda_i P_i,\ \text{where}\ P_i^\dagger = P_i\\
f(M) = \Sigma_i f(\lambda_i) \vert i\rangle \langle i\vert
$$

where $\lambda_i$ are eigenvalues of $M$ under a given orthonormal basis set $\{\vert i\rangle\}$ for vector space $V$, each $\vert i \rangle$ is an eigenvector of $M$ with eigenvalue $\lambda_i$.

If $M$ is ***Hermitian***, all eigenvalues $(\lambda_i\text{ s})$ are real.

## Tensor Products

---

![Linear%20Algebra%2061e9244dd7684d59a266b9dc61c698b3/Untitled.png](Math%20and%20Formal%20Systems/images/Linear%20Algebra%2061e9244dd7684d59a266b9dc61c698b3/Untitled.png)

- $z\vert{vw}\rangle = (z\vert{v}\rangle) \otimes (\vert{w}\rangle) =(\vert{v}\rangle) \otimes (z\vert{w}\rangle)$
- $(\vert v_1 \rangle + \vert v_2 \rangle) \otimes \vert w \rangle = \vert{v_1w}\rangle + \vert{v_2w}\rangle$
- $\vert v \rangle \otimes (\vert w_1 \rangle + \vert w_2 \rangle) = \vert{vw_1}\rangle + \vert{vw_2}\rangle$
- $\vert \psi \rangle^{\otimes^k} = \vert \psi \rangle \otimes \ldots \otimes \vert \psi \rangle \text{ k times}$
- $(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger$

### Linear Product

$A\otimes{B}$ forms the linear operator that acts on $V\otimes W$ vector space givern that $A$ acts on $V$ and $B$ acts on $W$.

$$
(A\otimes B)(\Sigma_{i} a_i\vert v_i\rangle \otimes \vert w_i \rangle) = \Sigma_{i} a_iA\vert v_i\rangle \otimes B\vert w_i \rangle
$$

### Inner Product

$$
(\Sigma_{i} a_i\vert v_i\rangle \otimes \vert w_i \rangle, \Sigma_{i} a_j\vert v'_j\rangle \otimes \vert w'_j \rangle) = \Sigma_{ij} a_i^*b_j \langle v_i\vert v'_j\rangle\langle w_i\vert w'_j\rangle
$$

## Trace

---

Properties of trace are given below as follows.

- $\text{tr}(A) = \Sigma_i A_{ii}$
- $\text{tr}(A) = \Sigma_i \langle i\vert A\vert i\rangle$ for orthonormal basis
- $\text{tr}(AB) = \text{tr}(BA)$
- $\text{tr}(zA+B) = z\cdot \text{tr}(A) + \text{tr}(B)$

The above properties yield certain implications as follows.

- $\text{tr}(UAU^\dagger) = tr(A)$
- $\text{tr}(A\vert \psi\rangle\langle\psi\vert) = \Sigma_i \langle i\vert A\vert \psi\rangle\langle\psi\vert i \rangle$
- $\text{tr}(A) = \sum_i \lambda_i$, $\text{det}(A) = \prod_i \lambda_i$ with algebraic multiplicities

$$
||A|| = \sqrt{tr (A^\dagger A)}
$$

## Partial Trace

---

Entanglement excludes the possibility of associating state vectors with individual subsystems. Therefore, we introduce density matrices and the corresponding idea of reduction preformed with partial trace.

$$
\text{tr}(A \otimes B) = \text{ tr}(A) \cdot \text{tr}(B)
$$

$$
\rho_{AB} : \mathcal{H_A}\otimes\mathcal{H_B} \xrightarrow{\text{ tr}_B} \rho_A : \mathcal{H_A}
$$

$$
\text{ tr}_B(AB) = A \text{ tr}(B)
$$

## Hilbert-Schimdt Inner Product

---

$L_v$ forms the vector space of operators over the Hilbert space $V$. Then, we can show that $L_v$  is also a Hilbert space with ****$\text{tr}(A^\dagger B)$ as the inner product operator on $L_v \times L_v$.

Also, we have $div(L_v) = dim(V)^2$.

## Commutator and Anti-commutator

---

$$
[A, B] = AB - BA\\
\{A, B\} = AB + BA
$$

## Theorem of Simultaneous Diagonalization

---

Suppose $A$ and $B$ are both Hermitian matrices, then $[A, B] = 0$ iff $\exists$ orthonormal basis such that both $A$ and $B$ are diagonal with respect to that basis.

## Polar Value Decomposition

---

If $A$ is any linear operator and $U$ is a unitary then $J, K$ are positive operators, such that

$$
A = UJ = KU, \text{ where } J = \sqrt{A^\dagger A} \text{ and } K = \sqrt{AA^\dagger}
$$

Moreover, if $A^{-1}$ exists, then $U$ is unique.

## Singular Value Decomposition

---

![Untitled](Math%20and%20Formal%20Systems/images/Linear%20Algebra%2061e9244dd7684d59a266b9dc61c698b3/Untitled%201.png)

SVD in general is given as follows. 

$$
{U\Sigma V^{T}}
  
$$

It generalizes the [eigen decomposition](https://en.wikipedia.org/wiki/Eigendecomposition) of a square [normal matrix](https://en.wikipedia.org/wiki/Normal_matrix) with an orthonormal eigen basis to any $m\times n$ matrix.

${\Sigma}$ is an ${m\times n}$ [rectangular diagonal matrix](https://en.wikipedia.org/wiki/Rectangular_diagonal_matrix) with non-negative real numbers on the diagonal (called singular values).

Corollary: If $A$ is a square matrix and $\exists\ U, V$ unitaries then $D$ is a diagonal matrix, such that

$$
A = UDV
$$

where $D$ has non-negative values.

Corollary: If $A$ has non-negative eigenvalues then, $A = U^\dagger DU$ is possible where $D$ has non-negative values.

- If $A$ is square both SVD and EVD exist but might not be same.
- If $A$ is a square symmetric matrix both SVD and EVD exist and are equivalent.
- If $A$ is non-square only SVD is possible.

## Rank of a matrix

---

Rank $=$ number of dimensions in column space.

- The row rank is the largest number of rows of $A$ that constitute a linearly independent set.
- The column rank is the largest number of columns of $A$ that constitute a linearly independent set. Moreover, column-rank $=$  row-rank for $A \in \mathbb{R}^{m \times n}$.

$$
rank(A \in \mathbb{R}^{m \times n}) \leq min(m, n)
$$

Matrix is called full rank if equality holds.

- $rank(A^T) = rank(A)$
- $rank(AB) ≤ min(rank(A), rank(B))$
- $rank(A + B) ≤ rank(A) + rank(B)$

## Projection and Spaces

---

$$
Proj(y ; A) = argmin_{v ∈R(A)} ||v − y||_2 = A(A^T A)^{−1} A^T y
$$

- $\mathcal{N} (A) = \{x ∈ \mathbb R^n : Ax = 0\}$ denotes all vectors in $\mathbb R^n$ that land at the origin after transformation. It is also called kernel.
- $\mathcal R(A) = \{v ∈ \mathbb R^m : v = Ax,~x ∈ \mathbb R^n \}$ denotes the space spanned by the transformed basis vectors in $\mathbb R^n$.
- $\mathcal R(A^T)$ and $\mathcal N (A)$ are orthogonal spaces which together span $\mathbb R^n$.

Determinant $\neq 0$ implies that the matrix has an inverse.

## Quadratic Forms

---

Reminder: we are in real $\mathbb R$ space.

$$
x^TAx = (x^TAx)^T = x^T(\frac 1 2 A + \frac 1 2 A^T)x
$$

## Moore-Penrose Pseudoinverse

---

$$
A^{\text{left inv}} = (A^\dagger A)^{-1}A^\dagger
$$

$$
A^{\text{right inv}} = A^\dagger(AA^\dagger)^{-1}
$$

This is a pseudo inverse formalism with left and right inverses.

$$
A^{\text{left inv}}A = I\\
AA^{\text{right inv}} = I
$$

## Row Echelon Forms

---

A matrix is in row echelon form if:

- All rows consisting of only zeroes are at the bottom.
- The leading coefficient (also called the pivot) of a nonzero row is always strictly to the right of the leading coefficient of the row above it.

A matrix is in reduced row echelon form if:

- It is in row echelon form.
- The leading entry in each nonzero row is a 1 (called a leading 1).
- Each column containing a leading 1 has zeros in all its other entries.