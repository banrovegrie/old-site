# Number Theory

<p style="text-align: right;"> By <em>Alapan Chaudhuri</em></h6>

## Preliminaries

- Well Ordering Principle
- Induction
- Binomial Theorem
    - ${n \choose k} = \frac{n!}{k!(n-k)!}$
    - ${n \choose k} + {n \choose k - 1} = {n + 1 \choose k}$

## Divisibility Theory in the Integers

- $a=bq+r$ for some $(a, b)\ \exists$ unique $(q, r)$ where $0 < b \leq a$

- $gcd(a, b) = ax + by$

- Euclidean Algorithm

### Linear Diophantine Equations

- $ax + by = c$ is a linear diophantine equations which has a solution iff $gcd(a,b) | n$.

- If $x_0$ and $y_0$ are some particicular solutions for the equation then the general form of equations shall be, $$x = x_0 + (\frac{b}{d})t\ \ \ \ \ y = y_0 - (\frac{a}{d})t$$ where $d = gcd(a, b)$.

## Primes and their Distribution

- Fundamental Theorem of Arithmetic
- Sieve of Eratosthenes
- If $p_n$ is the $n^{th}$ prime number then $p_n < 2^{2^{n-1}}$ and $$p_{n+1} \leq p_1.p_2.p_3...p_n + 1\\ \implies p_{n+1} \leq 2.2^2...2^{2^{n-1}} + 1 = 2^{2^{n} - 1} + 1 \leq 2^{2^n}$$

- Given any integer $n$ there are $n$ consecutive integers who are all composite. $$(n+1)!+2, ..., (n+1)!+(n+1)$$

### Conjectures

- There is a prime gap for every even number
- Twin Prime Conjecture (I believe Terry Tao loves it!)
- Goldbach Conjecture (oh the beauty!)

### Theorems

- Vinogradov Theorem: $n=p_1+p_2+p_3$ (if n is odd and sufficiently large)
- This is about the Goldbach theorem $$\lim_{x \to \infty} \frac{A(x)}{x} = 0$$ where $A(x)$ is the number of even numbers $<x$ that are not the sum of two primes
- Infinite primes of the form $4n+3$
- Dirichlet: If $gcd(a, b) = 1$ then the AP: $$a, a+b, a+2b, ...$$ has infinitely many primes.
- If all $n>2$ terms of the AP: $$p,p+d,...p+(n-1)d$$ are primes then $d$ is divisible by all primes $q<n$.

## Interesting Properties in Congruences

- $ca \equiv cb\ (mod\ n) \implies a \equiv c\ (mod\ \frac{n}{gcd(c,n)})$ 

- $ax \equiv 1\ (mod\ n)$ has a unique solution modulo $n$ iff $gcd(a, n) = 1$

- $ax \equiv b\ (mod\ n) \implies ax - ny = b$ and thus will have solutions iff $gcd(a,n) = b$

- $ax+by\equiv r\ (mod\ n)$ and $cx+dy \equiv s\ (mod\ n)$ has a unique solution modulo $x$ iff $gcd(ad-bc, n)=1$

### Chinese Remainder Theorem

$$
x \equiv a_1 \mod n_1\\ 
x \equiv a_2 \mod n_2\\
x \equiv a_3 \mod n_3\\
....\\
x \equiv a_r \mod n_r\\
$$

Let, $N = n_1...n_r$ and $N_i = \frac{N}{n_i}$ then, the solution for $x \mod n_1...n_r$ shall be $$x = \sum a_iN_ix_i$$ where $N_ix_i \equiv 1 \mod n_i$.

## Fermat's Theorem

The theorem states that: $a^{p-1} \equiv 1 \mod p$.

- Proof:
    - This is the required proof.
    - $a.2a.3a...(p-1)a \equiv 1.2...(p-1) \mod p$
    - From the equation above the Fermat's theorem, called formally as Fermat's Little Theorem in contrast with his last theorem, can be easily derived and hence proven.

If $p, q$ are two primes such that $a^p \equiv 1 \ (mod\ q)$ and $a^q \equiv 1 \ (mod\ p)$ then, $$a^{pq} \equiv 1 \ (mod\ pq)$$

## Wilson's Theorem

- $(p-1)! \equiv -1 \mod p$
- Proof:
    - $(p-1)! \equiv 1.2.3...(p-1) \mod p$
    - $\implies(p-1)! \equiv 1.(p-1).(2.3...(p-2)) \mod p$
    - $\implies (p-1)! \equiv (p-1) \mod p$
    - Hence, proved :) lol.
    - Backstory: Probably Leibnitz was the first person to find this shit but he never published. I am not quite sure who finally wrote the formal proof of this theorem. Probably, Euler.

- $x^2 + 1 \equiv 0 \ (mod\ p)$ has a solution iff $p \equiv 1 \ (mod\ 4)$ and $p$ is an odd prime.

## Pseudo Primes

If $n|2^n-2$ then $n$ is considered to be a pseudo prime, and then, $N = 2^n - 1$ is a larger pseudo prime, lol.

<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-AMS_CHTML"></script>
