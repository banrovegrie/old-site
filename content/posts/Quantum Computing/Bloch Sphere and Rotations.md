We can represent any $\rho$  (density matrix) as $\frac 1 2 (I + \vec{r}\cdot\vec{\sigma})$

## Single Qubit Operations

---

$$
e^{iAx} = cos(x) + isin(x)A
$$

Thus, $R_x(\theta) = e^{i\theta X/2}$, $R_y(\theta) = e^{i\theta Y/2}$ and $R_z(\theta) = e^{i\theta Z/2}$.

$$
R_{\hat{n}}(\theta) = e^{i\theta \hat n\cdot\vec\sigma/2}
$$

In general, we have the above equation where $\vec\sigma = X\hat i + Y\hat j + Z\hat k$.

## Some Algebra

---

$$
X^2 = Y^2 = Z^2 = -iXYZ = I
$$

$$
R_{\hat n}(\alpha) = R_z(\phi)R_y(\theta)R_z(\alpha)R_y(-\theta)R_z(-\phi)\\
= R_z(\phi)R_y(\theta)R_z(\alpha)R_y(\theta)^\dagger R_z(\phi)^\dagger
$$

## Theorems

---

1. Any arbitrary single qubit unitary operator can be written in the form $U = e^{i\alpha}R_{\hat n}(\theta)$.
2. Suppose $U$ is a unitary operation over a single qubit then $\exists\ \alpha, \beta, \gamma, \delta$ such that $U = e^{i\alpha}R_{\hat n}(\beta)R_{\hat m}(\gamma)R_{\hat n}(\delta)$.
3. There exists unitaries $A, B, C$ for any given unitary $U$ such that $ABC = I$ and $U = e^{i\alpha} AXBXC$.