def main():
	f = open("input.txt", "r")
	i = f.read()
	questions = i.split("\n\n")

	cntr = 0

	for group in questions:
		persons = group.split('\n')
		answers = []

		for person in persons:
			for answer in person:
				if answer not in answers:
					answers.append(answer)

		cntr += len(answers)

	print(cntr)

if __name__ == "__main__":	
    main()