import re

xVariable = ""
secondNum = 0
answer = 0

def Askquestion():
    expression = input("What is the equation you want me to solve?")
def FindInt():
    while True:
        i = 0
        try:
            exInt = int(expression[i])
        except:
            exInt = expression[i]
            break
        i = i + 1
Askquestion()
