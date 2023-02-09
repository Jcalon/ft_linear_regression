import numpy as np
from matplotlib import pyplot as plt
import sys

# Print datas
def print_plots(theta0, theta1, x, y):
	# Create window
	plt.figure(figsize=(10, 10), dpi=80)

	# Create raw data plot
	plt.subplot(2, 2, 1)
	plt.title("Raw data")
	plt.scatter(x, y)
	plt.xlabel('Km')
	plt.ylabel('Price')

	# Create linear regression plot
	plt.subplot(2, 2, 2)
	plt.title("After Machine Learning")
	plt.scatter(x, y)
	plt.xlabel('Km')
	plt.ylabel('Price')
	plt.plot(x, theta0 + (theta1 * x), c='r')

	plt.tight_layout()
	plt.show()


# Gradient Descent Algorithm
def gradient_descent(x, y, learning_rate, n):
	theta0, theta1 = float(0.0), float(0.0)
	for i in range(0, n):
		for size in range(0, x.shape[0]):
			estimate_price = (theta0 + (theta1 * x[size])) - y[size]
			theta0 -= learning_rate * (1 / x.shape[0]) * estimate_price
			theta1 -= learning_rate * (1 / x.shape[0]) * estimate_price * x[size]
	return theta0, theta1

# Parse .csv
def parsing(argv):
	try:
		data = np.genfromtxt(argv, delimiter=',')[1:]
	except:
		print("Impossible to read data.csv")
		exit(1)
	x = data[:, 0]
	y = data[:, 1]
	max_km = x.max()
	x_base = x
	x = x / max_km

	return x, y, x_base, max_km


def main():
	if len(sys.argv) != 2:
		print("Error, do: python3 train.py [your dataset]")
		exit(1)
	x, y, x_base, max_km = parsing(sys.argv[1])
	theta0, theta1 = gradient_descent(x, y, 0.1, 1000)
	theta1 /= max_km
	print("Theta0 = {0:.2f}".format(theta0), "\nTheta1 = {0:.2f}".format(theta1))
	try:
		file = open("theta.txt", "w")
		file.write(str(float(theta0)) + "," + str(float(theta1)))
		file.close()
	except:
		print("Error during writing theta value.")
		exit(1)
	# Display linear regression result
	print_plots(theta0, theta1, x_base, y)

if __name__ == "__main__":
	main() 
