# import the necessary packages
import numpy as np

from nn.neuralnetwork import NeuralNetwork

# construct the XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# define our 2-2-1 neural network and train it
nn = NeuralNetwork([2, 1], alpha=0.5)
nn.fit(X, y, epochs=20000)

# now that our network is trained, loop over the XOR data points
for (x, target) in zip(X, y):
    # make a prediction on the data point and display the result
    # to our console
    pred = nn.predict(x)[0][0]
    step = 1 if pred > 0.5 else 0
    print(f"[INFO] data={x}, ground-truth={target[0]}, pred={pred:.4f}, step={step}")
