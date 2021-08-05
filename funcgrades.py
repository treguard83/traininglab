def addgrades(hworkscore, assessscore, examscore):
    answer = hworkscore + assessscore + examscore
    return answer

name = str(input("What is your name? "))

isValidHWorkScore = False
isValidAssessScore = False
isValidExamScore = False

while not isValidHWorkScore:
    try:
        hworkscore = int(input("What is your homework score? "))
        if hworkscore >= 0 and hworkscore <= 25:
            isValidHWorkScore = True
    except:
        print('You must enter a valid homework score between 0 and 25')

while not isValidAssessScore:
    try:
        assessscore = int(input("What is your assessment score? "))
        if assessscore >= 0 and assessscore <= 50:
            isValidAssessScore = True
    except:
        print('You must enter a valid assessment score between 0 and 50')

while not isValidExamScore:
    try:
        examscore = int(input("What is your exam score? "))
        if examscore >= 0 and examscore <= 100:
            isValidExamScore = True
    except:
        print('You must enter a valid exam score between 0 and 100')

if isValidHWorkScore == True and isValidAssessScore == True and isValidExamScore == True:
   totalpoints = addgrades(hworkscore, assessscore, examscore)
   finalpcent = "{:.2f}".format((totalpoints/175)*100)
   print(name + " your final ICT grade as a percentage is: " + finalpcent +"%")
   finalpcent = float(finalpcent)
   if finalpcent >=90 and finalpcent <= 100:
      gradeStr = "A*"
   elif finalpcent >= 80 and finalpcent <= 89:
      gradeStr = "A"
   elif finalpcent >= 70 and finalpcent <= 79:
      gradeStr = "B"
   elif finalpcent >= 60 and finalpcent <= 69:
      gradeStr = "C"
   elif finalpcent >= 50 and finalpcent <= 59:
      gradeStr = "D"
   elif finalpcent >= 40 and finalpcent <= 49:
      gradeStr = "E"
   elif finalpcent >= 30 and finalpcent <= 39:
      gradeStr = "F"
   elif finalpcent >= 20 and finalpcent <= 29:
      gradeStr = "G"
   else:
      gradeStr = "U"
   print(name + " this means your final grade is: " + gradeStr)

