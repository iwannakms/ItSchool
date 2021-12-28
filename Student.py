class Student:

    def __init__(self, first_name, last_name, user_name,
                 password, math_grade=None, programming_langueges_grade=None,
                 human_computer_interaction_grade=None, german_grade=None,
                 english_grade=None, algorithms_and_data_structure_grade=None):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.math_grade = math_grade
        self.programming_langueges_grade = programming_langueges_grade
        self.human_computer_interaction_grade = human_computer_interaction_grade
        self.german_grade = german_grade
        self.english_grade = english_grade
        self.algorithms_and_data_structure_grade = algorithms_and_data_structure_grade

    def getFirstName(self):
        return self.first_name

    def setFirstName(self, newFirstName):
        self.first_name = newFirstName

    def getLastName(self):
        return self.last_name

    def setLastName(self, newLastName):
        self.last_name = newLastName

    def getUserName(self):
        return self.user_name

    def setUserName(self, newUserName):
        self.user_name = newUserName

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getMathGrade(self):
        return self.math_grade

    def setMathGrade(self, newGrade):
        self.password = newGrade

    def getProgrammingLanguegesGrade(self):
        return self.programming_langueges_grade

    def setProgrammingLanguegesGrade(self, newGrade):
        self.programming_langueges_grade = newGrade

    def getHumanComputerInteractionGrade(self):
        return self.human_computer_interaction_grade

    def setHumanComputerInteractionGrade(self, newGrade):
        self.human_computer_interaction_grade = newGrade

    def getGermanGrade(self):
        return self.german_grade

    def setGermanGrade(self, newGrade):
        self.german_grade = newGrade

    def getEnglishGrade(self):
        return self.english_grade

    def setEnglishGrade(self, newGrade):
        self.english_grade = newGrade

    def getAlgorithmsAndDataStructureGrade(self):
        return self.algorithms_and_data_structure_grade

    def setAlgorithmsAndDataStructureGrade(self, newGrade):
        self.algorithms_and_data_structure_grade = newGrade
