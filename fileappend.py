f = open("myfile.txt", "r+")

lines = list(f)

lines[0] = "This is a new line\n"

#f.write("This is a new line")

#lines = list(f)

for l in lines:
 print(l)

f.close()