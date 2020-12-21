def main():
	f = open("text.txt", "r")
	i = f.read()
	iParsed = i.split("\n")

	outcome = 0

	for n in iParsed:
		for n2 in iParsed:

			sumi = int(n) + int(n2)

			if (sumi == 2020):
				outcome = int(n) * int(n2)

	print(outcome)

if __name__ == "__main__":
    # execute only if run as a script
    main()