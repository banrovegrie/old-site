My notes for Complexity Theory. Also, you should read this while listening to this [playlist](https://open.spotify.com/playlist/11X4breG3ZmjgcPG1fm5co?si=673bc7d15f45496b).

## Encoding into Strings

- Set of all finite strings $\{0, 1\}^*$
- Can represent integers, alphabets and graphs (using adj matrix)

For example, you can encode tuples $\langle x, y\rangle$ as $[x] \#[y]$ where $0 \to 00, 1 \to 11$ and $\# \to 01$.

- Check out [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding).

## Languages

Given a boolean function, define $L_f = \{x: f(x) = 1\}$ as the set of inputs on which $f$ accepts $x.$

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled.png)

$$
L_f = \{[G]\circ[k]: \exists S\subset V \text{ s.t. } |S| =  k \text{ and } \forall u, v \in S, (u, v)\not\in E\}
$$

Now we have the encoding of a problem for example. given the input $[G], [k]$ how does $f$ compute $f([G])$? We have an algo but to run it, we need the idea of a machine.

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%201.png)

## Turing Machines

We can also describve a turing machine as a $7$ tuple.

- $Q$ as the set of states
- blank symbol $\square$
- $\Sigma$ as the alphabet ($\Gamma = \Sigma \cup \{\square\}$)
- $q_o$  as the start state
- $F$ as the set of final states
- $\delta$ as the transition function

$$
\delta : Q\times \Gamma^k \to Q \times \Gamma^{k - 1} \times \{L, R, S\}^{k}
$$

Size of the transition table is $|Q|.|\Gamma|^k$ as required.

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%202.png)

## Problems

Problems can always be modelling using binary strings.

Types of problems:

1. Decision
2. Search
3. Counting

Sometimes, search problems can be reduced to decision problems.

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%203.png)

However, such reductions are often non-trivial and in many cases unknown.

## Problems and Turing Machines

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%204.png)

The number of turing machines are countably infinite $(\aleph_0)$ whereas the number of problems (or languages) are uncountably infinite since they are a powerset of $\{0, 1\}^*$. 

## Decidability

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%205.png)

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

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%206.png)

## Multi-tape to Single-tape conversion

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%207.png)

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%208.png)

## NTM vs TM

Langauges decided by Non-deterministic Turing Machine is equivalent to the set of languages decidable by a Deterministic Turing Machine.

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%209.png)

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%2010.png)

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%2011.png)

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%2012.png)

## Savitch's Theorem

![Untitled](Quantum%20Computing/images/Yo,%20what's%20complexity%20theory/Untitled%2013.png)