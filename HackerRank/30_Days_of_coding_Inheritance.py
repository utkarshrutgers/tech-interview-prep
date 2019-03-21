class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,f,l,idn,scores):
        super().__init__(f,l,idn)
        self.scores = scores

    #   Function Name: calculate
    def calculate(self):
        sumn = 0
        for i in range(len(self.scores)):
            sumn = sumn + self.scores[i]
            #print(self.scores[i])
        sumn = sumn/len(self.scores)
        if(90<=sumn<=100):
            return 'O'
        elif(80<=sumn<=90):
            return 'E'
        elif(70<=sumn<=80):
            return 'A'
        elif(55<=sumn<=70):
            return 'P'
        elif(40<=sumn<=55):
            return 'D'
        elif(sumn<40):
            return 'T'
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
