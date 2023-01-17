| Functions | Example | Value | First derivative | Second derivative |
| --- | --- | --- | --- | --- |
| $f: \mathbb R \to \mathbb R$ | $x^2$ | $\mathbb R$ | $\mathbb R$ | $\mathbb R$ |
| $f: \mathbb R^d \to \mathbb R$ | loss function | $\mathbb R$ | $\mathbb R^d [\text{gradient}]$ | $\mathbb R^{d\times d} [\text{hessian}]$ |
| $f: \mathbb R^d \to \mathbb R^p$ | neural net layer | $\mathbb R^p$ | $\mathbb R^{d \times p} [\text{jacobian}]$ | $\mathbb R^{d \times p \times p}$ |

### Gradient

$$
\nabla_x f(x) = \nabla_x f(x_1, \cdots, x_d) = \begin{bmatrix}
\frac{\partial f(x)}{\partial x_1}\\
\vdots\\
\frac{\partial f(x)}{\partial x_d}
\end{bmatrix}
$$

$$
\nabla_Af(A) = \begin{bmatrix}
\frac{\partial f(A)}{\partial A_{11}} & \cdots\\
\vdots & \vdots\\
\cdots & \frac{\partial f(A)}{\partial A_{mn}}
\end{bmatrix}
$$

### Hessian

We have $f: \mathbb R^d \to \mathbb R^p$ thus, $f(x_1, \cdots, x_d) = \begin{bmatrix}
f_1(x_1, \cdots, x_d)\\
\vdots \\ f_p(x_1, \cdots, x_d)
\end{bmatrix}$

Note: Hessians are square-symmetric matrices.

$$
\nabla_x^2 f(x) = \begin{bmatrix}
\frac{\partial^2f(x)}{\partial x_1^2} & \frac{\partial^2f(x)}{\partial x_1x_2} & \cdots\\
\vdots & \ddots & \vdots \\
\vdots &\cdots & \frac{\partial^2f(x)}{\partial x_n^2}
\end{bmatrix}
$$

### Jacobian

$$
J = \begin{bmatrix}  \dfrac{\partial \mathbf{f}}{\partial x_1} & \cdots & \dfrac{\partial \mathbf{f}}{\partial x_d}\end{bmatrix}= \begin{bmatrix}  \nabla^{\mathrm T} f_1 \\    \vdots \\  \nabla^{\mathrm T} f_p   \end{bmatrix}= \begin{bmatrix}    \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n}\\    
\vdots                             & \ddots & \vdots\\    \dfrac{\partial f_p}{\partial x_1} & \cdots & \dfrac{\partial f_p}{\partial x_d}\end{bmatrix}
$$

where $\nabla^{\mathrm T} f_i$ is the transpose (row vector) of the gradient of the $i$ component.

### Examples

- $\nabla_xb^Tx = b$
- $\nabla_x^2 b^Tx = 0$
- $\nabla_xx^TAx = 2Ax$, if $A$ is symmetric
- $\nabla_x^2x^TAx = 2A$, if $A$ is symmetric