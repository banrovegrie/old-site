## Introduction
---
We can represent a system as an ensemble of pure states $\{p_i, \psi_i\}$. Now, if you have exact knowledge of the system then it is for sure in a pure state, i.e., $\rho = |\psi\rangle\langle\psi|$. However, if we have classical uncertainty amongst the possible states. The system can be represented as a mixed state $\rho = \sum_{i} p_i\psi_i$ where the probabilities $p_i$ are classical in nature.

This formulation helps us a lot in dealing with quantum information, noisy systems and helps us represent measurements better, as well. Why? Because it provides a convenient means for describing quantum systems whose state is not completely known.

## Postulates in Density Matrices formulation
---
1. Isolated physical system is given by its density matrix operating on a certain Hilbert space.
2. Evolution of a closed quantum system is given by a unitary transformation as $\rho \xrightarrow{U} U\rho U^\dagger$.
3. The state space of a composite physical system is the tensor product of the state spaces of the component systems.
    
    $$
    \rho = \rho_1\otimes...\otimes\rho_n
    $$
    
4. Quantum measurements are described by a collection $\{M_m\}$ of measurement operators acting on the state space of the system. 
    
    Probability that upon measurement the outcome is $m = p(m) = tr(M_m^\dagger M_m\rho)$ and the state of the system becomes as follows.
    
    $$
    \rho \xrightarrow{\text{on measuring}} \frac{M_m\rho M_m^\dagger}{p(m)}
    $$
    
    Measurement operators also follow the completeness equation, $\sum_m M_m^\dagger M_m = I$.
    

## Properties
---
Theorem 1: An operator $\rho$ is a density operator if and only if it is both positive semi-definite $(\rho = \rho^\dagger$ and non-negative eigenvalues$)$ and $tr(\rho) = 1$.

Converse is easy to prove. If an operator is both positive and has trace as one, then it shall have a spectral decomposition of the form $\sum_i\lambda_i|i\rangle\langle i|$.

For the direct proof, let us consider $tr(\rho) = \sum_i p_i tr(|\psi_i\rangle\langle\psi_i|) = 1$.

Theorem 2: The sets $|\tilde\psi\rangle$ and $|\tilde\phi\rangle$ generate the same density matrix if and only if,

$$
|\tilde\psi_i\rangle = \sum_j u_{ij} |\tilde\phi_j\rangle
$$

where $u_{ij}$ is a unitary matrix of complex numbers, with indices $i$ and $j$, and we 'pad' whichever set of vectors $|\tilde\psi_i\rangle$ or $|\tilde\phi_j\rangle$ is smaller with additional vectors $0$ so that the two sets have the same number of elements.

As a consequence of the theorem, note that $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i| = \sum_j q_j |\phi_j\rangle\langle\phi_j|$ if and only if we have the following as true for some unitary matrix $u_{ij}$.

$$
\sqrt p_i |\psi_i\rangle = \sum_j u_{ij} \sqrt q_j |\phi_j\rangle
$$

Theorem 3: If $\rho$ is a density operator, then $\rho$ is a pure state if and only if $tr(\rho^2) = 1$ and mixed state if and only if $tr(\rho^2) < 1$.

Theorem 4: Observable $M$ has expectation $\sum_x \langle \psi_x|M|\psi_x\rangle = tr(M\rho)$.

## Reduced Density Operator
---
This is the single-most important application of density operator formulation is the existence of reduced density operator. It is defined as follows.

$$
\rho_A = tr_B(\rho_{AB})
$$

This allows us to talk about sub-systems of a composite system.

$$
tr_B(|a_1\rangle\langle a_2| \otimes |b_1\rangle\langle b_2|) = |a_1\rangle\langle a_2| tr(|b_1\rangle\langle b_2|)
$$

## Schmidt Decomposition
---
Suppose $|\psi\rangle$ is a pure state of a composite system, $AB$. Then, there exists orthonormal states $|i_A\rangle$ for system $A$, and orthonormal states $|i_B\rangle$ of system $B$ such that

$$
|\psi\rangle = \sum_i \lambda_i |i_A\rangle |i_B\rangle
$$

where $\lambda_i$ are non-negative real numbers satisfying $\sum_i \lambda_i^2 = 1$ known as Schmidt co-efficients.

## Purification
---
Suppose we have a mixed state $\rho_A$ for a system $A$. Then, we can introduce another system $R$ such that $AR$ forms a pure state $|AR\rangle$ and $\rho_A = tr_R(|AR\rangle\langle AR|)$.

Given  $\rho_A = \sum_i p_i |i_A\rangle\langle i_A|$, we shall have the following where  $|i_R\rangle$ are orthonormal basis states.

$$
|AR\rangle = \sum_i \sqrt{p_i}|i_A\rangle|i_R\rangle
$$