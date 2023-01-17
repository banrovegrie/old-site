## CHSH Inequality

---

In a classical experiment, we have the following setup where Alice can choose to measure either Q or R and Bob chooses either S or T. The measurements are performed imultaneously and far off from each other.

![Bell's%20Inequality%20213b80330bfc4779a2c61a0f477b27fa/Untitled.png](Quantum%20Computing/images/Bell's%20Inequality/Untitled.png)

$$
E(QS) + E(RS) + E(RT) - E(QT) = E(QS + RS + RT-QT)\\

$$

$$
\implies E(QS) + E(RS) + E(RT) - E(QT) = \sum_{q,r,s,t}p(q, r, s, t)(qs + rs + rt - qt)\\

$$

$$
\implies E(QS) + E(RS) + E(RT) - E(QT) \leq \sum_{q,r,s,t}p\times 2 = 2
$$

and thereby we obtain the inequality $E(QS) + E(RS) + E(RT) - E(QT) \leq 2$.

This is one of the set of Bell inequalities, the first of which was found by John Bell. This one in particular is named CHSH inequality.

## Quantum Anomaly

---

In the quantum case, let us consider the measurements to be based on the following observables over the EPR pair $|\psi\rangle = \frac{|01\rangle - |10\rangle}{\sqrt 2}$.

$$
Q = Z_1, R= X_1,\\
S = \frac{-Z_2-X_2}{\sqrt 2},\\
T = \frac{Z_2 - X_2}{\sqrt 2}
$$

Then, we have the following result.

$$
E(QS) + E(RS) + E(RT) - E(QT) = \frac{1}{\sqrt 2} + \frac{1}{\sqrt 2} + \frac{1}{\sqrt 2} - \frac{1}{\sqrt 2} = 2\sqrt 2 > 2
$$

Thus, in other words, CHSH inequality doesn't hold. 

## Interpretation

---

The fact that CHSH doesn't hold in the quantum scenario implies that two of the major assumptions about nature is wrong in case of the classical experiment.

The assumptions are:

- Realism: Q, R, S, T are physical quantities which have defininte values irrespective of observation.
- Locality: Alice's measurement doesn't influence that of Bob's.

Thus, the result of CHSH being false when accounted for the quantum mechanical properties of nature (we can perform the experiment in a lab with particles) suggests that nature cannot be locally real and neither can any true mathematical representation of it be locally real.