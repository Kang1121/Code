from functions import *
import matplotlib.pyplot as plt
import math


def model(X, Y, layers_dims, lamd=0, learning_rate=0.01, num_iterations=4000):
    np.random.seed(1)
    costs = []
    lr = learning_rate
    parameters = initialize_parameters_deep(layers_dims)
    for i in range(0, num_iterations):
        AL, caches = whole_layers_forward(X, parameters)
        cost = compute_cost(AL, Y, parameters, lamd)
        grads = whole_layers_backward(AL, Y, caches, lamd)
        parameters = update_parameters(parameters, grads, lr)
        if i % 500 == 0:
            lr = lr * math.pow(0.95, i / 500)
        if i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))
        if i % 100 == 0:
            costs.append(cost)

    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundred)')
    plt.title("Learning rate =" + str(lr))
    plt.show()
    return parameters
