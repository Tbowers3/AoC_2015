import pathlib
file = r"C:\Users\tobias.bowers\Desktop\2015_aoc1.txt"
data = pathlib.Path(file).read_text()
floor = 0
for d in data:
	if d == "(":
		floor += 1
	elif d == ")":
		floor -= 1

print(floor) 

