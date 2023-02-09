import numpy as np
import sys

def get_thetas():
	theta0 = 0
	theta1 = 0
	try:
		with open("./theta.txt", "r") as file:
			buf = file.read()
			thetas = list(map(float, buf.split(',')))
			theta0 = thetas[0]
			theta1 = thetas[1]
	except:
		print("You should train first...")
	return theta0, theta1

def get_data(argv):
	try:
		data = np.genfromtxt(argv, delimiter=',')[1:]
	except:
		print("Impossible to read data.csv")
		exit(1)
	x = data[:, 0]
	y = data[:, 1]

	return x, y

def main():
	if len(sys.argv) != 2:
		print("Error, do: python3 precision.py [your dataset]")
		exit(1)
	theta0, theta1 = get_thetas()
	x, y = get_data(sys.argv[1])
	diff_sum = 0
	for i in range(0, x.shape[0]):
		diff_sum += abs(theta0 + (theta1 * x[i]) - y[i]) / y[i]
	m = (1 - diff_sum / x.shape[0]) * 100
	print("Algorithm precision : {0:.2f}%".format(m))

if __name__ == "__main__":
	main()
