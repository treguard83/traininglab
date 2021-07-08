import student

john = student.Student("John","21","dolphin") 

johnage = john.age

print("John\'s age is " + johnage)

print("Here are some avg scores: " + "{:.2f}".format(student.Student.avgscores(23,45,90)))