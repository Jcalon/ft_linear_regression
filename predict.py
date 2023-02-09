# Get theta0 & thata1 from training return file
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

def main():
	km = input("Km: ")
	try:
		km = int(km)
	except:
		print("Cannot cast '{}' to float.".format(km))
		exit(1)
	theta0, theta1 = get_thetas()
	# Linear function
	price = int(theta0 + (theta1 * km))
	if (price < 0):
		price = 0
	print("Estimated price :", price)

if __name__ == "__main__":
	main()
