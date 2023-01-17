# Differentials

---

- $df = f_xdx + f_ydy+f_zdz$
- $df \neq \Delta f$
- $\Delta f =  f_x\Delta x + f_y\Delta y + f_z\Delta z$
- $df$ is used to encode infinitesimal changes
- used to act as a placegolder value
- divide wrt time to get rate of change $\rightarrow$ CHAIN RULE

## Chain Rule with More Variables

Let $w = f(x, y)$ when $x(u, v), y(u, v)$ then,

$$
dw = f_x dx + f_y dy = (f_xx_u+ f_yy_u)du + (f_xx_v+ f_yy_v)dv = \frac{\partial f}{\partial u}du + \frac{\partial f}{\partial v}dv
$$

# Gradient Vector

---

$$
\frac{dw}{dt} = w_x \frac{dx}{dt} + w_y \frac{dy}{dt} + w_z \frac{dz}{dt} = \vec{\nabla} w.\frac{d\vec{r}}{dt}
$$

Note: $\vec{\nabla}w \ \perp \text{ level surfaces}$ (tangent to the level surface at any given point)

# Directional Derivatives

---

$$
\frac{dw}{ds}|_{\hat{u}} = \vec{\nabla}w \cdot \frac{d\vec{r}}{ds} = \vec{\nabla}w \cdot \hat{u}
$$

## Implications

Direction of $\vec{\nabla}w$ is the direction of fastest increase of $w$

# Lagrange Multipliers

---

Goal: minima/maximize a multi-variable function ($min/max\ \  f(x, y, z)$) where $x, y, z$ are not independent and $\exists$ $g(x, y, z) = c$.

These can be obtained on combining the given restraints with the following.

$$
\vec{\nabla}f = \lambda \vec{\nabla}g
$$

Basic idea: to find $(x, y)$ where the level curves of $f$ and $g$  are tangent to each other ($\vec{\nabla}f \parallel \vec{\nabla}g$). 

Note: Take care that the point is indeed a maxima or minima as required and not just a saddle point (second derivative test won't be applicable so be vigilant).