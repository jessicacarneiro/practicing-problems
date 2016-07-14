class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        sum = 0
        for grade in self.scores:
            sum += grade
        final_grade = sum/len(self.scores)
        
        if final_grade >= 90:
            return 'O'
        elif final_grade >= 80:
            return 'E'
        elif final_grade >= 70:
            return 'A'
        elif final_grade >= 55:
            return 'P'
        elif final_grade >= 40:
            return 'D'
        else:
            return 'T'

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()