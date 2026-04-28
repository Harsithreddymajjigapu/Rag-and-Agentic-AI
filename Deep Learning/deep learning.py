import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Dataset Preparation
data = load_breast_cancer()
X = data.data.T  # shape: (features, samples)
Y = data.target.reshape(1, -1)  # shape: (1, samples)

# Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X.T).T

# Train-test split (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X.T, Y.T, test_size=0.2, random_state=42)
X_train, X_test = X_train.T, X_test.T
Y_train, Y_test = Y_train.T, Y_test.T

# Activation Functions
def sigmoid(Z):
    A = 1 / (1 + np.exp(-Z))
    return A, Z

def relu(Z):
    A = np.maximum(0, Z)
    return A, Z

def relu_backward(dA, Z):
    dZ = np.array(dA, copy=True)
    dZ[Z <= 0] = 0
    return dZ

def sigmoid_backward(dA, Z):
    s = 1 / (1 + np.exp(-Z))
    return dA * s * (1 - s)

# Initialization 
def initialize_parameters_deep(layer_dims):
    np.random.seed(3)
    parameters = {}
    for l in range(1, len(layer_dims)):
        parameters[f"W{l}"] = np.random.randn(layer_dims[l], layer_dims[l-1]) * np.sqrt(2. / layer_dims[l-1])
        parameters[f"b{l}"] = np.zeros((layer_dims[l], 1))
    return parameters

# Forward Propagation
def linear_forward(A, W, b):
    Z=np.dot(W,A)+b
    return Z, (A, W, b)

def linear_activation_forward(A_prev, W, b, activation):
    Z, linear_cache = linear_forward(A_prev, W, b)
    A, activation_cache = (relu(Z) if activation == "relu" else sigmoid(Z))
    return A, (linear_cache, activation_cache)

def L_model_forward(X, parameters):
    A = X
    caches = []
    L = len(parameters) // 2

    for l in range(1, L):
        A, cache = linear_activation_forward(A, parameters[f"W{l}"], parameters[f"b{l}"], "relu")
        caches.append(cache)
    
    AL, cache = linear_activation_forward(A, parameters[f"W{L}"], parameters[f"b{L}"], "sigmoid")
    caches.append(cache)

    return AL, caches

# Cost Function
def compute_cost(AL, Y):
    m = Y.shape[1]
    cost=-1/m*np.sum(Y*np.log(AL)+(1-Y)*np.log(1-AL))
    cost = np.squeeze(cost)
    return cost

# Backward Propagation
def linear_backward(dZ, cache):
    A_prev, W, _ = cache
    m = A_prev.shape[1]
    dW=1/m*np.dot(dZ,A_prev.T)
    db=1/m*np.sum(dZ,axis=1,keepdims=True)
    dA_prev=np.dot(W.T,dZ)
    return dA_prev, dW, db

def linear_activation_backward(dA, cache, activation):
    linear_cache, activation_cache = cache
    dZ = relu_backward(dA, activation_cache) if activation == "relu" else sigmoid_backward(dA, activation_cache)
    return linear_backward(dZ, linear_cache)

def L_model_backward(AL, Y, caches):
    grads = {}
    L = len(caches)
    dAL=-(np.divide(Y,AL)-np.divide(1-Y,1-AL))

    grads["dA" + str(L - 1)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(
        dAL, caches[L - 1], "sigmoid"
    )

    for l in reversed(range(L - 1)):
        dA_prev, dW, db = linear_activation_backward(grads[f"dA{l + 1}"], caches[l], "relu")
        grads[f"dA{l}"], grads[f"dW{l + 1}"], grads[f"db{l + 1}"] = dA_prev, dW, db

    return grads

#Update Parameters
def update_parameters(parameters, grads, learning_rate):
    L = len(parameters) // 2
    for l in range(1, L + 1):
        parameters[f"W{l}"] -= learning_rate * grads[f"dW{l}"]
        parameters[f"b{l}"] -= learning_rate * grads[f"db{l}"]
    return parameters

# Model Training
def model(X, Y, layers_dims, learning_rate=0.0075, num_iterations=3000, print_cost=False):
    parameters = initialize_parameters_deep(layers_dims)

    for i in range(num_iterations):
        AL, caches = L_model_forward(X, parameters)
        cost = compute_cost(AL, Y)
        grads = L_model_backward(AL, Y, caches)
        parameters = update_parameters(parameters, grads, learning_rate)

        if print_cost and i % 100 == 0:
            print(f"Cost after iteration {i}: {cost:.4f}")
    return parameters

# Prediction
def predict(X, parameters):
    AL, _ = L_model_forward(X, parameters)
    return (AL > 0.5).astype(int)

#  Run the Model
layers_dims = [X_train.shape[0], 10, 5, 1]
parameters = model(X_train, Y_train, layers_dims, num_iterations=2500, print_cost=True)

#  Evaluation 
train_preds = predict(X_train, parameters)
test_preds = predict(X_test, parameters)

train_accuracy = np.mean(train_preds == Y_train) * 100
test_accuracy = np.mean(test_preds == Y_test) * 100

print(f"Training Accuracy: {train_accuracy:.2f}%")
print(f"Test Accuracy: {test_accuracy:.2f}%")
