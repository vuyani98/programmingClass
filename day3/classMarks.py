student1 = {
    "name" : "Matthew",
    "percentage" : 50,
    "grade" : ""
}

student2 = {
    "name" : "Mark",
    "percentage" : 30,
    "grade" : ""
}

student3 = {
    "name" : "Luke",
    "percentage" : 75,
    "grade" : ""
}

student4 = {
    "name" : "John",
    "percentage" : 43,
    "grade" : ""
}

students = [student1, student2, student3, student4]

numOfPasses = 0
numOfDistinctions = 0
numOfFails = 0

for student in students:

    if (student["percentage"] >= 75):
        student["grade"] = "Passed with Distinction"
        numOfDistinctions += 1

    elif (student["percentage"] >= 50): 
        student["grade"] = "Pass"
        numOfPasses += 1
        
    else:
        student["grade"] = "Fail"
        numOfFails += 1


print("Number of distinctions: ", numOfDistinctions)
print("Number of passes: ", numOfPasses)
print("Number of fails: ", numOfFails)