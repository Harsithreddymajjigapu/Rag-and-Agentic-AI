 - this gives us output of the probability between one and zero 
 - **Logistic Regression: Understanding the Linear Combination of Weights and Inputs**

# Logistic Regression Notes

## Linear Combination of Weights and Inputs

In logistic regression, we compute a weighted sum of the input features and add a bias term:

`z=wTx+bz = w^T x + b`

Where:

- w is the weight vector (parameters of the model)
- x is the input feature vector
- b is the bias term
- z is the result of the linear combination

This value z is then passed through a sigmoid function σ(z)\sigma(z) to produce a probability:

`y^=σ(z)=11+e−z\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}`

## Sigmoid Function Properties

- If z is large, σ(z)≈1\sigma(z) approx. 1
- If z is very small (large negative), σ(z)≈0\sigma(z) approx. 0
- The output of σ(z)\sigma(z) always lies in the range (0,1)(0,1), making it suitable for binary classification.