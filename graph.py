import matplotlib.pyplot as plt

X = [10, 20, 30, 40, 50]
Y = [30, 30, 30, 30, 30]

plt.plot(X,Y, label="LINE 1", linestyle="dotted")
plt.plot(Y,X, label="LINE 2", linestyle="dashed")
plt.LEGEND()
plt.show()