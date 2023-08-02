print("Test your skills here! ")

Will=input("Do you want to play ")

if Will.lower() != "yes":
    quit()

print("Okay lets begin! ")
score=0

Ques=input("What is RAM? ")
if Ques.lower() =="random access memory":
    print("Correct :)")
    score +=1
else:
    print("incorrect :( ")

Ques=input("What is CPU? ")
if Ques.lower() =="central processing unit":
    print("Correct :)")
    score +=1
else:
    print("incorrect :( ")

Ques=input("What is ROM? ")
if Ques.lower() =="read only memory":
    print("Correct :)")
    score +=1
else:
    print("incorrect :( ")

Ques=input("What is PSU? ")
if Ques.lower() =="power supply unit":
    print("Correct :)")
    score +=1
else:
    print("incorrect :( ")

Ques=input("What is ALU? ")
if Ques.lower() =="arithmetic logic unit":
    print("Correct :)")
    score +=1
else:
    print("incorrect :( ")


print("your final score is ", score)