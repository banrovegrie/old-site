## Introduction
---
Quantum Channels are generalizations of Quantum Operations. Since, in general our operations maybe noisy (inherently) and the system we are dealing with maybe open so Quantum Channels us the study of **noisy open** Quantum Operations.

$$
\rho \xrightarrow{U}\rho'
$$

The above only holds for **closed** quantum systems. Thus, in case of **noisy open** quantum systems we have the following.

$$
\rho \xrightarrow{\mathcal E} \rho'
$$

Here, $\mathcal E$ is a combination of:

- unitaries $(U)$
- adding systems $(\rho \to \rho \otimes \sigma)$
- subtracting systems or partial tracing $(\rho_{AB} \to \text{tr}_B \rho_{AB} = \rho_A)$

## Review of Density Matrices
---
Moreover, to deal with **noisy open** systems we also need to review density matrices which are the general way of representing noisy quantum states.

$$
\rho \equiv \text{noisy quantum state}\\
\mathcal E \equiv \text{noisy open quantum channel}
$$

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled.png](Quantum%20Computing/images/Quantum%20Channels/Untitled.png)

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%201.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%201.png)

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%202.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%202.png)

Now since, $\rho$ is positive semi-definite thus, $\frac{1 + ||\vec{a}||}{2} \geq 0 \implies ||\vec{a}|| \leq 1$.

This results in the Bloch Ball representation for general mixed state qubits, which serves as a generalization of the Bloch Sphere that serves as representation for pure state qubits. Pure state qubits have eigenvalues of $0$ or $1$, $\lambda(\rho) = 0\ \text{or}\ 1$.

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%203.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%203.png)

The eigenvalue of the maximally mixed state is ${I}/{2}$ where the state is actually given by the following.

$$
\frac{1}{2}(|0 \rangle\langle 0| + |1 \rangle\langle 1|) \equiv \frac{1}{2}(|+ \rangle\langle +| + |- \rangle\langle -|)
$$

## Quantum Operations
---
![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%204.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%204.png)

However, in both these above cases, we are still dealing with **closed** (albeit **noisy**) for the random case.

## Generalized Quantum Operations
---
We can refer to Generalized Quantum Operations as Quantum Channels (**noisy** and **open**) whose definitions we shall rediscover and formalize here.

Now, it should be noted that there are three major equivalent formalisms for Quantum Channels:

- Operational (Steinspring)
- Mathemtically Simplified (Kraus)
- Axiomatic (TPCP maps)

## Introduction to Steinspring Representation
---
For closed systems we have a probabilistic combinations of the above (noisy closed channels).

$$
|\psi\rangle \to U|\psi\rangle\\
|\psi\rangle\langle\psi| \to U |\psi\rangle\langle\psi|U^\dagger\\
\rho \to U\rho\ U^\dagger
$$

This can be generalized for noisy open channels as combinations of unitaries $(U)$, adding systems together $(\rho \to \rho \otimes \sigma)$ and subtracting systems $(\rho_{AB} \to \text{tr}_B(\rho_{AB}) = \rho_A)$.

But why is partial tracing allowed? Doesn't this "delete" information? 

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%205.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%205.png)

The information has basically flown out of your lab to the heavens (but still exists in nature) and in most cases, you simply can't access it anymore, kinda like your ex-girlfriend.

$$
\text{tr}(\rho_{AB}) = \sum_b (I_A \otimes \langle b|)\ \rho\ (I_A \otimes |b\rangle) = (I_A \otimes \text{tr}_B)(\rho_{AB})
$$

## Isometry
---
An operator $V \in \mathcal{L}(X),\ V:{X \to Y}$ is called an isometry if and only if $||V\vec{v}|| = ||\vec{v}||$ for all $\vec{v} \in {X}$. In other words, an isometry is a genralization of norm preserving operators.

Now, properties of linear isometries:

- $\langle v|v\rangle = \langle Vv|Vv\rangle = \langle v|V^\dagger V|v\rangle$
- Thus, $V^\dagger V = I_{{X}}$.

Linear isometries are not always unitary operators, though, as those require additionally that $X = Y$ and $V V^\dagger = I_X$.

By the Mazur–Ulam theorem, any isometry of normed vector spaces over $\mathbb{R}$ is affine. Affine transformations are those that preserve lines and parallelism (but not necessarily distances and angles).

## Steinspring Representation
---
Isometries allow us to restate the requirements of a **noisy open** quantum channel. Now, it can be formed by combinations of isometries and partial trace. Moreover, the purpose of the partial trace is to trash the environment shit out of my lab.

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%206.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%206.png)

Thus, we have the following formalism.

$$
V:A\to B\otimes E\\
\mathcal E : \mathcal L(A) \to \mathcal L(B)
$$

$$
\mathcal E(\rho) = \text{tr}_E(V\rho\ V^\dagger)
$$

Partial tracing can be delayed (deferred tracing), an idea similar to deferred measurements. Also, from a philosophical standpoint (Church of the Larger Hilbert Space) you can defer it forever.

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%207.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%207.png)

Now, the above circuit is equivalent to the below circuit. As a result, inductively, combinations of isometries and partial trace is equivalent to the $\mathcal E$ operator.

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%208.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%208.png)

## Kraus Operator Picture
---
We can fix a orthonormal bases $\{|e\rangle\}$ for $E$, and have $\{V_e\}$ such that

$$
V = \sum_e V_e \otimes |e\rangle
$$

where $V_e \in \mathcal L(A), V_e: A \to B$ and furthermore

$$
I = V^\dagger V = (\sum_{e_1} V^\dagger_{e_1} \otimes \langle e_1|)(\sum_{e_2} V_{e_2} \otimes |e_2\rangle)
$$

such that $V_e \neq V_e^\dagger$in general and thus, we have the Kraus operator condition (stated below).

$$
I = \sum_e V_e^\dagger V_e
$$

Thus, we can have a equivalent and simplified formalism of the Steinspring Operator $(\mathcal E)$, where $\{V_e\}$ are Kraus operators.

$$
\mathcal E(\rho) = \text{tr}_E (V \rho\ V^\dagger) = \text{tr}_E (\sum_{e_1, e_2} V_{e_1} \rho\ V_{e_2}^\dagger \otimes |e_1\rangle\langle e_2|)\\
\implies \mathcal E(\rho) = \sum_e V_e\rho\ V_e^\dagger
$$

Conversely, given $\{V_e\}$ satisfying Kraus operator conditions, $\mathcal E(\rho) = \sum_e {V_e \rho\ V_e^\dagger}$ is a quantum operator with $V = \sum_e V_e \otimes |e\rangle$ as the isometry involved in the transformation.

## Examples of Kraus Operators for Quantum Channels
---
1. $\mathcal E(\rho) = U \rho\ U^\dagger \rightarrow$ single Kraus operator $\{U\}$
2. $\mathcal E(\rho) = \sum_e p_e U_e\ \rho\ U_e^\dagger \rightarrow$ Kraus operators $\{\sqrt{p_e} U_e\}$
3. $\text{tr}(\rho_{AB}) = \sum_b (I_A \otimes \langle b|)\ \rho\ (I_A \otimes |b\rangle)$ where $V_b = (I_A \otimes \langle b |_B)$ thus we also have the following holding true, $\sum_b V_b^\dagger V_b = \sum_b I_A \otimes |b\rangle\langle b| = I_A \otimes I_B = I$.
4. Ultimate Refrigerator: $\mathcal E (\rho) = |0\rangle\langle 0|$, regardless of the initial state $\rho$. 
    
    $$
    V_0 = |0\rangle\langle 0|, V_1 = |0\rangle\langle 1|\\
    V_0 \rho\ V_0^\dagger + V_1 \rho\ V_1^\dagger = |0\rangle\langle 0|
    $$
5. Depolarizing Channel: $\mathcal E (\rho) = (1 - p)\rho + \rho ({I}/{2})$ $\rightarrow$ simple kind of white noise effect 
6. Amplitude Damping Channel: $\mathcal E_\gamma (\rho) = K_0 \rho\ K_0^\dagger + K_1 \rho\ K_1^\dagger$ where we have the following 
    
    $$
    K_0 = \begin{bmatrix}
    1 & 0 \\
    0 & \sqrt{1 - \gamma} \\
    \end{bmatrix} \text{ and, }\ 
    K_1 = \begin{bmatrix}
    0 & \sqrt{\gamma} \\
    0 & 0 \\
    \end{bmatrix}
    $$

## Axiomatic Definitions
---
By God, properties of $\mathcal E$ should be as follows:

- Linear (assume this or die, basically) and Hermitian preserving
- Trace preserving (TP) such that $\text{tr}(\mathcal E(\rho)) = \text{tr}(\rho) = 1$
- Completely positive (CP) since $\rho \geq 0 \implies (\mathcal E \otimes I)(\rho) \geq 0$

But why completely positive? Well, because we are dealing with isometries of form $A \to B \otimes E$.

Here, completely positive means that if $\mathcal E$ is applied on a subsystem, then the complete system and the subsystems must remain positive.

## Equivalence of TPCP maps and Kraus operators
---
Equivalence Theorem: If $\mathcal E(\rho) = \sum_e V_e\rho\ V_e^\dagger$ then $\mathcal E$ is TPCP and converse holds true as well.

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%209.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%209.png)

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%2010.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%2010.png)

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%2011.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%2011.png)

![Quantum%20Channels%2088f84e65202e4cfabb6e0530a1f66d41/Untitled%2012.png](Quantum%20Computing/images/Quantum%20Channels/Untitled%2012.png)

This implies that the map $N→J(N)$ is injective. In fact it is known as the Choi-Jamiołkowski isomorphism — a correspondence between quantum channels and quantum states (described by density matrices).

Equivalence of Operators: Given $2$ operators $\mathcal E$ and $\mathcal F$ with operator elements $\{\mathcal E_i\}$ and $\{\mathcal F_i\}$ respectively, if $\mathcal E = \mathcal F$ then  

$$
\mathcal E_i = \sum_j u_{ij} \mathcal F_j
$$

## Measurements as Quantum Operations
---
Measurement can be thought of as a quantum operation where the input is any quantum state and the output is classical, $\mathcal E(\rho) = \sum_x p_x|x\rangle\langle x|$ (diagonal density matrix). 

The probabilities, $p_x$, should depend on the state. Further, $p_x$ should be a linear function of the density matrix $p_x = \text{tr}(M_x \rho)$. From this we can work out the properties that $M_x$ should obey:

- Normalization: $\text{tr}(\mathcal E(\rho)) = \text{tr}(p_x) = tr(M_x\rho) = 1 \implies \sum M_x = I$
- Positive Semi-definite: $(\mathcal E \otimes I)(\rho) \geq 0 \implies p_x \geq 0$ thus $\text{tr}(M_x \rho) \geq 0, \forall\ M_x$ over $\rho$ thus, we have $M_x \geq 0 \implies M_x's$ are positive semi-definite $\implies M_x = E_x E_x^\dagger$

Thus, we have the following:

$$
\sum_x M_x = I\\
M_x \geq 0
$$

These conditions still leave room for noisy measurements, etc.

We can also talk about non-demolition measurements, which do not discard the quantum systems aftermeasurements. Consider the following quantum channel.

$$
 \mathcal E(\rho) =\sum_e V_e \rho V^\dagger_e \otimes |e\rangle\langle e| = \sum_e \frac{V_e \rho V^\dagger_e} {\text{tr}(V_e\rho V^†_e)} \otimes \text{tr}(V_e \rho V^\dagger_e)|e\rangle\langle e|
$$

This channel has the following interpretation: with probability as

$$
p_e = \text{tr}(V_e \rho V_e^\dagger) = \text{tr}(V_e V_e^\dagger\rho) = \text{tr}(M_e\rho)
$$

the state of the system after the application of this channel is $\rho_e = {(V_e \rho V^\dagger_e)}/{\text{tr}(V_e\rho V^†_e)}$. This is similar to having a measurement that outputs the post measured state $\rho_e$ with probability $p_e$.

## Quantum Norms and Distance Metrics
---
Motivation: Now that we have defined channels and states of information, how do you differentiate between two items of information? What does it mean to say that information is preserved by some process? 

Well for these questions it is necessary to develop distance measures. There is a certain arbitrariness in the way distance measures are defined, both classically and quantum mechanically, and the community of people studying quantum computation and quantum information has found it convenient to use a variety of distance measures over the years. Two of those measures, the trace distance and the fidelity, have particularly wide currency today.

## Norms
---
Norm is a distance metric such that

1. $|cv| = |c|.|v|$
2. $|v+w| \leq |v| + |w|$
3. $|v| = 0$ iff $v = 0$

Examples of norms are as follows

- Manhattan ($L_1$)
- Euclidean ($L_2$)
- $L_p$ norm $\to |v|_{L_p} = (\sum v_i^p)^{1/p}$

## Schatten $p$-norms
---
1. $L_1$ norm corresponds to probability distributions
2. $L_2$ norm corresponds to pure states
3. $L_\infty = \max_i {|v_i|}$

Similarly, schatten $p$-norm $:$ $|M|_{S_p} = |\sigma(M)|_{S_p}$ where $\sigma(M)$ is a vector of singular values of a matrix, say $M$.

$$
S_1 = \sum \text{singular values}\\
S_2 = \sqrt {\sum \text{singular values}^2}\\
S_\infty = \max_i |\text{singular values}|
$$

In case of density matrices (in general to positive semi-definite Hermitian operators), we have $\text{singular values = eigen values}$ thus, $\sigma(M) = \lambda(M)$.

$$
|X|_{S_p} = |\sigma(X)|_{L_p} = (\sum_i \sigma_i^p)^{1/p}
$$

If $X \geq 0$, then $\sigma(X) = \lambda(X)$ then, $|X|_{S_1} = tr X \implies |\rho|_{S_1} {= \text{tr} (\rho)}$.

Thus, $\rho$ is a density matrix $\iff \rho \geq 0$ and $|\rho|_{S_1} = 1$.

![Entanglement%20and%20non-Markovianity%20160f2cfc349640d1bb63e11617524db2/Untitled%206.png](Quantum%20Computing/images/Entanglement/Untitled%206.png)

## Measurements
---
Let us consider a simple system with $\{M, I-M\}$ as measurement operators.

Then, we have

$$
M \geq 0, I - M \geq 0 \iff M \leq I\\
\iff 0 \leq M \leq I\\
\iff |M|_{S_\infty} \leq 1
$$

But why is it that two objects with different norms can co-exist in the same operator framework? The answer lies in the notion of duality.

## Duality
---
Given a norm $|.|$ there exists a dual norm such that, $|x|_* = \max_{|y| \leq 1} |\langle x,y\rangle|$.

1. $L_2$ is dual to $L_2$
2. $L_1$ and $L_\infty$  are dual to each other
3. $S_2$ is dual to $S_2$
4. $S_1$ and $S_\infty$  are dual to each other

## Introduction to Trace Norm
---
$$
T(\rho, \sigma) = \frac{1}{2}|\rho - \sigma|_{S_1} = \frac{1}{2}\  \text{tr}\ |\rho - \sigma|
$$

Then, $\forall M$ where $M$ denotes measurement,

$$
|\text{tr}(M\rho) - \text{tr}(M\sigma)| = |\text{tr}(M (\rho - \sigma))| \leq |M|_{S_\infty} |\rho -\sigma|_{S_1} \leq |\rho -\sigma|_{S_1} = 2T(\rho, \sigma)
$$

In fact, we can tighten this inequality even further to obtain

$$
|\text{tr}(M\rho) - \text{tr}(M\sigma)| \leq T(\rho, \sigma)$$

$$\Big\downarrow$$
$$
T(\rho, \sigma) = \max_M |\text{tr}\ M(\rho-\sigma)|$$
$$
\Big\downarrow$$
$$
T(\mathcal E(\rho) - \mathcal E(\sigma)) \leq \max_M |\text{tr}\ M(\rho-\sigma| = T(\rho, \sigma)
$$

and finally we get the required inequality

$$
T(\mathcal E(\rho), \mathcal E(\sigma)) \leq T(\rho, \sigma)
$$

Thus, I can never increase the distance of two states, no matter what. So, basically when you wanna protect against noise all we are doing is slowing down the rate of noise (indistinguishable nonsense).