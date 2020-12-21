def main():
	f = open("input.txt", "r")
	i = f.read()
	passports = i.split("\n\n")

	valid = 0

	for passport in passports:
		reqFields = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "hcl"]

		passport = passport.replace("\n", " ")
		fields = passport.split(" ")

		for field in fields:
			field = field.split(":")[0]
			if field in reqFields:
				reqFields.remove(field)

		if len(reqFields) <= 0:
			valid += 1

	print(valid)

if __name__ == "__main__":
    main()	