# Models of Classical Computation
---
The following serve as universal models of computation:

- Turing Machines
- $\lambda$-calculus
- Circuits

### Super-Universal

Circuits can describe computations which are beyond what a Turing machine can do.

Apparently, we can solve the halting problem under some circuit model. But, what is that supposed to mean?

### Quantum Computation

The idea of a QC model is to have information in superposition. If we want Turing Machines to be part of the quantum computational model then we will somehow have to make the read/write head to be in a superposition. But that is not possible (doubt). Hence we use a circuit where we keep the bits in a superposition and operate on them with gates.

# History of Quantum Mechanics and Computation
---
Major questions in QM started arising with the EPR paradox in 1936 when faster than light travel was questioned. 

Here's the paradox: Consider $2$ particles that are moving away. Their positions are $x$ and $-x$ and momenta are $p$ and $-p$. Now we can't measure the exact position and momentum of one particle due to the uncertainty principle. But what if we measure the position of one particle and momentum of the other at the same time (Like a split second difference)? Assuming there is no interaction between the particles, we would in principle know the position and momentum of one particle at a time (cause we can know position or momentum of particle $1$ if we measure that quantity on the second particle cause its just the negative of it). This would violate the uncertainty principle. Hence, there has to be some sort of interaction between the two particles that makes the wavefunction of particle $2$ also collapse instantaneously when I measure position or momentum of particle $1$. This mean that the particles were somehow connected. This was the paradox. But Schrodinger said this is possible by entanglement.

In 1964 Bell gave his Theorem and then it was later verified too which proved that Quantum Mechanics is cool with EPR pair. But there was another problem that how is faster than light communication possible? It was later proved that faster than light communication is not possible indeed as you cannot actually send 'information' with the entanglement coordination. Basically you cannot manipulate the particles to actually transmit any useful information.

Non-cloning theorem: In physics, the no-cloning theorem states that it is impossible to create an independent and identical copy of an arbitrary unknown quantum state, a statement which has profound implications in the field of quantum computing among others.