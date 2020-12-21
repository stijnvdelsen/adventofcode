import re

def main():
	f = open("input.txt", "r")
	i = f.read()
	iParsed = i.split("\n")

	regexSplit = r"([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)"

	validCntr = 0

	for passPolicy in iParsed:
		matchSplit = re.findall(regexSplit, passPolicy)[0]

		minPolicy = matchSplit[0]
		maxPolicy = matchSplit[1]
		letterPolicy = matchSplit[2]

		password = matchSplit[3]

		letterCntr = 0

		for letter in password:
			if letter == letterPolicy:
				letterCntr += 1

		if int(minPolicy) <= letterCntr <= int(maxPolicy):
			validCntr += 1

	print(validCntr)


if __name__ == "__main__":
    # execute only if run as a script
    main()