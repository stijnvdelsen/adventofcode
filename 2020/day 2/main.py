import re

def main():
	f = open("input.txt", "r")
	i = f.read()
	iParsed = i.split("\n")

	regexSplit = r"([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)"

	validCntr = 0

	for passPolicy in iParsed:
		matchSplit = re.findall(regexSplit, passPolicy)[0]

		minPolicy = int(matchSplit[0]) - 1
		maxPolicy = int(matchSplit[1]) - 1
		letterPolicy = matchSplit[2]

		password = matchSplit[3]

		letterCntr = 0

		if password[minPolicy] == letterPolicy:
			letterCntr += 1

		if password[maxPolicy] == letterPolicy:
			letterCntr += 1

		if letterCntr == 1:
			validCntr += 1

	print(validCntr)


if __name__ == "__main__":
    main()