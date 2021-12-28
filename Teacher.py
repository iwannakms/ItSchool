class Teacher:

    def __init__(self, first_name, last_name, user_name, password, subject):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.subject = subject

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

    def getSubject(self):
        return self.subject

    def setSubject(self, newSubject):
        self.subject = newSubject
