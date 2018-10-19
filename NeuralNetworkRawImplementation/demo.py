import neural_network as nn

data_set = [[2.7810836, 2.550537003, 0],
            [1.465489372, 2.362125076, 0],
            [3.396561688, 4.400293529, 0],
            [1.38807019, 1.850220317, 0],
            [3.06407232, 3.005305973, 0],
            [7.627531214, 2.759262235, 1],
            [5.332441248, 2.088626775, 1],
            [6.922596716, 1.77106367, 1],
            [8.675418651, -0.242068655, 1],
            [7.673756466, 3.508563011, 1]]

train = data_set
test = train[4:6]

n_inputs = 2   # number of features
n_hidden_layers = 1  # how many hidden layers
n_hidden_neurons = 5  # how many neuron per hidden layer
n_outputs = 2  # number of classes
my_neural_network = nn.initialize_network(n_inputs, n_hidden_layers, n_hidden_neurons, n_outputs)
n_epoch = 40
l_rate = .3
nn.train_the_network(my_neural_network, train, l_rate, n_epoch, n_outputs)
for row in test:
    predict = nn.predict(my_neural_network, row)
    print('actual=>', row[-1], 'predicted=>', predict)