f = open("teams.txt", "r")

lines = list(f)

f.close()

f = open("teams.txt", "w")

lines.insert(0,"This is a new line\n")

liststr = "".join(lines)

f.write(liststr)

for l in lines:
 print(l)

f.close()