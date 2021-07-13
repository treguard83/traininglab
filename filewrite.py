f = open("teams.txt", "x")

teams = ["Man U","Celtic","Liverpool","Cardiff City","Dundalk"]

for n in range(1,6):
    newline = "This is line " + str(n) + " for the team of " + teams[n-1] + "\n"
    f.write(newline)

f.close()

f = open("teams.txt", "r")
lines = list(f)

print("Line 1 contents: " + lines[0])
print("Line 4 contents: " + lines[3])

f.close()