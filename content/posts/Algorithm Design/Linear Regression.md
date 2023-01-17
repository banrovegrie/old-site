Here, is the required report in PDF format. Compiled by Alapan Chaudhuri and Kunwar Shaanjeet Singh Grover.

# Linear Regression in sklearn
---

> Write a brief about what function does the method, LinearRegression().fit() performs.

`LinearRegression()` is a model that fits a one degree function onto the given data.

To fit the model we call `LinearRegression().fit($\mathbf{X}, \mathbf{y}$)`  where $\mathbf{X}$ is the matrix whose rows are the input attributes and $\mathbf{y}$ is the target vector.

The $i^{th}$ row of $\mathbf{X}$ are the attributes whose target value is $i^{th}$ element of $\mathbf{y}$.

## How does it fit?
---
The model finds the perfect linear fit by minimizing the mean squared error by performing gradient descent. The error which has to be minimized is defined as:

$$\mathbf{E} = \frac{(\mathbf{y} - (\mathbf{W}^T \mathbf{x} + \mathbf{b}))^T(\mathbf{y} - (\mathbf{W}^T \mathbf{x} + \mathbf{b}))}{\mathbf{N}}
$$

where, $\mathbf{N}$ is the number of data points in the data.

### Numerical method of solving

Rather than calculating the derivates and finding the minima of the cost function, which is computationally very heavy for datasets which have a lot of attributes, `LinearRegression()` performs **gradient descent.**

Gradient descent has a starting point at which it calculates the gradient and takes a "step" in the opposite direction. The point it arrives to is the next point from which the process is repeated till it reaches a minima.

Although this method is susceptible to errors when the data is noisy, in general this method works and is used by `LinearRegression()` to fit the data and minimize the cost.

## Performing Polynomial Regression
---
Performing preprocessing on the data to convert the attributes to polynomial attributes can be done after which performing linear regression will be equivalent to polynomial regression.

### Polynomial transformation

To perform a polynomial regression, we first transform the input vector to its higher degree vector. for a 1 attribute input, its quadratic formation will be:

$$x \rightarrow [ x, x^2]
$$

A more complicated example is as follows:

$$\begin{pmatrix} x\\y\end{pmatrix} \rightarrow \begin{pmatrix} x & y & xy & x^2 & y^2 \end{pmatrix}$$

### Linear regression

Now the input for the linear regression will be the output of the polynomial transformation. Linear regression will treat the values as different attributes. 

For example:

$$x \rightarrow [x, x^2] \rightarrow b + w_1x + w_2x^2$$

Linear regression will find the best parameters which are nothing but the coefficients of the required polynomial.

Doing polynomial transformation followed by Linear Regression is no different than doing polynomial regression.

### Output calculation

When calculating the output, we first convert the input attributes to their higher degrees and then those values are then fit onto the regression model.

## Averaging over all data-points
---
Since $\text{bias}^2, \text{variance \& mean squared error}$ are calculated for each point, we take their average over all the points to obtain the aggregate over the complete test data set.

# Results
---
### Visualization of Training Data

![Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled.png](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled.png)

### Visualization of Test Data

![Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%201.png](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%201.png)

## Batching

---

Given data was in 2 different files, test and train. Training data was split into 10 random batches, the data was then plotted, as you can see it was randomly distributed giving us less dense versions of the training set. We create a model of each degree by fitting each data set.

### Visualizing fit over Test Data

Please check `code.ipynb` for all the plots. Here, I am putting down only the first 3 and the last 3 plots.

![ **Degree 1, 2 and 3 respectively**](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%202.png)

 **Degree 1, 2 and 3 respectively**

It can be noticed that all the fits after degree 3 are quite similar. As we go even higher (in terms of degree), there arises some level of overfitting which can be noticed in the plots below.

![**Degree 18, 19 and 20 respectively**](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%203.png)

**Degree 18, 19 and 20 respectively**

## Tabulation of the Error Values
---
> Tabulate the values of bias, variance and irreducible error, as obtained for different degrees.

![Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%204.png](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%204.png)

The general trend is that *Bias decreases a lot relatively (and then increases after degree 10)*, *Variance increases*, and *MSE dips and goes back up*. This is because a lower-degree polynomial will underfit the data (you can observe the values of bias and variance for degrees 1 and 2). A higher-degree polynomial will tend to overfit the data. This is the cause for the inaccuracy in polynomials of degree 15 and more.

The later increase (at higher degrees) in Bias and Bias Squared may also be contributed due to fractional errors (during computation/calculation).

Whereas the irreducible error as expected stays the same, and since we can see that test data is very structured, there is almost no irreducible error.

To have a better understanding it is better to plot these points on a plot.

### Plotting the Error Values

> Based on the variance, bias and total error calculated in earlier tasks, plot the $\text{Bias}^2$-$\text{Variance}$ tradeoff graph.
> 

![Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%205.png](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%205.png)

As expected, the drop in error and the minimum occurs at degree 3 since the test data resembles a degree 3 polynomial. Anything below degree 3, massively underfits the given test data.

![Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%206.png](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%206.png)

Also, after degree 10, the behavior of data is pretty interesting. In this case, we have our test data as a 3 degree polynomial and we are trying to fit a higher degree polynomial.

This means that the higher order approximations probably would not be smooth since the training data itself is so broad and the functions have such a large domain.

This results in undesirable effects of overfitting and the bias increases.

![Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%207.png](Algorithm%20Design/images/Linear%20Regression%208d793f8885724a84a459e4d3f34101b4/Untitled%207.png)