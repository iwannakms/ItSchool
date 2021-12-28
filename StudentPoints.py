class StudentPoints:


    def __init__(self, user_name, math_points=None, programming_langueges_points=None,
                 human_computer_interaction_points=None, german_points=None,
                 english_points=None, algorithms_and_data_structure_epoints=None):
        self.user_name = user_name
        self.math_points = math_points
        self.programming_langueges_points = programming_langueges_points
        self.human_computer_interaction_points = human_computer_interaction_points
        self.german_points = german_points
        self.english_points = english_points
        self.algorithms_and_data_structure_epoints = algorithms_and_data_structure_epoints

    def getPointsUserName(self):
        return self.user_name

    def setPointsUserName(self, newUserName):
        self.user_name = newUserName

    def getMathPoints(self):
        return self.math_points

    def setMathPoints(self, newGrade):
        self.math_points = newGrade

    def getProgrammingLanguegesPoints(self):
        return self.programming_langueges_points

    def setProgrammingLanguegesPoints(self, newGrade):
        self.programming_langueges_points = newGrade

    def getHumanComputerInteractionPoints(self):
        return self.human_computer_interaction_points

    def setHumanComputerInteractionPoints(self, newGrade):
        self.human_computer_interaction_points = newGrade

    def getGermanPoints(self):
        return self.german_points

    def setGermanGradePoints(self, newGrade):
        self.german_points = newGrade

    def getEnglishPoints(self):
        return self.english_points

    def setEnglishPoints(self, newGrade):
        self.english_points = newGrade

    def getAlgorithmsAndDataStructurePoints(self):
        return self.algorithms_and_data_structure_epoints

    def setAlgorithmsAndDataStructurePoints(self, newGrade):
        self.algorithms_and_data_structure_epoints = newGrade
