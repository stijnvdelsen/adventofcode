import math

def test():
	f = open("input.txt", "r")
	i = f.read()
	paths = i.split("\n")

	e = [0, -2]
	se = [-1, -1]
	sw = [-1, 1]
	w = [1, 1]
	nw = [1, -1]

	newPaths = []

	for path in paths:
		pass

def main():
	f = open("input.txt", "r")
	i = f.read()
	paths = i.split("\n")

	# white is bit(0)
	# black is bit(1)
	# all bits are starting with 0
	# 
	# 				 0 0
	# 				0 0 0
	#				 0 0
	# 
	
	grid = []

	# First we want to create this grid like previous times for viualizing the problem
	# for y in range(0, 100):
	# 	row = []

	# 	for x in range(0, 100):
	# 		if x == 0 or x % 2 == 0:
	# 			if y % 2 == 0:
	# 				row.append("0")
	# 			else:
	# 				row.append(" ")
	# 		else:
	# 			if y % 2 == 0:
	# 				row.append(" ")
	# 			else:
	# 				row.append("0")

	# 	grid.append(row)

	# for row in grid:
	# 	print(''.join(row))
	
	# grid = []

	# I want to give every bit an address from the center of the grid
	# Like e: -1, se: 2, sw: 3, w: 1, nw: 5: ne: 6
	# That converts wwswwwswwnwwe to 4434434541

	# First we want to create this grid like previous times for viualizing the problem
	
	# x x x x x x x x x x x

	maxrow = 101
	maxcol = 101

	centerY = math.ceil(maxrow / 2)
	centerX = math.ceil(maxcol / 2)

	for y in range(0, maxrow):
		row = []

		for x in range(0, maxcol):

			el = []
			el.append(y*maxcol+x)

			if x == 0 or x % 2 == 0:
				if y % 2 == 0:
					el.append("0")
				else:
					el.append(None)
			else:
				if y % 2 == 0:
					el.append(None)
				else:
					el.append("0")

			row.append(el)

		grid.append(row)

	# Print grid, display None as space
	# for row in grid:
	# 	print(''.join(map(lambda col: col[1] if col[1] != None else " ", row)))

	# We want to give all coords a y and x
	coE = [0, -2]
	coSE = [-1, -1]
	coSW = [-1, 1]
	coW = [0, 1]
	coNW = [1, 1]
	coNE = [1, -1]

	def mapPath(path):
		nPath = []
		i = 0

		while i < len(path):
			if path[i] == "e":
				nPath.append(coE)
				i += 1
			elif path[i] == "s":
				if path[i+1] == "e":
					nPath.append(coSE)
				else:
					nPath.append(coSW)

				i += 2
			elif path[i] == "w":
				nPath.append(coW)
				i += 1
			elif path[i] == "n":
				if path[i+1] == "w":
					nPath.append(coNW)
				else:
					nPath.append(coNE)

				i += 2
			else:
				i += 1

		return nPath

	# print(paths)

	newPath = list(map(mapPath, paths))

	# print(newPath)

	for path in newPath:

		curPos = [centerY, centerX]

		for instructions in path:
			curPos[0] = curPos[0] + instructions[0]
			curPos[1] = curPos[1] + instructions[1]

		# print(len(newPath))
		# print(path)
		# print(curPos)

		print(grid[curPos[0]][curPos[1]])

		# print(grid[curPos[0]][curPos[1]])

		grid[curPos[0]][curPos[1]] = "1" if grid[curPos[0]][curPos[1]] else "0"

	# for row in grid:
	# 	print(''.join(map(lambda col: col[1] if col[1] != None else " ", row)))

	# print(grid)

	cnt = 0

	# for row in grid:
	# 	cnt += len(map(lambda col: col[1] if col[1] == "1" e))

	# print(str(cnt))

if __name__ == "__main__":	
    main()