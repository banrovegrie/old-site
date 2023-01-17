## Postulate
---
Quantum Measurements are descrivbed by a collection of  measurement operators $\{M_m\}$ with $p(m)= \langle \psi | M_m^\dagger M_m | \psi \rangle,\ \sum{p(m)} = 1$.

$$
\vert \psi \rangle \xrightarrow{\text{on   measurement}} \frac{M_m \vert \psi \rangle}{\sqrt{p(m)}}
$$

If $M_i = |i\rangle \langle i|,\ \forall i$  then we are measuring in a computational basis.

## Non-distinguishability of arbitrary states
---
We cannot distinguish any two arbitrary non-orthogonal quantum states.

Proof: Let $|\psi_1\rangle$ and $|\psi_2\rangle$ be two non-orthogonal states. 

Then $\exists\ E_1, E_2$ such that $E_1 = \sum_{j:f(j) = 1} M_j^\dagger M_j$ and similarly $E_2$ then $\langle \psi_1 | E_1 | \psi_1 \rangle = 1$ and $\langle \psi_2 | E_2 | \psi_2 \rangle = 1$.

Thus, $\sqrt{E_2}| \psi_1\rangle = 0$ and let $\psi_2 = a\psi_1 + b \phi$ where $\psi$ and $\phi$ are orthogonal.

$$
\langle \psi_2 | E_2 \psi_2 \rangle = |\beta|^2 \langle \psi_2 | \phi \psi_2 \leq  |\beta|^2 < 1
$$

Hence, proved by contradiction.

## Projective Measurements
---
We can use projective measurement formalism for any general measurement too.

In case of projective measurements, $M = \sum mP_m$ and $p(m) = \langle \psi | P_m | \psi \rangle$.

$$
\vert \psi \rangle \rightarrow \frac{P_m \vert \psi\rangle}{\sqrt {p(m)}}
$$

$$
E(M) = \sum mp(m) = \langle \psi | M | \psi \rangle = \langle M\rangle
$$

$$
\Delta(M) = \sqrt{\langle M^2\rangle - \langle M \rangle^2}
$$

Here, $E(M)$ is expectation and $\Delta(M)$ is standard deviation or the square root of variance.

## POVM Measurements
---
POVM Measurements are a formalism where only measurement statistics matters.

$$
\{E_m\} \rightarrow \sum{E_m} = I,\ p(m) = \langle \psi | E_m |\psi \rangle
$$

Here, each of $E_m$ are hermitian.

## Global Phase doesn't matter
---
We say $e^{i\theta} |\psi\rangle \equiv |\psi\rangle$ but why? Because, $\langle \psi | M_m^{\dagger}M_m | \psi \rangle = \langle \psi \vert e^{-i\theta}M_m^\dagger M_m e^{i\theta}\vert \psi \rangle$.

However, be aware that the global phase is quite different from the relative phase.