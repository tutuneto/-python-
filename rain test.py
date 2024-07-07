print("what's the weather looks outside?")
weather1 = ""
weather1= input ()
while weather1 !="rainy":
    print ("Are you sure?")
    weather1 = input()
print("that's terrible.")

while True:
    print("Do you have an umbrella?")
    answer1 = input()
    if  answer1 =="yes":
        print("let's go grab a drink.")
        break
    else:
        print("it seems we have to wait till the sum comes out.") 
        print("how about now?(still rains/finally stops)")
        weather2 = input()
        if weather2 == "finally stops":
            print("ok, let's go") 
            break
        else:
            print("i'm straving.")
            break
