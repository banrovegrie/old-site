## Problem
---
- Classification of Absolutely Separable States (ABSEP).
- Relations between different Absolute Classes.
- Find examples to settle the following question with high confidence.

$$
\text{Absolute PPT} \overset{?}{=} \text{ABSEP}
$$
## Initial Ideas
---
**March 1, 2022**

1. Generate absolutely separable states using absolutely separating maps and channels.
2. Read the paper on such state generating maps ([https://arxiv.org/abs/1703.00344](https://arxiv.org/abs/1703.00344)).
3. Once we have an absolutely separable state, we apply unitary operations over it to generate other absolutely separable states.
4. Are there clusters of absolutely separable states? If there are clusters then we definitely need data spanning all such clusters or some procedure to ensure unbaised sampling of density matrices from possible clusters.
5. To create non absolutely separable states, we shall use pure product states cause they can definitely be converted into entangled states.
6. Do preprocessing on entanglement criteria and build features to pass into a possible classifier along with the matrix (density matrix) itself.
7. Read the Absolute PPT paper ([https://arxiv.org/pdf/1405.5853.pdf](https://arxiv.org/pdf/1405.5853.pdf)) and the $2\otimes d$ paper ([https://arxiv.org/abs/1911.13145](https://arxiv.org/abs/1911.13145)).

## Tasks
---
**April 1, 2022**

Computational:

1. Data for different forms of entanglement
2. SEP classifier
3. Absolutely separating channel implementation
4. Data for absolutely separable states
5. ABSEP classifier
6. Benchmarking ML models (supervised and unsupervised)
7. Absolutely local or unsteerable states classifier
8. ACVENN classifier

Analytical:

1. $3 \otimes 3$ ABSEP problem
2. $3 \otimes d$ ABSEP problem

## Meeting Notes
---
**July 2, 2022**

- [ ]  Generation of data for absolutely separable states (validation)
    - Use random unitaries to generate data with high confidence
    - Compare deviations wrt the known $2 \times 2$ case
    - Try for $3 \times 3$ case (figure out if $\exists$ entangled Absolutely PPT states)
- [x]  Implementing pseudo-siamese NN for unsupervised learning
- [ ]  Figure out how to get a description of the classification boundary from the classifier
- [ ]  Further work on Implementation of a classifier for SEP based on extendibility (based on semidefinite programming definition of the problem)
- [ ]  ACVENN
- [ ]  Model based on absolute unsteerability

## On Using OC-SVM
---
As discussed last meeting we have a way to generate "probably" absolute separable states. But to use that for training, we would need something like a non-linear One-Class Classifier ([https://en.wikipedia.org/wiki/One-class_classification](https://en.wikipedia.org/wiki/One-class_classification)) or Anomaly Detector. In that regard, OCSVM appears to be quite promising to our problem.