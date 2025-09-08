
class Student:

    def __init__ (self, firstName, lastName, __nationalId, regStatus):
        self.firstName = firstName
        self.lastName = lastName
        self.__nationalId = __nationalId # private attribute
        self.regStatus = regStatus

    def doesStudentHaveId(self):
        if self.__nationalId:
            return True
        else:
            return False

newStudent = Student("John", "Doe", "123456789", True)

print(f"This is regStatus: {newStudent.regStatus}")
print(f"Does student have ID? {newStudent.doesStudentHaveId()}")


