import numpy as np

class NeuralNetwork(object):


    def __init__(self, layer_sizes):
        """
        The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers.
        """
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:], layer_sizes[:-1])]
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in weight_shapes]
        self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]


    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for w, b in zip(self.weights, self.biases):
            a = self.sigmoid(np.matmul(w,a) + b)
        return a

    '''
    def print_accuracy(self, images, labels):
        predictions = self.feedforward(images)
        num_correct = sum([np.argmax(a) == np.argmax(b) for a,b in zip(predictions,labels)])
        print(f'{num_correct}/{len(images)} accuracy: {100*num_correct/len(images)}%')
    '''

    @staticmethod
    def sigmoid(z):
        """The sigmoid activation function."""
        return 1 / (1 + np.exp(-z))


if __name__ == '__main__':
    layer_sizes = (300,500,100)
    x = np.ones((layer_sizes[0],1))

    net = NeuralNetwork(layer_sizes)
    prediction = net.feedforward(x)
    print(prediction)