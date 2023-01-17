## Projective Measurement

A PM is defined by  $M = \sum_m \lambda_m \ket{m}\bra{m}$ where $\{\lambda_m\}$ are the set of outcomes and $\{M_m\} = \{\ket{m}\bra{m}\}$ are the set of measurement operators.

$$
p(m) = \langle \psi | M_m^\dagger M_m|\psi\rangle = \langle \psi | m\rangle \langle m|\psi\rangle = \|\langle m | \psi \rangle\|^2
$$

$$
\sum_mp(m) = 1\ \ \text{and} \ \ \ket{\psi} \xrightarrow{\text{on measurement}} \frac{M_m \ket{\psi}}{\sqrt{p(m)}} = \ket{m}
$$

## Classical Circuit

$$
f:\{0, 1\}^n \to \{0, 1\}^m
$$

A function with an m-bit output is equivalent to m functions, each with a one-bit output, so we may just as well say that the basic task performed by a computer is the evaluation of $f:\{0, 1\}^n \to \{0, 1\}$.

$$
f:\{0, 1\}^n \to \{0, 1\},\ \text{a boolean function}
$$

The evaluation of a boolean function $f$ can be reduced to a sequence of simple logical operations.

$$
f^{(a)} (x) = 
\begin{cases}
1&x=x^{(a)}\\ 
0&\text{otherwise}
\end{cases}
$$

where $f^{(a)}$ is obtained as the AND of $n$ bits with NOT operation may or maynot present with the atomic variables acting as the $n$ bits.

$$
f(x) = f^{(1)}(x) \vee f^{(2)}(x) \vee \ldots
$$

Thus, the above form of $f(x)$ is referred to as the DNF form (disjunctive normal form). Thus, $\{AND, OR, NOT\}$ is universal.

Note: the gatesets $\{AND, OR, NOT\}$, $\{NAND\}$ etc. are universal.

## Reversible Computation

Landauer’s Principle: erasure of information is a dissipative process.

According to Landauer’s principle, then, we need to do an amount of work at least $W = kT \ln 2$ to operate a $2$-to-$1$ logic gate at temperature $T$.

But, if we only allow invertible functions from $\{0, 1\}^n$ to $\{0, 1\}^n$ then there need be no dissipation and no power requirement. We can compute for free!

Any irreversible computation can be packaged as an evaluation of an invertible function. For example, for any $f: \{0, 1\}^n \to \{0, 1\}$, we can construct $\hat f: \{0, 1\}^{n + 1} \to \{0, 1\}^{n + 1}$.

$$
\hat f (x, y) = (x, y \oplus f(x))
$$

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled.png)

Universal reversible gates: {Fredkin} and {Toffolli} for classical computation.  {Toffoli, Hadamard} makes the set of universal quantum gates.

## Uncomputation

Disadvantages of Reversible computing:

1. Garbage output bits: $(x, 0)\to(f(x), g(x))$ where $f(x) =$  required output, $g(x) =$ garbage output. Now, $\ket{f(x)}\ket{g(x)}$ can be entangled.
2. Input dependent garbage qubits can interfere with your computation and give erroneous results.

But using uncomputation, we can clean up the garbage at a small constant cost. We can convert all reversible circuits this way into $(x, y) \to (x, y \oplus f(x))$.

## Universal Quantum Gates

$$
\|U - U_tU_{t-1}\ldots U_{1}\| < \epsilon,\ \  \ U_i \in G
$$

Solovay Ketanov Theorem: Any general $t$-gate quantum circuit can be $\epsilon$ approximated using only $O(t\ \text{polylog}(1/\epsilon))$ gates from $G = \{CNOT, H, R_{\pi/4}\}$. There are also other universal gate sets: some are efficient than others.

## Quantum Parallelism

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%201.png)

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%202.png)

- By applying $U_f$ only once, we are able to obtain a quantum state that contains in it all $2^n$ possible values of $f(x)$ in superposition.
- This in itself is not very useful. If we make projective measurement, we will observe some $|z⟩ |f (z)⟩$ with probability $1/2^n$.
- Quantum parallelism needs to be combined with interference, entanglement, to something better than classical computing.

## Phase Kickback Oracle

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%203.png)

If we substitute $\ket{-}$ for $y$ we get:

if $f(x) = 0$,

$$
\ket{x}\frac{\ket{0} - \ket{1}}{2} \xrightarrow{U_f} \ket{x}\frac{\ket{0} - \ket{1}}{2}
$$

and if $f(x) = 1$, then we have

$$
\ket{x}\frac{\ket{0} - \ket{1}}{2} \xrightarrow{U_f} -\ket{x}\frac{\ket{0} - \ket{1}}{2}
$$

and thus we have the follwoing.

$$
\ket{x}\ket{-} \xrightarrow{U_f} (-1)^{f(x)}\ket{x}\ket{-}
$$

The second input and output lines can be dropped as they remain the same in another frequently used representation.

![ff](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%204.png)

$$
H^{\otimes n} \ket{0}^{\otimes n} \xrightarrow{U_f^{\pm}} \frac{1}{\sqrt {2^n}} \sum _{x\in \{0, 1\}} \ket{x} \xrightarrow{U_f^{\pm}}\frac{1}{\sqrt {2^n}} \sum _{x\in \{0, 1\}} (-1)^{f(x)}\ket{x}
$$

## Deutsch-Josza Algorithm

In the Deutsch–Jozsa problem, we are given a black box quantum computer known as an [oracle](https://en.wikipedia.org/wiki/Oracle_machine) that implements some function $f:\{0, 1\}^n \to \{0, 1\}$. The function takes $n$-digit binary values as input and produces either a $0$ or a $1$ as output for each such value. 

We are [promised](https://en.wikipedia.org/wiki/Promise_problem) that the function is either [constant](https://en.wikipedia.org/wiki/Constant_function) ($0$ on all outputs or $1$ on all outputs) or balanced (returns $1$ for half of the input [domain](https://en.wikipedia.org/wiki/Function_domain) and $0$ for the other half). The task then is to determine if $f$ is constant or balanced by using the oracle.

In the Deutsch-Josza quantum algorithm the speedup is exponential.

- Classical Complexity: $2^{n - 1} + 1$ queries
- Quantum Complexity: $1$ query

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%205.png)

$$
\ket{0^{\otimes n}}\otimes \ket{1} \xrightarrow{H^{\otimes n + 1}} \frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} \ket{x} \otimes \ket{-}

$$

$$
\xrightarrow{U_f} \frac{1}{\sqrt {2^{n+1}}}\sum_{x \in \{0, 1\}^n} \ket{x} \otimes (\ket{f(x)} - \ket{1 \oplus f(x)}) = \frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} (-1)^{f(x)} \ket{x} \otimes \ket{-}
$$

$$
\frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} (-1)^{f(x)} \ket{x} \xrightarrow{H^{\otimes n}} \frac{1}{\sqrt{2^n}} \sum_{\forall x} (-1)^{f(x)} \big[\sum_{\forall y} (-1)^{x.y} \ket{y} \big]
$$

$$
= \frac{1}{\sqrt{2^n}} \sum_{\forall x}  \big[\sum_{\forall y} (-1)^{f(x) \oplus x.y} \ket{y} \big] = \frac{1}{\sqrt{2^n}} \sum_{\forall y}  \big[\sum_{\forall x} (-1)^{f(x) \oplus x.y} \big] \ket{y}
$$

Now, the probability of measuring $|0^{\otimes n}\rangle$ is as given bellow.

$$
\|\frac{1}{\sqrt{2^n}} \sum_{\forall x \in \{0, 1\}^n} (-1)^{f(x)}\| =\begin{cases}
0 & f(x) \text{ is balanced}\\
1 & f(x) \text{ is constant}
\end{cases}
$$

```python
def oracle(circuit, n):
    case = np.random.randint(2)

    # consider the function to be constant
    if case == 1:
        print("Example Constant:")
        output = np.random.randint(2)
        if output == 1:
            circuit.x(n)
        return circuit

    # example of a balanced function
    else:
        print("Example Balanced:")
        circuit.cx(0, n)
        return circuit

def deutsch_josza(n):
    circuit = QuantumCircuit(n + 1, n + 1)
    for i in range(0, n):
        circuit.h(i)
    circuit.x(n)
    circuit.h(n)
    circuit = oracle(circuit, n)
    for i in range(0, n):
        circuit.h(i)

    for i in range(0, n):
        circuit.measure(i, i)

    print(circuit)
    return circuit
```

## Bernstein-Vazirani Algorithm

Problem: Given a function $f:\{0, 1\}^n \to \{0, 1\}$ and a input $x$,  $f(x) = (s.x)\mod 2$. We are expected to find $s$.

Classical Complexity: $n$ queries

Quantum Complexity: $1$ queries

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%206.png)

$$
\ket{0^{\otimes n}}\otimes \ket{1} \xrightarrow{H^{\otimes n + 1}} \frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} \ket{x} \otimes \ket{-} \xrightarrow{U_f} \frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} (-1)^{f(x)} \ket{x} \otimes \ket{-} 
$$

$$
= \frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} (-1)^{s \cdot x} \ket{x} \otimes \ket{-} \xrightarrow{H^{\otimes n} \otimes \mathbb{I}} \frac{1}{\sqrt {2^n}}\sum_{x,y \in \{0, 1\}^n} (-1)^{s \cdot x + x \cdot y} \ket{y} \otimes \ket{-}
$$

The above evaluates to $\ket{s}$ because of the reason mentioned below.

$$
\ket{s} \xrightarrow{H^{\otimes n}} 
\frac{1}{\sqrt {2^n}}\sum_{x \in \{0, 1\}^n} (-1)^{s.x} \ket{x} \xrightarrow{H^{\otimes n}} \frac{1}{\sqrt {2^n}}\sum_{x,y \in \{0, 1\}^n} (-1)^{s\cdot x + x\cdot y} \ket{y}
$$

## Simon’s Algorithm

Problem: Given a function $f:\{0, 1\}^n \to \{0, 1\}^n$ and some $x$ and $y$,  $f(x) = f(y)$ if and only if $x = y \oplus s$.

| Problem | Classical Complexity | Quantum Complexity |
| --- | --- | --- |
| Deutsch-Josza | $2^{n-1} + 1$ | $1$ |
| Bernstein-Vazirani | $n$ | $1$ |
| Simon’s Algorithm  | $O(\sqrt {2^{n}})$ | $O(n)$ |

![Untitled](Quantum%20Computing/images/Basics%20of%20Quantum%20Algorithms/Untitled%207.png)

$$
(H^{\otimes n}\ket{0^n})\otimes\ket{0^n}= \frac{1}{2^{n/2}} \sum_{x \in {0, 1}^n} (\ket{x} \otimes \ket{0^n})
$$

$$
\xrightarrow{U_f} {\frac {1}{2^{n/2}}}\sum _{x\in \{0,1\}^{n}}\left|x\right\rangle \otimes \left|f(x)\right\rangle = {\frac {1}{2^{(n - 1)/2}}}\sum _{x\in \{0,1\}^{n}}\frac{(\left|x\right\rangle + \ket{x \oplus s})}{\sqrt 2} \otimes \left|f(x)\right\rangle
$$

Once we measure the last $n$ registers, we obtain some $\ket{f(x)}$. Then the state on our above register converges to some $({\ket{x} + \ket{x \oplus s}}) /{\sqrt 2}$.

$$
\frac{\ket{x} + \ket{x \oplus s}}{\sqrt 2} \xrightarrow{H^{\otimes n}} \frac{1}{\sqrt{2^{n + 1}}} \sum_{z} [(-1)^{x\cdot z} + (-1)^{(x\oplus s)\cdot z} ] \ket{z}
$$

Thus, we finally obtain the following state in our first $n$ registers.

$$
\frac{1}{\sqrt{2^{n + 1}}} \sum_{z} (-1)^{x}[1 + (-1)^{s\cdot z} ] \ket{z}
$$

Now, upon measurement we will observe $\ket{z}$ if and only if $(s\cdot z) \mod 2 = 0$.

$$
s\cdot z_1 = 0\\
\vdots\\
s\cdot z_n = 0
$$

If $\{z_1 \ldots z_2\}$ are linearly independent then we have $s$ after $O(4n)$. The probability that they are independent is at least $> 1/4$.