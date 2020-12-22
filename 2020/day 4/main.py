import re

def main():
	f = open("input.txt", "r")
	i = f.read()
	passports = i.split("\n\n")

	valid = 0

	for passport in passports:
		reqFields = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "hcl"]

		reqFields = {
			"byr": "19[2-9][0-9]|200[0-2]",
			"iyr": "201[0-9]|2020",
			"eyr": "202[0-9]|2030",
			"hgt": "1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in",
			"ecl": "amb|blu|brn|gry|grn|hzl|oth",
			"pid": "[0-9]{9}",
			"hcl": "#[a-zA-Z0-9]{6}"
		}

		passport = passport.replace("\n", " ")
		fields = passport.split(" ")

		for field in fields:
			value = field.split(":")[1]
			field = field.split(":")[0]

			if field in reqFields:
				regex = "^" + reqFields[field] + "$"

				if re.match(regex, value):
					del reqFields[field]

		if len(reqFields) <= 0:
			valid += 1

	print(valid)

if __name__ == "__main__":
    main()	