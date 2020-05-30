# Number Theoretic Functions

## Generic Number Theoretic Functions

Consider, the following equation. $$F(n) = \sum_{d|n}f(d)$$ Here, $F$ and $f$ are teo number theoretic functions operating on natural numbers. Later, in many cases we shall find that this summation form of representation is of utmost importance.

## Sum and Number of Divisors

The initial number theoretic functions that we shall explore are $\tau(x)$ and $\sigma(x)$.

Now, let us formalize these functions.

Consider $n$ to be of the form $n=p_1^{k_1}...p_r^{k_r}$ then, 

- $\tau(x)$ represents number of divisors of $x$ and can be expressed as $$\tau(x) = (k_1 +1).(k_2+1)...(k_r+1)$$

- $\sigma(x)$ represents the sum of divisors of $n$ and can be expressed as $$\sigma(x)=\frac{p_1^{k_1+1} - 1}{p_1 - 1}...\frac{p_r^{k_r}-1}{p_r - 1}$$ 


We can also representy the above functions in terms of summation. $$\tau(x) = \sum_{d|n}1$$ $$\sigma(n) = \sum_{d|n}d$$

Also, another interesting result that can be obtained in multiplicative form $$n^{\frac{\tau(n)}{2}} = \prod_{d|n}d$$

## Multiplicative Property of Number Theoretic Functions

If $f(mn) = f(m)f(n)$ whenever $gcd(m,n) = 1$ then, $f$ is considered to be a multiplicative function.

### Some Results related to Multiplicative Functions

- The functions $\tau$ and $\sigma$ are both multuplicative.
- If $f$ is  multiplicative then $F$ is multiplicative as well.
    - We can prove this with the help of the following lemma: 
        - If $gcd(m,n)=1$ then, the set of positive divisors of $mn$ consists of distinct products of form $d_1d_2$ where $d_1|m$ and $d_2|n$ and $gcd(d_1, d_2) = 1$.

## Mobius Function

Consider, the following function.

$$
\mu(n) = 
\begin{cases} 
      1, & n=1 \\
      0, & p^2|n\ for\ some\ prime\ p  \\
      (-1)^r, & n=p_1...p_r\ where\ each\ p_i\ is\ a\ distinct\ prime
\end{cases}
$$

This function $\mu$ is known as the mobius function.

### Properties of the Mobius Function

- The function $\mu$ is multiplicative
- For each positive integer $n \geq 0$,
    $$
    F(n) = \sum_{d|n}\mu(d)
    = \begin{cases}
        0, & n>1\\
        1, & n=1\\
    \end{cases}
    $$

### Mobius Inversion Formula

Let $F$ and $f$ be two number theoretic functions related by the formula 
$$
F(n) = \sum_{d|n}f(d)
$$ 
then, 
$$
f(n) = \sum_{d|n}\mu(\frac{n}{d})F(d) = \sum_{d|n}\mu(d)F(\frac{n}{d})
$$ 

A major implication of the above formula is that if $F$ is a multiplicative function such that,
$$
F(n)=\sum_{d|n}f(d)
$$ 
then $f$ is a multiplicative function as well.

## Other Well-known Number Theoretic Functions