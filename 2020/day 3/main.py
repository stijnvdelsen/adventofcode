def main():
	f = open("input.txt", "r")
	i = f.read()
	iParsed = i.split("\n")

	index = 0
	trees = 0

	for path in iParsed:
		symbol = path[index]

		if symbol == "#":
			trees += 1

		index += 3

		if index >= len(path):
			index = index - len(path)		


	print(trees)

if __name__ == "__main__":
    # execute only if run as a script
    main()