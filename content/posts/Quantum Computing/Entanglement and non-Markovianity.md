## Introduction

During our study of Quantum Systems, mostly we have encountered Markovian evolutions (which are supposed to be the ideal case). This arises from weak coupling with an environment that acts as a memoryless reservoir.

![Untitled](Quantum%20Computing/images/Entanglement/Untitled.png)

This works very well from Quantum optics, but when dealing with interacting many-body systems. Why does it not work for multi-body systems? Because, subsystem’s coupling strength may be comparable to the coupling to the bath in case of interacting many-body systems.

Strong coupling (leading to non-Markovian dynamics) is a largely unsolved problem even today. There are hopes of achieving some sort of computational solution using hybrid quantum-classical machine learning.

Any ideal open quantum system will undergo Markovian dynamics provided that its evolution satisfies a Master equation.

$$
\frac{d\rho}{dt} = \mathcal L(\rho) = -i[H, \rho] + \sum_k \gamma_k (V_k\rho V_k^\dagger - \frac{1}{2} \{V_k^\dagger V_k, \rho\})
$$

Markovian: quantum system given by $TP$ maps $(\mathcal E)$ that define one-param semigroup of $CP$ maps such that $\mathcal E_{r_1 + r_0} = \mathcal E_{r_1}\mathcal E_{r_0}$.

- $\mathcal E_{t_2,t_0} = \mathcal E_{t_2, t_1}\mathcal E_{t_1, t_0}$ where $\mathcal E_{t_j, t_i} = \mathcal T e^{\int_{t_i}^{t_j} d\mathcal T}$$\longrightarrow$ Markovian dynamics
- Similar to classical Chapman-Kolmogorov equation (given below in functional and matrix form).
    
    $$
    p_{{i_{1},\ldots ,i_{{n-1}}}}(f_{1},\ldots ,f_{{n-1}})=\int _{{-\infty }}^{{\infty }}p_{{i_{1},\ldots ,i_{n}}}(f_{1},\ldots ,f_{n})\,df_{n}
    $$
    
    $$
    P(t + s) = P(t)P(s)
    $$
    

At the level of one-point probabilities, divisible and Markovian processes are equivalent. It is required to known the complete hierarchy of time-conditional probabilities to make any distinction.

$$
\mathbb P(x_1, t_1) = \sum_{x_0 \in \mathcal X} T(x_1, t_1 \vert x_0, t_0) \mathbb P(x_0, t_0)
$$

### Markov Process

![Untitled](Quantum%20Computing/images/Entanglement/Untitled%201.png)

Consider a Markov process $\{X(t),t \in I\}$. Given any two time instants $t_1$ and $t_2$ we have $T(x_2,t_2|x_1,t_1) = P(x_2,t_2|x_1,t_1)$.

Let us consider a system in a quantum state given by some (non-degenerate) density matrix $\rho$, the spectral decomposition yields

$$
\rho = \sum_xp(x)\vert\psi(x)\rangle\langle\psi(x)\vert
$$

Here the eigenvalues $p(x)$ form a classical probability distribution, which may be interpreted as the probabilities for the system to be in the corresponding eigenstate $\vert \psi(x)\rangle$, $\mathbb P(\vert \psi(x\rangle) = p(x)$.

Consider now some time evolution of the quantum system such that the spectral decomposition of the initial state is preserved, $\rho(t_0) = \sum_x p(x, t_0)\vert \psi(x)\rangle\langle\psi(x)\vert$,

$$
\rho(t) = \sum_x p(x, t)\vert \psi(x)\rangle\langle\psi(x)\vert \in \mathcal S
$$

where $\mathcal S$ denotes the set of quantum states with the same eigenvectors as $\rho(t_0)$. Since this process can be seen as a classical stochastic process on the variable $x$, which labels the eigenstates $\vert \psi(x)\rangle$, we consider it to be divisible if the evolution of $p(x,t)$ satisfies the classical definition of divisibility. In such a case, there are transition matrices $T(x_1,t_1|x_0,t_0)$, such that

$$
p(x_1, y_1) = \sum_{x_0 \in \mathcal X} T(x_1,t_1|x_0,t_0)p(x_0, t_0)
$$

can be written in terms of density matrices as $\rho(t_1) = \mathcal E_{(t_1, t_0)}[\rho(t_0)]$.

Here, $\mathcal E_{(t_1, t_0)}$ is a dynamical map that preserves the spectral decomposition of $\rho(t_0)$ and satisfies the following equation.

$$
\mathcal E(t_1,t_0)\rho(t_0) = \sum_{x_0 \in X}
p(x_0, t_0)\mathcal E(t_1,t_0)[\vert\psi(x)\rangle\langle\psi(x)\vert]\\ = \sum_{x_0 \in X} T(x_1,t_1|x_0,t_0)
p(x_0, t_0)[\vert\psi(x)\rangle\langle\psi(x)\vert]
$$

Furthermore, $\mathcal E(t_2,t_1)$ preserves positivity and trace of any state in $\mathcal S$ and obeys the composition law.

$$
\mathcal E(t_3,t_1) = \mathcal E(t_3,t_2)\mathcal E(t_2,t_1)
$$

![Comparision between Classical and Quantum markvianity](Quantum%20Computing/images/Entanglement/Untitled%202.png)

Comparision between Classical and Quantum markvianity

### Understanding Markovianity

1. Information flow: goes out of the system, to the environment and does not come back (fischer information)

![Untitled](Quantum%20Computing/images/Entanglement/Untitled%203.png)

1. Trace distance: In general, for open quantum systems (under Markovian dynamics) you can never increase the distance of two states, no matter what. So, basically when you wanna protect against noise all we are doing is slowing down the rate of noise (indistinguishable nonsense).
    
    $$
    T(\mathcal E(\rho), \mathcal E(\sigma)) \leq T(\rho, \sigma)
    $$
    
    Definition of trace distance given below.
    
    $$
    T(\rho, \sigma) = \frac{1}{2}|\rho - \sigma|_{S_1} = \frac{1}{2}\  \text{tr}\ |\rho - \sigma|
    $$
    
    However, if the distance between them increases then they become more distinguishable. This implies that information has entered the system from the environment, further implying non-markovianity.
    

![Untitled](Quantum%20Computing/images/Entanglement/Untitled%204.png)

1. Entanglement and/or coupling: weak coupling $\implies$ markovianity, and strong coupling $\implies$ non-markovianity. Also, decay of the entanglement with an ancillary system will be monotonically decreasing for Markovian evolutions.

### Measures of Quantum non-Markovianity

- Optimization Problem
    
    The measure of non-Markovianity can be formulated as an optimization problem. Let $\mathcal E$ be the physical dynamical map that is unknown to us, then we are interested in finding the map from the family of Markovian Maps $\mathcal E_{t_0+\epsilon,t_0}^M$such that its $S_1$ norm with $\mathcal E$ is as low as possible. At the same time, we also want to find the maximum non-markovianity over the entire duration, hence we treat $\epsilon$ as a variable and choose the one that gives us the largest non-markovianity. This leads to a min-max problem. The major disadvantage of this formulation is that it requires the knowledge of $\mathcal E$ beforehand, which we definitely don't know about. 
    
    $$
    \max_{\epsilon > 0} \min_{\mathcal E^M} \vert\vert \mathcal E_{(t_0 + \epsilon, t_0)} - \mathcal E^M_{(t_0 + \epsilon, t_0)} \vert\vert
    $$
    

![Entanglement vs Time](Quantum%20Computing/images/Entanglement/Untitled%205.png)

Entanglement vs Time

- Entanglement measure (sufficient)
    
    $$
    \mathcal I^{(E)} = \int_{t_0}^{t_{max}} |{\dot E}[\rho_{SA}(t)]|dt - \Delta E = \int_{t_0}^{t_{max}} |{\dot E}[\rho_{SA}(t)]|dt - \int_{t_0}^{t_{max}} d{E}[\rho_{SA}(t)]
    $$
    
    $$
    \Delta  E =  E[\rho_{SA}(t_0)] -  E [\rho_{SA}(t_{max})]
    $$
    
    $$
    \rho_{SA}(t_0) = \vert\phi\rangle\langle\phi\vert, ~~~ \phi = \frac 1 d \sum_{i = 0}^{d - 1} \vert i \rangle \otimes \vert i \rangle
    $$
    
    Hence we obtain the sufficient condition to show that an evolution is non-markovian as:
    
    1. If $I(E) = 0\implies$ the integral term is equal to $\Delta  E$. Which means there was no increase in entanglement at any point.
    2. If $\mathcal I(E) >0$ we conclude that the evolution is non-Markovian. However, there can be however non-Markovian quantum evolutions that remain undetected by the proposed measure.
    
    $ E$ can be something of the form — logarithmic negativity or concurrence.
    
    $$
     E (\rho_{SE}) = \log_2\vert\vert \rho_{SE}^{T_S} \vert\vert_1
    $$
    
    $$
     E(\rho_{SE}) = \max(0,\sqrtλ_1 −\sqrtλ_2 −\sqrtλ_3 −\sqrtλ_4)
    $$
    

### Partial Transpose

Partial transpose as mentioned above is described as follows.

$$
\rho_{AB}^{T_B} = (\mathbb I\otimes T)\rho_{AB}
$$

### Choi Isomorphism

Let $\mathcal E :\mathbb {C} ^{n\times n}\to \mathbb {C} ^{m\times m}$ be a linear map. Then, the following are equivalent:

- $\mathcal E$ is $n$-positive (i.e. $\mathcal E(A)\in \mathbb {C} ^{m\times m}$ is positive whenever $A\in \mathbb {C} ^{n\times n}$ is positive).
- The matrix $\Gamma_\mathcal E$, sometimes called the Choi matrix of $\Phi$, is positive.
    
    $$
    \Gamma_{\mathcal E}=\left(\operatorname {\mathbb I} _{n}\otimes \mathcal E \right)\left(\vert \phi \rangle\langle \phi \vert\right)
    $$
    
- $\mathcal E$ is completely positive.

The Choi-Jamiolkowski isomorphism allows to map many statements about states to statements about channels and vice versa.  For example, a channel is completely positive exactly if the Choi state is positive, a channel is entanglement breaking exactly if the Choi state is separable, and so further.

Clearly, the isomorphism is very straightforward, and thus, one could equally well transfer any proof from channels to states and vice versa; however, often it is much more intuitive to work with one or the other, and to transfer the results later on.

### Norms

Norm is a distance metric such that

1. $|cv| = |c|.|v|$
2. $|v+w| \leq |v| + |w|$
3. $|v| = 0$ iff $v = 0$

Examples of norms are as follows

- Manhattan ($L_1$)
- Euclidean ($L_2$)
- $L_p$ norm $\to |v|_{L_p} = (\sum v_i^p)^{1/p}$

Now, we have the following relations.

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

If $X \geq 0$, then $\sigma(X) = \lambda(X)$ then, $|X|_{S_1} = tr X \implies |\rho|_{S_1} {= \text{tr} (\rho)}$. Thus, $\rho$ is a density matrix $\iff \rho \geq 0$ and $|\rho|_{S_1} = 1$.

![Entanglement%20and%20non-Markovianity%20160f2cfc349640d1bb63e11617524db2/Untitled%206.png](Quantum%20Computing/images/Entanglement/Untitled%206.png)

### Necessary and sufficient condition for non-Markovianity

Notice that we never knew what the exact dynamical map was. We just kept applying it locally on our system and measuring the entanglement.

However, if we can reconstruct the dynamical map, then we can achieve a necessary and sufficient condition for non-markovianity. The reconstruction can be done by a method like quantum tomography.

$$
\mathcal E_{t + \epsilon, 0} = \mathcal E_{t + \epsilon, t}\mathcal E_{t, 0}
$$

In case of markovian evolution, we know that $\mathcal E_{t + \epsilon, t}$ is $CPTP$. Our necessary and sufficient condition is to prove the same $\forall t$ to conclude Markovianity.

We use the Choi-Jamiolkowski isomorphism to check whether $\mathcal E_{t + \epsilon, t}$ is $CP$, in other wordss we have to check if the following holds true.

$$
(\mathbb I \otimes \mathcal E_{t + \epsilon, t})\vert\phi\rangle\langle\phi\vert \geq 0
$$

Given the trace preserving property, we have the following as a measure of non-markovianity.

$$
f_{NCP}(t + \epsilon, t) = \vert\vert (\mathbb I \otimes \mathcal E_{t + \epsilon, t})(\vert\phi\rangle\langle\phi\vert) \vert\vert_1
$$

Therefore, $\mathcal E(t + \epsilon, t)$ is $CP$ if and only if $f_{NCP}(t + \epsilon, t) = 1$, otherwise $f_{NCP}(t + \epsilon, t) > 1$ which we shall use to arrive at a measure of non-markovianity.

$$
g(t) = \lim_{\epsilon \to 0^+} \frac{f_{NCP}(t + \epsilon, t) - 1}{\epsilon} = \begin{cases}
\mathcal g(t) = 0,~~ \text{~iff ~} \mathcal E_{t + \epsilon, t} \text{ is CP (markovian)}\\
\mathcal g(t) > 0, ~~ \text{~otherwise (non-markovian)}
\end{cases}
$$

$$
\mathcal I = \int_0^\infty g(t)dt 
$$

Now, $\mathcal I$ can be taken as a measure of non-Markovianity, and as long as $g(t)$ decreases fast enough and still is finite.

We can further obtained a normalized version of the above measure given by $\mathcal D_{NM}$.

$$
\mathcal D_{NM} = \frac{\mathcal I}{\mathcal I + 1} = \begin{cases}
\mathcal D_{NM} = 0 \text{~when~} \mathcal I = 0 \text{~(markovian)}\\
\mathcal D_{NM} \to 1 \text{~when~} \mathcal I \to \infty \text{~(non-markovian)}
\end{cases}
$$

## Examples

Single Damped Harmonic Oscillator: In this case, in order to visulaize the sensitivity of the proposed measure $\mathcal I^{(E)}$, two different spectral densities of the bath have been considered, along with several initial temperatures.

$$
J(ω) = αω^ke^{−ω/ω_c}
$$

where $k = 1$ for ohmic spectral density and $k = 3$ for super-ohmic spectral density.

Non-markovian character increases as $\alpha$ increases. As $\alpha \to 0$, the evolution approaches markovian character.

![Super-ohmic spectral density](Quantum%20Computing/images/Entanglement/Untitled%207.png)

Super-ohmic spectral density

![Ohmic spectral density](Quantum%20Computing/images/Entanglement/Untitled%208.png)

Ohmic spectral density

Pure Dephasing: If $\gamma(t) \geq 0$ we have markovianity, else if its negative we have non-markovianity.

$$
\frac{d\rho}{dt} = \gamma(t)(σ_zρσ_z −ρ)
$$

$$
g(t) = \begin{cases}
0,~~ \gamma(t) \geq 0\\
-2\gamma(t),~~ \gamma(t) < 0 
\end{cases}
$$

$$
\mathcal I = -2 \int_{\gamma(t) < 0} \gamma(t)dt
$$

## Conclusion

This report explored some basic concepts related to what Non-Markovian quantum evolution is and how it can be measured. We derived the necessary and sufficient conditions to indicate whether a dynamical map is Non-Markovian or not. We attempted to demonstrate our ideas by also using a classical analogue in thermodynamics.