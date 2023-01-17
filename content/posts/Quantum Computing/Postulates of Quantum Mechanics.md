
I shall state here the four major generic postulates of Quantum Mechanics stated in terms of both state-vector formalization and density-matrix formalization.

## State is a vector

1. Isolated physical system is given by its state vector operating on a certain Hilbert space.
2. Evolution of a closed quantum system is given by a unitary transformation.
    
    In its physical interpretation we have this postulate governed by the Schrodinger Equation, as stated.
    
    $$
    i{\hbar}\frac{d\vert\psi\rangle}{dt} = H\vert\psi\rangle
    $$
    
    The Hamiltonian is a hermitian operator and has a spectral decomposition, $H = \sum E\vert E\rangle\langle E\vert$.
    
3. The state space of a composite physical system is the tensor product of the state spaces of the component systems.
    
    $$
    \vert\psi\rangle = \vert\psi_1\rangle\otimes...\otimes\vert\psi_n\rangle
    $$
    
4. Quantum measurements are described by a collection $\{M_m\}$ of measurement operators acting on the state space of the system. 
    
    Probability that upon measurement the outcome is $m = p(m) = \langle\psi\vert M_m^\dagger M_m\vert\psi\rangle$ and the state of the system becomes as follows.
    
    $$
    \vert\psi\rangle \xrightarrow{\text{on measuring}} \frac{M_m\vert\psi\rangle}{\sqrt{p(m)}} = \frac{M_m\vert\psi\rangle}{||M_m\vert\psi\rangle||}
    $$
    
    Measurement operators also follow the completeness equation, $\sum_m M_m^\dagger M_m = I$.
    

## State is a density matrix

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