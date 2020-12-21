def main():
	f = open("input.txt", "r")
	i = f.read()
	iParsed = i.split("\n")

	outcome = 0

	for n in iParsed:
		for n2 in iParsed:
			for n3 in iParsed:
				sumi = int(n) + int(n2) + int(n3)

				if (sumi == 2020):
					outcome = int(n) * int(n2) * int(n3)

	print(outcome)

if __name__ == "__main__":
    # execute only if run as a script
    main()