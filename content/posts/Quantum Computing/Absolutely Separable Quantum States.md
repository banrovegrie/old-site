## Introduction

Now that we know the definition of separable and entangled states, we will move on to the definition of absolutely separable quantum states and describe the problem of absolute seoarability.

## The Problem

The absolutely separability problem, or the separability from spectrum problem, calls for the characterization of states $\rho \in M_m \otimes M_n$ such that for all unitary matrices $U \in M_m \otimes M_n$ we have $U\rho U^\dagger$ as separable.

This problem is equivalent to asking which sets of real numbers $\{\lambda_1, \lambda_2, \ldots, \lambda_{mn}\}$ are such that every state $\rho \in M_m \otimes M_n$ with eigenvalues $\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_{mn} \geq 0$ is separable.

![Untitled](Quantum%20Computing/images/Absolutely%20Separable%20Quantum%20States/Untitled.png)

## Convexity

Similar to the case of separable quantum states and all quantum states, absolutely separable quantum states are also convex in nature.

Let $\alpha_i \geq 0\ \forall\ i \in \{1, 2, \ldots, n\}$ and $\sum_{i = 1}^{n} \alpha_i = 1$ then, if $\rho_i$ is absolutely separable  $\forall\ i \in \{1, 2, \ldots, n\}$ then, $U\left(\sum_{i = 1}^n \alpha_i \rho_i\right)U^\dagger = \sum_{i = 1}^n \alpha_i U\rho_i U^\dagger = \sum_{i = 1}^n \alpha_i \rho_i'\ \forall\ U$.

Now since $\rho_i$ is absolutely separable, $\rho_i'$ is also separable and hence $\sum_{i = 1}^n \alpha_i \rho_i'$ is also separable. This holds for all $U$. Thus, $\sum_{i = 1}^n \alpha_i \rho_i$ is absolutely separable as well.

Hence, absolutely separable states form a convex set.

## Criterions for Absolute Seprarability

Remember the conditions for characterizing separable and entangled states? More specifically, the PPT (positive partial trace) condition. A similar criterion can also be constructed for absolutely separable states.

In case of the PPT criterion, it was necessary and sufficient when ${\displaystyle {\textrm {dim}}({\mathcal {H}}_{A}\otimes {\mathcal {H}}_{B})\leq 6}$
  . Here, $\mathcal{H}_A$ and $\mathcal{H}_B$ are defined as follows. If $\rho$ is the required separable state then we can represent $\rho =\sum p_{i}\rho _{i}^{A}\otimes \rho _{i}^{B}$, such that $\rho_i^A \in \mathcal{H}_A$ and $\rho_i^B \in\mathcal{H}_B$. In other words, the PPT criterion is necessary in case of all Hilbert spaces but holds to be sufficient and necessary for $2\otimes 2$ and $2\otimes 3$ Hilbert spaces.

However in the case of absolutely separability, the absolute PPT criterion holds to be necessary and sufficient for all $2\otimes d$ Hilbert spaces. So what is the absolute PPT criterion?

## Absolute PPT

For each $m, n \in N$, there exists a finite family of linear matrix inequalities (LMIs) with the property that $\rho \in M_m \otimes M_n$ is absolutely PPT if and only if its eigenvalues $\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_{mn}$ satisfy each of the LMIs.

In the case of $m = 2$ case, the LMI that determines absolute PPT is as follows.

$$
L_1 = \begin{bmatrix}2\lambda_{2n}& \lambda_{2n - 1} - \lambda_1\\
\lambda_{2n - 1} - \lambda_1& 2\lambda_{2n - 2}
\end{bmatrix} \geq 0
$$

This is easily seen to be equivalent to the inequalities $\lambda_1 \leq \lambda_3 + 2 \sqrt{\lambda_2\lambda_4}$ when $n = 2$ and $\lambda_1 \leq \lambda_5 + 2\sqrt{\lambda_4 \lambda_6}$ when $n = 3$.

In general, for a given $m, n$ we use $L_1, L_2, \ldots$ to denote the matrices of eigenvalues whose positive semi-definiteness determine absolute PPT. For each $L_i$ of size $\min\{m, n\} \times \min\{m, n\}$, the diaginal entry of each $L_i$ is $2$ times one of the $\lambda_j$’s and each off diagonal entry is the difference of the two $\lambda_j$’s.