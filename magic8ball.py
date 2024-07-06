import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is decidedly so"
    elif answerNumber == 2:
        return "It is certain"
    elif answerNumber == 3:
        return "yes"
    elif answerNumber == 4:
        return "reply hazy try again"
    elif answerNumber == 5:
        return "concentrate and try it again"
    elif answerNumber == 6:
        return "ask again later"
    elif answerNumber == 7:
        return "my reply is no"
    elif answerNumber == 8:
        return "outlook not so good"
    elif answerNumber == 9:
        return "very doubtful"
    
r == random.randint(1,9)
forfune = getAnswer(r)
print(forfune)

print(getAnswer(random.randint(1,9)))