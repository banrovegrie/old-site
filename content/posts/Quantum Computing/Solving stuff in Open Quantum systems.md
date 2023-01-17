## Choi's Theorem

Let $\mathcal E :\mathbb {C} ^{n\times n}\to \mathbb {C} ^{m\times m}$ be a linear map. Then, the following are equivalent:

- $\mathcal E$ is $n$-positive (i.e. $\mathcal E(A)\in \mathbb {C} ^{m\times m}$ is positive whenever $A\in \mathbb {C} ^{n\times n}$ is positive).
- The matrix $\Gamma_\mathcal E$, sometimes called the Choi matrix, is positive. Here the state $\phi$ is maximally entangled.
    
    $$
    \Gamma_{\mathcal E}=\left(\operatorname {id} _{n}\otimes \mathcal E \right)\left(\vert \phi \rangle\langle \phi \vert\right)
    $$
    
- $\mathcal E$ is completely positive.

## Solving a Lindblad Equation

Any ideal open quantum system will undergo Markovian dynamics provided that its evolution satisfies a Master equation.

$$
\frac{d\rho}{dt} = \mathcal L(\rho) = -i[H, \rho] + \sum_k \gamma_k (V_k\rho V_k^\dagger - \frac{1}{2} \{V_k^\dagger V_k, \rho\})
$$

Let $\rho = \frac{1}{2}(I + \vec r \cdot \vec \sigma)$ and differentiate $\rho(t)$ to obtain $\dot \rho(t)$ in terms of $\frac{d\vec{r}}{dt}$.

$$
\frac{d\rho}{dt} = \frac 1 2 (\dot r_x\sigma_x + \dot r_y\sigma_y + \dot r_z\sigma_z)
$$

We equate $\dot \rho = \mathcal L(\rho)$ using the above representation for $\dot \rho$ and $\rho$ and solve the equation by solving the individual differential equations obtained. After we solve for $\rho$, we obtain $\Lambda_t$.

$$
\Lambda_t: \rho_0 \to \rho_t \text{,~~~~~} \rho(t) = \Lambda_t(\rho(0))
$$

Now, with Choi's theorem we check if $\Lambda_t$ is $CP$ by checking whether $\Gamma_\Lambda$ is positive semi-definite.

$$
\Gamma_\Lambda = C\vert\psi\rangle\langle\psi\vert
$$

$$
C = (I \otimes \Lambda_t)
$$

Now, we find the eigenvalues and eigenvectors of $C$ and represent it as $C = \sum_i \lambda_i\vert v_i\rangle$. Then, we can obtain Kraus operators $\{K_i\}_{\forall i}$ such as follows (check below).

$$
v_{i} = \begin{bmatrix}
-1/2\\1/2\\-1/2\\1/2
\end{bmatrix} \implies K_i = \sqrt{\lambda_i}
\begin{bmatrix}
-1/2 & -1/2\\1/2 & 1/2
\end{bmatrix}
$$