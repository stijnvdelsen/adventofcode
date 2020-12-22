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
			"iyr": "20[1|2][0-9]",
			"eyr": "20[2|3][0-9]",
			"hgt": "1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]",
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
					#print(field + ":" + value)

					del reqFields[field]
				# else:
				# 	print("MISMATCH: " + field + ":" + value)

		if len(reqFields) <= 0:
			valid += 1

	print(valid)

if __name__ == "__main__":
    main()	