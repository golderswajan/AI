import random as rn
from math import exp


# Network Initializer
def initialize_network(n_inputs, n_hidden_layers, n_hidden_neurons, n_outputs):
    rn.seed(1)
    network = list()
    for k in range(n_hidden_layers):
        if k == 0:
            hidden_layer = [{'weights': [rn.random() for i in range(n_inputs + 1)]} for i in range(n_hidden_neurons)]
        else:
            hidden_layer = [{'weights': [rn.random() for i in range(n_hidden_neurons + 1)]} for i in range(n_hidden_neurons)]
        network.append(hidden_layer)
    output_layer = [{'weights':[rn.random() for i in range(n_hidden_neurons + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network


# Neuron Value Calculation
def measure_neuron_value(weights, inputs):
    value = weights[-1]
    for i in range(len(weights)-1):
        value += weights[i]*inputs[i]
    return value


# Sigmoid Activation Function
def activation(value):
    return 1.0/(1.0+exp(-value))


# Feed Forwarding
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = list()
        for neuron in layer:
            neuron_value = measure_neuron_value(neuron['weights'], inputs)
            # print('value=>', neuron_value)
            neuron['output'] = activation(neuron_value)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# Transfer Derivative
def transfer_derivative(output):
    return output*(1.0-output)


# Backpropagate Error and Store in Neuron
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        """Output Layer Neurons"""
        if i == len(network)-1:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j]-neuron['output'])
        # """ Other Layer Neurons """
        else:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i+1]:
                    error += neuron['delta'] * neuron['weights'][j]
                errors.append(error)
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j]*transfer_derivative(neuron['output'])


# """ Update the weights with errors"""
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i-1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate*neuron['delta']*inputs[j]
            neuron['weights'][-1] += l_rate * neuron['delta']


# Network Training
def train_the_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        # print('epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


# Predict Function
def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))
