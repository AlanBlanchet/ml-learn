import os

from .io import Dataset

os.chdir("custom")

dataset = Dataset()

dataset.load("assets")

# print(np.random.randn(3 + 1) / np.sqrt(3))

# # construct the OR dataset
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [0], [0], [1]])
# # define our perceptron and train it
# print("[INFO] training perceptron...")
# p = Perceptron(X.shape[1], alpha=0.1)
# p.fit(X, y, epochs=20)

# # now that our perceptron is trained we can evaluate it
# print("[INFO] testing perceptron...")
# # now that our network is trained, loop over the data points
# for (x, target) in zip(X, y):
#     # make a prediction on the data point and display the result
#     # to our console
#     pred = p.predict(x)
#     print(f"[INFO] data={x}, ground-truth={target[0]}, pred={pred}")
