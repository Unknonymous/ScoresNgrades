from random import *
def grade():
    for i in range (0, 12):
        result = []
        score = 100
        if i == 0:
            print "Scores and Grades"
        elif i > 0 and i < 11 :
            score = randint(60, 100)
            if score >= 60 and score <= 69:
                grade = "D"
            elif score >= 70 and score <= 79:
                grade = "C"
            elif score >= 80 and score <= 89:
                grade = "B"
            elif score >= 90 and score <= 100:
                grade = "A"
            print "Score:", score, "; Your grade is", grade
        else:
            print "End of the program. Bye!"

grade()