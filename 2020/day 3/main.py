def main():
	f = open("input.txt", "r")
	i = f.read()
	slopeMap = i.split("\n")

	trees = getTrees(slopeMap, 1, 1) * getTrees(slopeMap, 3, 1) * getTrees(slopeMap, 5, 1) * getTrees(slopeMap, 7, 1) * getTrees(slopeMap, 1, 2)

	print(trees)

def getTrees(slopeMap, right, down):
	index = 0
	trees = 0

	i = 0

	while i < len(slopeMap):
		path = slopeMap[i]
		symbol = path[index]

		if symbol == "#":
			trees += 1

		index += right

		if index >= len(path):
			index = index - len(path)	

		i += down

	return trees


if __name__ == "__main__":
    main()