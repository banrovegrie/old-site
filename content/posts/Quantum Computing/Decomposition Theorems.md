## Spectral Decomposition
---
Any normal operator $M$ on a vector space $V$ is diagonal with respect to some orthonormal basis for $V$. 

Conversely, any diagonalizable operator is normal.

### Proof

$$
M = (P+Q)M(P+Q) = PMP+QMP+PMQ+QMQ = PMP + QMQ
$$

Now we have

$$
QM = QM(P+Q) = QMQ \text{ and } QM^\dagger = QM^\dagger Q$$$$
QMQQM^\dagger Q = QMM^\dagger Q = QM^\dagger MQ = QM^\dagger QQMQ
$$

Thus, if $M$ is normal then $M = PMP + QMQ$ where $PMP = \lambda P^2 = \lambda P$ and thus is diagonalizable wrt orthonormal basis for $P$. Similarly, $QMQ$ is also diagonalizable wrt some orthonormal basis for $Q$.

Thus, $M$ is diagonalizable for orthonormal basis of the entire vector space.

$$
M = \Sigma \lambda_i \vert i\rangle \langle i \vert = \Sigma \lambda_i P_i
$$

## Polar Value Decomposition
---
Let $A$ be a matrix on vector space $V$. Then there exists unitary $U$ and positive operators $J$ and $K$ such that, $A= UJ=KU$ where the unique positive operators shall satisfy the equations $J \equiv \sqrt{A^\dagger A}$ and $K \equiv \sqrt{AA^\dagger}$.

Moreover, if $A$ is invertible then $U$ is unique.

## Singular Value Decomposition
---
Let $A$ be a square matrix. Then there exist unitary matrices $U$ and $V$, and a diagonal matrix $D$ with non-negative entries such that $A = UDV$.

The diagonal elements of $D$ are called the singular values of $A$.

### Proof

From polar value decomposition we have, $A = SJ = STDT^\dagger = (ST)D(T^\dagger) = UDV$.