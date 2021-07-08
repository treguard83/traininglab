class Student:

   def __init__(self, name, age, classname):
     self.name = name
     self.age = age
     self.classname = classname

   def avgscores(hworkscore, assessscore, examscore):
    answer = (hworkscore + assessscore + examscore) / 3
    return answer

   #John = Student("John", "21","dolphin")
   #Jane = Student("Jane", "22","tiger")