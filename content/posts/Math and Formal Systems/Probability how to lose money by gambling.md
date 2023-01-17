# Basics
---
### Axioms

1. $P(A) \geq 0$
2. $P(A \cup B) = P(A) + P(B)$, where both are disjoint sets
3. $P(\Omega) = 1$

### Properties

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

$$
P(A) \leq P(B), \text{ if } A \sub B
$$

### Conditional Probability

$$
P(A\vert B) = \frac{P(A \cap B)}{P(B)}
$$

### Total Probability

$$
P(B) = P(A_1 \cap B) + \cdots + P (A_n \cap B) \\
= \sum P(A_i) P(B\vert A_i)
$$

Here, $A_i$’s are independent.

### Independence

If $A$ and $B$ are independent, we have the following.

$$
P(A \vert B) = P(A)\\
P(A \cap B) = P(A)P(B)\\

$$

### Conditional Independence

$$
P(A \cap B \vert C) = P(A \vert C) P(B \vert C)
$$

# Expectation and Variance
---
### Definitions

$$
E[g(X)] = \sum_x g(x)p_X(x)
$$

$$
Var[X] = E[(X - E[X])^2]\\
Var[X] = E[X^2] - E[X]^2
$$

### Linearity

$$
E[aX + b] = aE[X] + b\\
Var[aX + b] = a^2\ Var[X]\\
E[aX + bY + c] = aE[X] + bE[Y] + c
$$

# Probability Mass Functions
---
$$
p_{X,Y}(x, y) = P(X=x, Y=y)
$$

### Marginal PMFs

$$
p_X(x) = \sum_y p_{{X, Y}}(x, y)
$$

$$
E[g(X, Y)] = \sum_x \sum_y g(x, y)p_{X, Y} (x, y)
$$

### Conditionals

$$
p_{X|A}(x) = P(X = x | A), \text{ such that } \sum_x p_{X|A}(x) = 1\\
p_X(x) = \sum P(A_i) p_{x|A_i}(x)
$$

$$
p_{X, Y}(x, y) = p_Y(y)p_{X|Y}(x|y)\\
p_X = \sum_y p_Y(y)p_{X|Y}(x|y)
$$

$$
E[g(X)|A] = \sum_x g(x)p_{X|A}(x)\\
E[g(X)|Y=y] = \sum_x g(x)p_{X|Y}(x|y)\\
E[X] = \sum P(A_i)E[x|A_i]
$$

### Independence strikes back

- $p_{X|A}(x) = p_X(x)$
- $E[XY]=E[X]E[Y]$
- $Var[X + Y] = Var[X] + Var[Y]$
- $p_{X, Y}(x, y) = p_X(x) p_Y(y)$,   $\forall$  $x \in X$ and $y \in Y$

# Continuity and Lovely Curves
---
$$
P(X\in B)= \int_B f_X(x)dx, \text{ where } f_X(x) \geq 0
$$

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x)f_X(x)dx
$$

### Cumulative Distributions

$$
F_X(x) = P(X \leq x)\\
F_X(x) = \int_{-\infty}^x f_X(x)dx
$$

### Conditionals

$$
\int_B f_{X|A}(x)dx = P(X \in B|A)\\
f_X(x) = \sum P(A_i) f_{x|A_i}(x)
$$

$$
f_{X, Y}(x, y) = f_Y(y)f_{X|Y}(x|y)\\
f_X = \int_{-\infty}^{\infty} f_Y(y)f_{X|Y}(x|y)
$$

### Conditional Expectation

$$
E[g(X)|A] = \int_{\Omega} g(x)f_{X|A}(x)
$$

$$
E[g(X)|Y=y] = \int_\Omega g(x)f_{X|Y}(x|y)\\
$$

$$
\\

E[X] = \sum P(A_i)E[x|A_i]
$$

### Bayes' Theorem

 You can of course interchange $p$ with $f$ to account for continuous random variables.

$$
p_X(x)p_{Y|X}(y|x) = p_Y(y)p_{X|Y}(x|Y)
$$

### Gimme More

$$
F_Y(y) = P(g(X)\leq y) = \int_{x | g(x) \leq y} f_X(x)dx
$$

where $Y = g(X)$.

Also, if $Y = aX+b$, then we have $f_Y(y) = \frac{1}{|a|}f_X(\frac{y - a}{b})$.

# Correlations
---
$$
Cov(X, Y) = E[(X - E[X])(Y - E[Y])]\\
= E[XY] - E[X]E[Y]
$$

$$
Var[X + Y] = Var[X] + Var[Y] + 2 Cov[X, Y]
$$

$$
Cor(X, Y) = \rho(X, Y) = \frac{Cov(X, Y)}{\sqrt{var(X)var(Y)}}
$$

# Laws of the land
---
### Law of iterated expectations

$$
E[E[X|Y]] = E[X]
$$

### Law of total variance

$$
Var[X] = E[Var[X|Y]] + Var[E[X|Y]]
$$

# Limits of the land
---
1. If $X$ takes only non-negative values then $P(X \geq a) \leq E[X]/a$.
2. $P(|X - \mu|\geq c) \leq \sigma^2/c^2$ for all $c > 0$.
3. According to the idea of convergence $\lim_{n\to \infty} P(|X_n - a| \geq \epsilon)= 0$.

### Central Limit Theorem

Independent sampling of any distribution always yields a mean distribution which is normal. 

$$
Z_n = \frac{X_1 + \cdots + X_n - n\mu}{\sigma\sqrt n}
$$

$$
\lim_{n \to \infty} P(Z_n \leq z) = \phi(z) = \frac{1}{\sqrt {2\pi}} e^{-z^2/2}
$$

![Untitled|center|600](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled.png)

### Law of large numbers

If you repeat an experiment independently a large number of times and average the result, what you obtain should be close to the expected value.

$$
P(\lim \frac{X_1 + \cdots + X_n}{n} = \mu) = 1
$$

![Untitled|center|600](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled%201.png)

# Distributions
---
The gaussian distribution shows up in nature a lot because there are many situations in which a lot of small effects sum up to the thing you actually measure.

Poisson statistics describe situations where an event occurs randomly but has a constant probability of happening everytime.

### Discrete Random Distributions

![Untitled|center|500](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled%202.png)

### Continuous Random Distributions

![Untitled|center|500](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled%203.png)

### Poisson Distribution

- To predict the number of events occurring in the future!
- More formally, to predict the probability of a given number of events occurring in a fixed interval of time.
- The Poisson Distribution, on the other hand, doesn’t require you to know $n$ or $p$. We are assuming $n$ is infinitely large and $p$ is infinitesimal. The only parameter of the Poisson distribution is the rate $\lambda$ (the expected value of $x$). In real life, only knowing the rate (i.e., during 2pm~4pm, I received 3 phone calls) is much more common than knowing both $n$ & $p$.

![Untitled|center|500](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled%204.png)

This gives the probability of observing $k$ events in an interval. The average number of events in an interval is designated by $\lambda$.

$$
P(X = k) = \frac{\lambda^k}{k!}e^{-\lambda}
$$

- Even though the Poisson distribution models rare events, the rate $\lambda$ can be any number. It doesn’t always have to be small.
- Assumptions:
    - The **average rate** of events per unit time is **constant**.
    - Events are **independent**.
- If the number of events per unit time follows a Poisson distribution, then the amount of time between events follows the exponential distribution. The Poisson distribution is discrete and the exponential distribution is continuous, yet the two distributions are closely related.

# Random Shit

---

1. How do you test whether a data sample is normal or not? [https://en.wikipedia.org/wiki/Jarque–Bera_test](https://en.wikipedia.org/wiki/Jarque%E2%80%93Bera_test)
2. Optimal theoretical size for a bet is given by the [https://en.wikipedia.org/wiki/Kelly_criterion](https://en.wikipedia.org/wiki/Kelly_criterion).
3. Random variable X is distributed as N(a, b), and random variable Y is distributed as N(c, d). What is the distribution of (1) X+Y, (2) X-Y, (3) X\*Y, (4) X/Y?

(1) $X+Y \sim N(a+c, \sqrt{(b^2 + d^2 + 2\rho bd)})$

(2) $X+Y \sim N(a+c, \sqrt{(b^2 + d^2 - 2\rho bd)})$

(3) $X*Y \sim N(a*c, \sqrt{(a^2 d + c^2 b + bd)})$  

![Standard deviation for Z = X + Y|center](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled%205.png) 
Standard deviation for Z = X + Y
![When, X and Y are independent variables|center|500](Math%20and%20Formal%20Systems/images/Probability%20how%20to%20lose%20money%20by%20gambling%202949d4177caa457daec4be598fbfda6c/Untitled%206.png)
When, X and Y are independent variables

4. The Monty Hall Problem