A single qubit operator can be represented as $U = a_0I + a_1X + a_2Y +a_3Z$.

Also, such a unitary can also be represented this way,

$$
U = \begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

and thus, we obtain the following equivalences.

$$
a_0 = (a+d)/2,\ a_1 = (b+c)/2,\\ a_2 = (c-b)/2i,\ a_3 = (d-a)/2
$$

Also from $UU^\dagger = I$ we get,

$$
|a_0|^2 + |a_1|^2 + |a_2|^2 + |a_3|^2 = 1$$
$$
a^∗_0a_1+a^∗_1a_0+ia^∗_2a_3−ia^∗_3a_2 = 0$$
$$
a^∗_0a_2−ia^∗_1a_3+a^∗_2a_0+ia^∗_3a_1 = 0$$
$$
a^∗_0a_3+ia^∗_1a_2−ia^∗_2a_1+a^∗_3a_0 = 0
$$
where we define $|a_0| = cos(\theta/2)$ then $|a_1|^2 + |a_2|^2 + |a_3|^2 = |sin(\theta/2)|$.

Then define,

$$
n_x = |a_1|/|sin(\theta/2)|\\
n_y = |a_2|/|sin(\theta/2)|\\
n_z = |a_3|/|sin(\theta/2)|
$$

and further we get $n_x^2 + n_y^2 + n_z^2 = 1$.

Now, we define $exp(iα) =a_0/cos(θ/2)$ and denote the phase of $a_1,a_2,a_3$ as $α_1,α_2,α_3$ respectively.

By putting these in the other constraints we get, $α_1=α_2=α_3=α−π/2$.

$$
a_0 = e^{i\alpha}cos(\theta/2),$$
$$
a_1 = -ie^{i\alpha}sin(\theta/2)n_x,$$
$$
a_2 = -ie^{i\alpha}sin(\theta/2)n_y,$$
$$
a_3 = -ie^{i\alpha}sin(\theta/2)n_z
$$

$$
U= e^{iα}(\cos(\frac{θ}{2})I − i\sin(\frac{\theta}{2})(n_xX+n_yY+n_zZ))= e^{iα}R_{\hat n}(θ)
$$