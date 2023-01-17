## Definitions

$$
PSDP: \min_{P\in S^n_{\geq}} ||F - PG||
$$

$$
SP: \min_{S\in S^n} ||F - SG||
$$

Here, $F, G \in R^{\ n\times m}$.

## Background

- $\tilde{S}$ denotes a minimizer for the SP problem.
- $\tilde{P}$ denotes a minimizer for the PSDP problem.
- $\tilde{S}GG'+ GG'\tilde{S} = FG' + GF' = Q$
- When  $rank(G) = n$, a sufficient condition for $\tilde{S}$ to be in $S^n_{\geq}$ is that $Q \in S^n_{\geq}$.
- A sufficient condition for $\tilde{S}$ to be in $S^n_{\geq}$ is that $FG' \in S^m_{\geq}$.
- $rank(G) = n$ is also necessary and sufficient for uniqueness of minimizers in case of PSDP.

## Previous Approches

- The objective function and the feasible set in case of PSDP are both convex.
- We can use convex optimization which directly exploits the convexity of $S^n_{\geq}$.
- Solutions involve finite convergence towards global minimas bringing the approximate minimizer arbitrarily close to the unique global minimizer.

## Approach of this paper

$$
PSDP^*: \min_{E \in R^{n\times n}} ||F - E'EG||
$$

$$
\tilde{P}_{\text{global}} = \tilde{E}_{\text{local}}'\tilde{E}_{\text{local}}
$$

Algorithm ideas:

- Steepest descent (doesn’t converge, proven)
- Newton’s algorithm (modified, superior than known convex programs of that time)
- Where do we obtain the data? Take stuff, perturb by errors to make sure that $\tilde{S} \neq \tilde{P}$.

Newton’s method:

$$
x_{k + 1} = x_k - \frac{f'(x_k)}{f''(x_k)}
$$

- Has quadratic convergence.
- Can find complex zeroes.
- If you have $n$ variables, then $n^2$ operations is needed to find $\nabla^2 f$ (Hessian) and $n^3$  operations to find the inverse of the Hessian.

Quasi Newtown method:

$$
GD:\ \ \ \ x_{k + 1} = x_k - \eta \cdot I\cdot \nabla f(x_k)\\
NM:\ \ \ \ x_{k + 1} = x_k - \eta \cdot \frac{1}{\nabla^{2}f(x_k)}\cdot \nabla f(x_k)\\
QNM:\ \ \ \ x_{k + 1} = x_k - \eta \cdot H_k\cdot \nabla f(x_k)
$$

A good choice for $H$  can be the following. This is the BFGS method and $H_k$ holds curvature information. Key idea is to match curvature along trajectory.

$$
H = \begin{bmatrix}
1& 1\\
\end{bmatrix}
$$

## Algorithm

![Untitled|center|400](Math%20and%20Formal%20Systems/images/PSDP%20Problem%206cabea65c10e4ffda66cca3275886bf0/Untitled.png)

- $L(E) = E'EGG' +GG'E'E - Q$
- $D_i = E_i-L(E_i)$
- $f(E) = \frac{1}{2}tr(F’F + (E’E)^2GG’ -E’EQ)$
- Setting all the negative eigenvalues in $L(E_i)$ spectral form to zero results in $L(E_i)_{>}$ which is required in the algorithm.

![Untitled|center|400](Math%20and%20Formal%20Systems/images/PSDP%20Problem%206cabea65c10e4ffda66cca3275886bf0/Untitled%201.png)

- $v(.)$  denotes vertical stacking.
- $\mathcal{N}$ denotes scaling such that $\mathcal{N}(E_i) = \tilde{\alpha} E_i$ where $\tilde\alpha$ is given as follows.

$$
\tilde\alpha = \max \{0, \frac{tr(E_i'E_iQ)}{\sqrt{2 tr(E_i'E_iE_i'E_iGG')}}\}
$$

The linear computations of step 3 may be performed by a variety of methods as may the steplength computation of step 4.