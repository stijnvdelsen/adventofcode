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

def part_1():
	f = open("input.txt", "r")
	i = f.read()
	b = i.split("\n")

	print(max(list(map(lambda p: int("0b" + ''.join(list(map(lambda l: "0" if l == "F" or l == "L" else "1", p))).lstrip("0"), 2), b))))

def main():
	f = open("input.txt", "r")
	i = f.read()
	b = i.split("\n")

	passes = list(map(lambda p: int("0b" + ''.join(list(map(lambda l: "0" if l == "F" or l == "L" else "1", p))).lstrip("0"), 2), b))

	highestRow = 127
	highestColumn = 7

	# This is for visualizing the problem to solver it faster
	matrix = []

	for y in range(0,highestRow+1):
		matrix.append([])

		for x in range(0,highestColumn+1):
			matrix[y].append(y*8+x)

	for bPass in passes:
		passCoord = [(index, row.index(bPass)) for index, row in enumerate(matrix) if bPass in row]
		del matrix[passCoord[0][0]][passCoord[0][1]]

	# This will print a map of the seats in the airplane
	for m in matrix:
		print(m)

if __name__ == "__main__":	
    main()