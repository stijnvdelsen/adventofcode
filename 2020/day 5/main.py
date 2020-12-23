def explenation():
	f = open("input.txt", "r")
	i = f.read()
	boardingPasses = i.split("\n")

	highestRow = 127
	highestColumn = 7

	# This is for visualizing the problem to solver it faster
	matrix = []

	for y in range(0,highestRow+1):
		matrix.append([])

		for x in range(0,highestColumn+1):
			matrix[y].append(bin(y*8+x))
			
	# This will print a map of the seats in the airplane
	for m in matrix:
		print(m)

	newBoardingpasses = []

	for boardingPass in boardingPasses:

		newBoardingPass = ""

		for letter in boardingPass:
			if letter == "F" or letter == "L":
				newBoardingPass += "0"
			else:
				newBoardingPass += "1"


		newBoardingPass = "0b" + newBoardingPass.lstrip("0")
		newBoardingpasses.append(newBoardingPass)

	print(newBoardingpasses)

	for newPass in newBoardingpasses:
		test = [(index, row.index(newPass)) for index, row in enumerate(matrix) if newPass in row]
		print(newPass)
		print(matrix[test[0][0]][test[0][1]])
		print("\n\n")

def main():
	f = open("input.txt", "r")
	i = f.read()
	boardingPasses = i.split("\n")

	highestValue = 0

	for boardingPass in boardingPasses:
		newBoardingPass = ""

		for letter in boardingPass:
			if letter == "F" or letter == "L":
				newBoardingPass += "0"
			else:
				newBoardingPass += "1"

		value = int("0b" + newBoardingPass.lstrip("0"), 2)

		if value > highestValue:
			highestValue = value

	print(highestValue)

if __name__ == "__main__":	
    main()