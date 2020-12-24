def part_1():
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

def main():
	f = open("input.txt", "r")
	i = f.read()
	questions = i.split("\n\n")

	cntr = 0

	for group in questions:
		persons = group.split('\n')
		answers = list(set(group.replace('\n', '')))

		# print(answers)
		# print(group)

		for person in persons:
			for letter in group.replace('\n', ''):
				if letter not in person and letter in answers:
					answers.remove(letter)

		# for letter in group.replace('\n', ''):
		# 	for person in persons:
		# 		if letter not in person:
		# 			print(letter)
		# 			answers.remove(letter)

		cntr += len(answers)

	print(cntr)

if __name__ == "__main__":	
    main()


 # Alle letters die persoon bevat