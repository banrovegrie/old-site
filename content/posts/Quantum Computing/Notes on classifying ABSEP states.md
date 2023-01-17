# Introduction
---
Before introducing the problem of entanglement detection, we’ll look at what is entanglement and what are the different types of entanglement.

## Entanglement

Intuitively, entanglement can be thought of as some kind of non-local quantum correlations that exist between quantum particles. Or a more accurate thought process for understanding entanglement would be that if two particles are entangled, then it is not possible to describe the quantum state of one particle independent of the other particle. This applies, of course, to multiple particles, if they are entangled.

### Bipartite Entanglement

We will first study the case where only two particles are entangled. This is known as bipartite entanglement. To understand entanglement better, we first need to see what separability means.

Separability is kind of like the opposite of entanglement. Entangled and separable states are mutually exclusive and exhaustive. Which means that if a quantum state is not separable, it is entangled and vice-versa.

Hence, if we able to write down the definition of separability; whatever quantum state does not fit this definition will be entangled.

- **Pure States**: We define a bipartite separable pure state as $| \psi \rangle = | \phi^A \rangle \otimes | \phi^B \rangle$ which is also called a product state. Hence, a pure state that cannot be expressed at a product state is a pure entangled state.
- **Mixed States**: We define a general bipartite separable mixed state as $\varrho=\sum_{i} p_{i} \varrho_{i}^{A} \otimes \varrho_{i}^{B}$ which is just a mixture of product states. And hence, similar to the pure case, an entangled mixed state will be a state that cannot be written in the above form.

### Multipartite Entanglement

We saw how entanglement can exist between two particles. It can also exist between mutliple particles and that too, in multiple ways. One way is that, say there are three particles, and there is bipartite entanglement between each pair of them. Another way is that, instead of bipartite entanglement between pairs, there exists entanglement between all three of them. This is known as genuine multipartite entanglement. We won’t be focusing on multipartite entanglement in the report.

# Geometry
---
There is a nice geometric representation of quantum states which is worth considering. Note that whenever we are talking about states, we are talking about a specific hilbert space. Meaning, a $16$ dimensional state might be separable as $4 \otimes 4$ state but not as a  $2\otimes 8$ state.

## Convexity of quantum states

The entire set of quantum states is a convex set. How do we know this? Take any two quantum states. If you take any convex combination of these two, then the resulting state will always be a quantum state. In fact, it will be a mixed state.

Hence, we also know that the pure states are the extreme points of the entire set as we cannot add two quatum states to get a pure state.

### Convexity of separable states

The set of separable states is also a convex set.

Take two separable states $\varrho = \sum_{i} p_{i} \varrho_{i}^{A} \otimes \varrho_{i}^{B}$ and $\varphi = \sum_{j} q_{j} \varphi_{j}^{A} \otimes \varphi_{j}^{B}$. If we take a convex combination, we will again get a separable state.

And here, the extreme points are the pure product states. Hence, it is a subset of the extreme points of the set of all quantum states.

### Set of entangled states

If we subtract the set of separable from the set of quantum states, then we get the set of entangled states. It is easy to see that it is not convex. If we take a convex combination of two entangled states, we might get a separable state.

# Entanglement Detection
---
We know the definition of entanglement and separablity. We also know the extreme points of the convex sets in the geometric representation. Now, the big question is that given the density matrix of a state, can we tell whether it is entangled or separable?

## Pure States

Let’s talk about the easier case first. For pure states, if a state is separable, it is a product state. And it’s really easy to verify whether a state is a valid product state or not. You just have to solve a couple of equations.

Let’s look at this with an example (also since we are talking about pure states right now, we’ll use the vector notation).

Consider this given state.

$$
\ket{\psi} = [1 \ 0 \ 0 \ 0]^T
$$

We want to check if this 4 dimensional vector is $2 \otimes 2$ separable. So we’ll simple solve for the following.

$$
[a \ b]^T \otimes [c \ d]^T = [1 \ 0 \ 0 \ 0]^T
$$

If there exists a valid solution, such that both the states are valid, then $\ket{\psi}$ is separable. In this example, our solution is $a = 1, \ b=0, \ c=1, \ d=0$. Hence $\ket{\psi}$ turns out to be separable.

## Mixed States

This is where the tricky part of the problem is. A mixed separable state $\sum_{i} p_{i} \varrho_{i}^{A} \otimes \varrho_{i}^{B}$ can be a statistical sum over infinite product states with the corresponding probabilities. Hence, it’s computationally hard to find out whether a given state is separable or not like we did in the pure states case.

This is the point where we start exploting actual properties of separable states to find out whether a state is entangled or not. Note that, a general solution is still not known. The following criterias only work sometimes and when they work, they are only able to tell with surety that a given state is entangled. They cannot say that the state is separable.

## Creating a criterion

Before formalising any actual criteria, let’s intuitively consider what can be used to detect entanglement. A good approach is to think about some property of separable states that always holds true under certain operations, which might be violated if the state is entangled to begin with.

Completely Positive maps are positive maps that can be extended to any higher dimension. Positive but not CP maps however, might not be extendable to higher dimensions and might lose their property of positivity. This is one of the keys to our problem. We can use this property to detect entanglement. How?

Consider a separable state $\varrho = \sum_{i} p_{i} \varrho_{i}^{A} \otimes \varrho_{i}^{B}$ and a positive but not CP map $\Lambda$ that acts on space $B$. Let’s apply this on our state $(I \otimes \Lambda) \varrho = \sum_{i} p_{i} \varrho_{i}^{A} \otimes \Lambda(\varrho_{i}^{B})$.

The output of $\Lambda(\varrho_{i}^{B})$ will always be some valid density matrix $\varphi_{i}^{B}$ as $\Lambda$ is positive. Hence our new state will be $\varrho' = \sum_{i} p_{i} \varrho_{i}^{A} \otimes \varphi_{i}^{B}$ which is still separable.

What happens if we applied $I \otimes \Lambda$ on entangled states? Since they do not have such a separable form, the output state will not necessary be a valid density matrix, unlike the separable case. This might not always happen, but when it does, we know for sure that the state is entangled. Hence, this kind of criterion is only sufficient and not necessary in general.

## Criteria

There are many criteria for detecting entanglement. We’ll start by introducting a criterion based on the method we described above.

### PPT Criterion

The transposition map is a positive map that is not completely positive. Hence, using the method described above, we can detect many entangled states with it. It is called positive partial transpose because we apply the partial transposition map $(I \otimes T)$ on our state and check whether the output state is positive semi-definite or not.

Why do we specifically focus on the transposition map? Because for $2 \times 2$ and $2 \times 3$ dimensions, the PPT criterion is necessary and sufficient. This is stated by the Horodecki theorem.

### Other critera

There are a few other criteria like CCNR criterion, range criterion, the majorization criterion based on eigenvalues the state, some algorithmic approaches which formulates the problem as a convex optimisation problem, and some more as well. This area is active in terms or research.

# Entanglement Witnesses
---
Entanglement witnesses are observables such that:

- $Tr(\mathcal{W} \varrho_s) \geq 0$ for all separable states $\varrho_s$
- $Tr(\mathcal{W} \varrho_e) < 0$ for at least one entangled state $\varrho_e$.

Then we call $W$ the witness for the entangled state(s) $\varrho_e$.

### What’s so special about witnesses?

The criteria we saw earlier assume that we know the density matrix of our state. Witnesses, however, are observables. They don’t need to know the density matrix. You simply feed them a state to act on, and then measure. If you get a value less than zero, voila! You have just detected an entangled state.

## Geometric View

How do witnesses relate to the convex set representation we looked at earlier? Since the expectation value of an observable depends linearly on the state, the states where $Tr(W\varrho)= 0$  would be a hyperplane in the set of quantum states and would divide it into two parts.

![Notes%20classifying%20ABSEP%20states%20dbe6d7c6f75442afac49db15242b3b8a/Untitled.png](Quantum%20Computing/images/Notes%20classifying%20ABSEP%20states/Untitled.png)

Both of the lines shown are valid witnesses. $\mathcal{W}^{(1)}$ is however better than $\mathcal{W}^{(2)}$ as it detects more entangled states. We can, in fact, call $\mathcal{W}^{(1)}$ as optimised, because if it was shifted even slightly, it wouldn’t be a valid witness because $Tr(\mathcal{W}\varrho)$  would be $< 0$ for some separable states.

### Completeness of witnesses

Through the geometric view, it is easy to see that the set of witnesses can detect all entangled states. Or to put it in better terms: For each entangled state $\varrho_e$, there exists an entanglement witness detecting it.

The reason is that, since separable states form a convex set, there will always be a hyperplane separating the set of separable states with any given point outside the set (which is our entangled state).

## How do we construct witnesses?

There are many ways to construct witnesses depending on the state we want to detect. The review paper (on Entanglement Detection) talks about a certain example where we detect NPT entangled states. We take the NPT entangled state $\varrho_e$, apply partial transposition on it. Let eigenvector $\ket{n}$ correspond to the negative eigenvalue $\lambda_{-}$ in the NPT output. So, we construct out witness

$$
\mathcal{W} = \ket{n}\bra{n}^{T_A}
$$

which detects our state $\varrho_e$. How? Let’s apply it and see! We need to find $Tr(W\varrho_e)$.

$$
Tr(\mathcal{W} \varrho_{e})=Tr(|\eta\rangle\langle\eta|^{T_{A}} \varrho_{e})=Tr(|\eta\rangle\langle\eta| \varrho_{e}^{T_{A}})=\lambda_{-}<0

$$

## Hahn-Banach Separation Theorem

If $A$ and $B$ are non empty convex subsets of a real normed vector space $V$ such that they are disjoint and $A$ has an interior point then $\exists$  a hyperplane separating $A$ and $B$.

## Krenin-Milman Theorem

A convex compact set corresponding to finite dimensional vector space is equal to the convex hull of the extreme points of the set.

# Absolutely Separable Quantum States
---
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

![Untitled](Quantum%20Computing/images/Notes%20classifying%20ABSEP%20states/Untitled%201.png)