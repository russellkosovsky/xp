import numpy as np

# Activation function: Sigmoid
def sigmoid(x):
    """Compute sigmoid activation."""
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function for backpropagation
def sigmoid_derivative(x):
    """Compute derivative of sigmoid activation."""
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden1_size, hidden2_size, output_size):
        # - input_size (int): Number of neurons in the input layer.
        # - hidden1_size (int): Number of neurons in the first hidden layer.
        # - hidden2_size (int): Number of neurons in the second hidden layer.
        # - output_size (int): Number of neurons in the output layer.
        
        # Weights and biases for input to first hidden layer
        self.weights_input_hidden1 = np.random.uniform(-1, 1, (input_size, hidden1_size))
        self.bias_hidden1 = np.random.uniform(-1, 1, (hidden1_size,))
        
        # Weights and biases for first hidden layer to second hidden layer
        self.weights_hidden1_hidden2 = np.random.uniform(-1, 1, (hidden1_size, hidden2_size))
        self.bias_hidden2 = np.random.uniform(-1, 1, (hidden2_size,))
        
        # Weights and biases for second hidden layer to output
        self.weights_hidden2_output = np.random.uniform(-1, 1, (hidden2_size, output_size))
        self.bias_output = np.random.uniform(-1, 1, (output_size,))

    def forward(self, X):
        # - X (nparray): Input data.
        # Returns: nparray: Output after forward propagation.
        
        # Input to first hidden layer
        self.input = X
        self.hidden1_output = sigmoid(np.dot(self.input, self.weights_input_hidden1) + self.bias_hidden1)
        
        # First hidden layer to second hidden layer
        self.hidden2_output = sigmoid(np.dot(self.hidden1_output, self.weights_hidden1_hidden2) + self.bias_hidden2)
        
        # Second hidden layer to output
        self.output = sigmoid(np.dot(self.hidden2_output, self.weights_hidden2_output) + self.bias_output)
        
        return self.output

    def backward(self, X, y, learning_rate = 0.1):
        # - X (nparray): Input data.
        # - y (nparray): True labels.
        # - learning_rate (float): Learning rate for weight updates.
        
        # Compute the difference between predicted and true labels
        output_error = y - self.output
        # Derivative for the output layer
        d_output = output_error * sigmoid_derivative(self.output)
        
        # Backpropagate the error from output to second hidden layer
        hidden2_error = d_output.dot(self.weights_hidden2_output.T)
        d_hidden2 = hidden2_error * sigmoid_derivative(self.hidden2_output)
        
        # Backpropagate the error from second hidden layer to first hidden layer
        hidden1_error = d_hidden2.dot(self.weights_hidden1_hidden2.T)
        d_hidden1 = hidden1_error * sigmoid_derivative(self.hidden1_output)

        # Weight and bias updates for second hidden layer to output
        self.weights_hidden2_output += self.hidden2_output.T.dot(d_output) * learning_rate
        self.bias_output += np.sum(d_output, axis=0) * learning_rate
        
        # Weight and bias updates for first hidden layer to second hidden layer
        self.weights_hidden1_hidden2 += self.hidden1_output.T.dot(d_hidden2) * learning_rate
        self.bias_hidden2 += np.sum(d_hidden2, axis=0) * learning_rate
        
        # Weight and bias updates for input to first hidden layer
        self.weights_input_hidden1 += X.T.dot(d_hidden1) * learning_rate
        self.bias_hidden1 += np.sum(d_hidden1, axis=0) * learning_rate

    def train(self, X, y, epochs = 1000, learning_rate = 0.1):
        # - X (nparray): Input data.
        # - y (nparray): True labels.
        # - epochs (int): Number of training iterations.
        # - learning_rate (float): Learning rate for weight updates.
        for _ in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)


if __name__ == "__main__":
    # Generate all 32 possible inputs for a 5-input binary perceptron.
    training_inputs = np.array([list(map(int, format(i, '05b'))) for i in range(32)])
    
    # Generate desired outputs based on the specified input patterns.
    desired_patterns = [
        [0,1,1,1,1], [1,0,1,1,1], [1,1,0,1,1], [1,1,1,0,1], [1,1,1,1,0], [1,1,1,1,1],
        [0,0,0,0,0], [1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]
    ]
    desired_outputs = np.array([1 if inp.tolist() in desired_patterns else 0 for inp in training_inputs]).reshape(-1, 1)

    # Create and train the neural network
    nn = NeuralNetwork(input_size=5, hidden1_size=5, hidden2_size=3, output_size=1)
    nn.train(training_inputs, desired_outputs, epochs=10000)
    
    # Test and print the results
    print("Testing with trained weights...")
    for i in range(len(training_inputs)):
        predicted_output = nn.forward(training_inputs[i])
        print("Input:", training_inputs[i], "-> Predicted Output:", round(predicted_output[0]), ", Desired Output:", desired_outputs[i][0])

