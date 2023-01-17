## Definitions

**Deterministic Finite Automata**: A $5$-tuple $\{Q, \Sigma, \delta,q_0, F\}$ where $\delta: Q \times \Sigma \to Q$.

**Language**: $L \subseteq \{0, 1\}^*$

**Recognizing Language**: If a machine $M$ accepts all strings $\in L$ and rejects every other string $\not\in L$, then we say that $M$ recognizes $L$. Conversely, $L(M) =$  language recognized by $M$.

**Regular Expressions**: Uses $()\text{ braces},\ |\text{ union},\ *\text,\ \cdot\text{ concatenation}$.

**Non-deterministic Finite Automata**: A $5$-tuple $\{Q, \Sigma, \delta,q_0, F\}$ where $\delta: Q \times \{\Sigma \cup \epsilon\} \to 2^Q$.

**Generalized NFA**: A $5$-tuple $\{Q, \Sigma, \delta,q_{start}, q_{accept}\}$ where we have the following.

$$
\delta: \{Q - \{q_{accept}\}\} \times \{Q - \{q_{start}\}\} \to R\ (\text{Regex})
$$

## Theorems on Finite Automation

- $L(\text{finite automata}) = \text{regular language}$
- All finite languages are regular.
- Memory of a finite automata $= log_2 (|Q|) \sim O(1)$
- Regular languages are closed under the union operation.
- Regular languages are closed under the concatenation operation.
- $\text{Regex} \equiv \text{DFA} \equiv \text{NFA}$
- For a given NFA of n state, number of states in equivalent DFA is atmost $2^n$. Worst case complexity is $O(2^n)$.
- Conversion of NFA to DFA may require exponential increase in space. But $2^{O(1)} = O(1)$.

## Pumping Lemma

If $A$ is a regular language then there is a number $p$ where if $s$ is any string in $A$ of length at least $p$ $(|s| \geq p)$, then $s$ may be divided into three pieces, $s = xyz$, satisfying the following conditions:

1. for each $i \geq 0,\ xy^iz \in A$
2. $\vert y \vert > 0$
3. $\vert xy \vert \leq p$

![Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled.png|center|600](Algorithm%20Design/images/Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled.png)

## Main Proof: $\text{Regex} \equiv \text{DFA} \equiv \text{NFA}$

![Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%201.png|center|600](Algorithm%20Design/images/Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%201.png)

![Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%202.png|center|600](Algorithm%20Design/images/Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%202.png)

![Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%203.png|center|600](Algorithm%20Design/images/Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%203.png)

![Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%204.png|center|600](Algorithm%20Design/images/Finite%20Automata%20a4f27eeeac384c3eab14aee365266b15/Untitled%204.png)