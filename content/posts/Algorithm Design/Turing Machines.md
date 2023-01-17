## Problems

Problems can always be modelling using binary strings.

Types of problems:

1. Decision
2. Search
3. Counting

Sometimes, search problems can be reduced to decision problems.

![Untitled|center|600](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled.png)

However, such reductions are often non-trivial and in many cases unknown.

## Problems and Turing Machines

![Untitled|center|500](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%201.png)

The number of turing machines are countably infinite $(\aleph_0)$ whereas the number of problems (or languages) are uncountably infinite since they are a powerset of $\{0, 1\}^*$. 

## Decidability

![Untitled|center|300](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%202.png)

A language is Recognizable iff there is a Turing Machine which will halt and accept *only* the strings in that language and for strings not in the language, the TM either rejects, or does not halt at all. 

Note: There is no requirement that the Turing Machine should halt for strings not in the language.

A language is Decidable iff there is a Turing Machine which will accept strings in the language and reject strings not in the language.

$$
\text{R} = \{L: \text{there is a TM that decides }L\}
$$

$$
\text{RE} = \{L: \text{there is a TM that recognizes }L\}
$$

Are all languages $\in$ RE? No. We have something called Arithmetic Hierarchy that deals with such problems.

## Halting Problem Proof

Behold the rigor of wikipedia (Penrose 1990).

$$
h(i, x) = \begin{cases}
1,\ \text{ if program } i \text{ halts on input }x\\
0,\ \text{otherwise}
\end{cases}
$$

Here program $i$ refers to the $i$-th program in an enumeration of all the programs of a fixed Turing-complete model of computation.

The proof proceeds by directly establishing that no total computable function with two arguments can be the required function $h$.

As in the sketch of the concept, given any total computable binary function $f$, the following partial function $g$ is also computable by some program $e$:

$$
g(i) = \begin{cases}
0, \text{ if } f(i, i) = 0\\
\text{undefined, otherwise} 
\end{cases}
$$

![Untitled|center|200](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%203.png)

## Multi-tape to Single-tape conversion

![Untitled|center|350](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%204.png)

![Untitled|center|350](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%205.png)

## NTM vs TM

Langauges decided by Non-deterministic Turing Machine is equivalent to the set of languages decidable by a Deterministic Turing Machine.

![Untitled|center|400](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%206.png)

![Untitled|center|400](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%207.png)

![Untitled|center|400](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%208.png)

![Untitled|center|400](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%209.png)

## Savitch's Theorem

![Untitled|center|400](Algorithm%20Design/images/Turing%20Machines%203d78e24caed44d56af5094d5221c2145/Untitled%2010.png)