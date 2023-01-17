## Entropy

$$
H(X) = - \sum_{x \in X} p(x) \log(p(x))
$$

Here, information is given by $-\log(p(x))\ \forall x \in X$.

$$
H(X) \geq 0 
$$

## Joint Entropy and Conditional Entropy

$$
H(X, Y)= - \sum_{x \in X} \sum_{y \in Y} p(x, y) \log(p(x, y))
$$

$$
H(X, Y) = E[-\log p(X, Y)]
$$

$$
H(Y|X)= - \sum_{x \in X} \sum_{y \in Y} p(x, y) \log(p(y|x))
$$

$$
H(X, Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)
$$

$$
H(X, Y|Z) = H(X|Z) + H(Y|X, Z)
$$

## Relative Entropy and Mutual Information

💡 The relative entropy $D(p||q)$ is a measure of the inefficiency of assuming that the distribution is $q$ when the true distribution is $p$. For example, if  we used code for a distribution $q$, we would need $H (p) + D(p||q)$ bits on the average to describe the random variable $q$.

$$
D(p||q) = \sum_{x \in X} p(x) \log \frac{p(x)}{q(x)}
$$

![H(XY).png|center |500](H(XY).png)

### Relations

- $I(X;Y)= D(p(x, y) || p(x)q(x))$
- $I(X;Y) = H(X) + H(Y) - H(X, Y)$
- $I(X;Y) = H(Y) - H(Y | X)$
- $I(X;Y) = H(X) - H(X | Y)$
- $I(X;Y) = I(Y;X)$
- $I(X;X) = H(X)$

$$
\begin{align*}
I(X;Y|Z)&=H(X|Z)-H(X|Y,Z) = H(Y|Z) - H(Y|X,Z)\\ &= H(X|Z) + H(Y|Z) - H(X,Y|Z) \\
&=E_{p(x,y,z)}\log\frac{p(x,y|z)}{p(x|z)p(y|z)}
\end{align*}
$$

### Chain Rule

$$
H(X_1, X_2, \ldots, X_n) = \sum_{\forall i} H(X_i | X_{i - 1} , \ldots, X_1)
$$

$$
I(X_1,X_2,\ldots;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},X_{i-2},\ldots,X_1)
$$

$$
D(p(X_1,\ldots,X_n)||q(X_1,\ldots,X_n))\\=\sum_{i=1}^nD(p(X_i|X_{i-1},\ldots,X_1)||q(X_i|X_{i-1},\ldots,X_1))
$$

## Inequalities

$$
f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) + (1-\lambda) f(x_2)
$$

A function $f(x)$ is said to be **convex** over an interval $(a, b)$ if, $\forall x_1, x_2 \in (a, b)$ and $\lambda \in [0, 1]$ if the above holds.

$$
D(\lambda p_1 +(1-\lambda)p_2|| \lambda q_1 +(1-\lambda)q_2) \leq  \lambda D(p_1||q_1)+(1-\lambda)D(p_2||q_2)
$$

### Theorems

- If $f$ has a second derivative which is non-negative (or positive) everywhere, then the function is convex (or strictly convex).
    - Proof
        
        Let $a<b$ be two points,
        
        $$
        \begin{align*}
        1&=\frac{x-a}{b-a}+\frac{b-x}{b-a}\\
        \Rightarrow f(x)&=\frac{x-a}{b-a}f(x)+\frac{b-x}{b-a}f(x)
        \end{align*}
        $$
        
        The secant line between points $a$ and $b$ is defined as,
        
        $$
        L_{a,b}(x)=f(a)+\frac{x-a}{b-a}\left(f(b)-f(a)\right)\text{ for }a<x<b
        $$
        
        Then we get
        
        $$
        \begin{align*}
        L_{a,b}(x)-f(x)&=f(a)+\frac{x-a}{b-a}\left(f(b)-f(a)\right)-f(x)\\
        &=\frac{b-x}{b-a}f(a)+\frac{x-a}{b-a}f(b)-\frac{b-x}{b-a}f(x)-\frac{x-a}{b-a}f(x)\\
        &=\frac{x-a}{b-a}\left(f(b)-f(x)\right)-\frac{b-x}{b-a}\left(f(x)-f(a)\right)\\
        &=\frac{(x-a)(b-x)}{b-a}\left(\frac{f(b)-f(x)}{b-x}-\frac{f(x)-f(a)}{x-a}\right)
        \end{align*}
        $$
        
        Now according to Mean Value Theorem (MVT), $\exists c_1,c_2$ such that $a<c_1<x<c_2<b$ and 
        
        $f'(c_1)=\frac{f(x)-f(a)}{x-a},f'(c_2)=\frac{f(b)-f(x)}{b-x}$
        
        $$
        \begin{align*}
        \therefore L_{a,b}(x)-f(x)&=\frac{x-a}{b-a}\left(f(b)-f(x)\right)-\frac{b-x}{b-a}\left(f(x)-f(a)\right)\\
        &=\frac{(x-a)(b-x)}{b-a}\left(f'(c_2)-f'(c_1)\right)\\
        &=\frac{(x-a)(b-x)(c_2-c_1)}{b-a}\times\frac{f'(c_2)-f'(c_1)}{c_2-c_1}\\
        &=\frac{(x-a)(b-x)(c_2-c_1)}{b-a}f''(c)\\
        \therefore f(x)&\le L_{a,b}(x)\\
        &=f(a)+\frac{x-a}{b-a}\left(f(b)-f(a)\right)\\
        &=\frac{b-x}{b-a}f(a)+\frac{x-a}{b-a}f(b)\\
        \therefore f(\lambda a+(1-\lambda)b)&\le\lambda f(a)+(1-\lambda)f(b)
        \end{align*}
        $$
        
        Hence, $f$ is a convex function.
        
- If $f$ is a convex function and $x$ is a random variable, then $E[f(x)] \geq f(E[x])$, where $E$ denotes expectation value.
    - Proof
        
        Consider a discrete random variable $X$
        
        By definition, we know that when $X$ has two-mass-point distribution $p_1f(x_1)+p_2f(x_2)\ge f(p_1x_1+p_2x_2)\Rightarrow E[f(x)] \geq f(E[x])$. This will be the base case for induction.
        
        Now, let this inequality be true when $X$ has $k-1$ mass-points.
        
        That is, $E[f(x)] \geq f(E[x]) \Rightarrow\sum_{r=1}^{k-1}p_rf(x_r)\ge f\left(\sum_{r=1}^{k-1}p_rx_r\right)$.
        
        We consider a random variable $Y$ with $k-1$ mass-points where $y_1=x_1,y_2=x_2,\ldots y_{k-1}=x_{k-1}$ and $\forall1\le r\le k-1,p'_r=\frac{p_r}{1-p_k}$
        
        $$
        \begin{align*}
        \therefore\sum_{r=1}^{k-1}p'_rf(y_r)&\ge f\left(\sum_{r=1}^{k-1}p'_ry_r\right)\\
        \Rightarrow\sum_{r=1}^kp_rf(x_r)&\ge p_kf(x_k)+(1-p_k)f\left(\sum_{r=1}^{k-1}p'_rx_r\right)\\
        \Rightarrow\sum_{r=1}^kp_rf(x_r)&\ge f\left(p_kx_k+(1-p_k)\sum_{r=1}^{k-1}p'_rx_r\right)\\
        &=f\left(\sum_{r=1}^kp_rx_r\right)\\
        \Rightarrow E[f(x)] \geq f(E[x])
        \end{align*}
        $$
        

### Log sum Inequality

We have the following,

$$
\displaystyle \sum_{i=1}^n a_i \log{\dfrac{a_i}{b_i}} \geq \left(\sum_{i=1}^n a_i \right) \log{\dfrac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}}
$$

with equality if and only if $\dfrac{a_i}{b_i}$ is a constant.

$$
\left(0\log0=0,a\log\frac{a}{0}=\infty\text{ for }a>0,0\log\frac{0}{0}\right)
$$

- Proof
    
    WLG consider $a_i>0,b_i>0$
    Consider the function $f(x)=x\log x$.
    
    $$
    f''(x)=\frac{1}{x}
    $$
    
    Thus, $f$ is strictly convex when $x$ is positive. And hence,
    
    $$
    \sum t_if(x_i)\ge f\left(\sum t_ix_i\right)\text{ for }t_i\ge0,\sum_it_i=1\text{ (by Jensen's Inequality)}
    $$
    
    Now consider $t_i=\frac{b_i}{\sum_j b_j}$ and $x_i=\frac{a_i}{b_i}$. Now we get,
    
    $$
    \begin{align*}
    \sum_i\frac{b_i}{\sum_jb_j}\times\frac{a_i}{b_i}\log\frac{a_i}{b_i}&\ge\sum_i\frac{b_i}{\sum_jb_j}\times\frac{a_i}{b_i}\log\left(\sum_i\frac{b_i}{\sum_jb_j}\times\frac{a_i}{b_i}\right)\\
    \Rightarrow\frac{1}{\sum_jb_j}\sum_ia_i\log\frac{a_i}{b_i}&\ge\frac{1}{\sum_jb_j}\sum_ia_i\log\left(\frac{1}{\sum_jb_j}\sum_ia_i\right)\\
    \Rightarrow\sum_ia_i\log\frac{a_i}{b_i}&\ge\left(\sum_ia_i\right)\log\frac{\sum_ja_j}{\sum_jb_j}
    \end{align*}
    $$
    

### Concavity

- $H(p)$ is a convex function of $p$.
- $H(p) = \log(X) - D(p||u)$ where $u$ is the uniform distribution on $|X|$ outcomes.
- The mutual information $I (X; Y )$ is a concave function of $p(x)$ for fixed $p(y|x)$ and a convex function of $p(y|x)$ for fixed $p(x)$.