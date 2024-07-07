input("what's the weather looks outside?")
weather1 = ""
while weather1 !="rainy":
    print ("Are you sure?")
    weather1 = input()
print("that's terrible.")

while True:
    print("Do you have an umbrella?")
    answer1 = input()
    if  answer1 =="yes":
        print("Let's grab a drink")
    else:
        print("it seems we have to wait till the sum comes out.")    
        break
input("how about now?(still rain/others)")
weather2 = input()
if weather2 == "finally stops":
    print("ok, let's go") 