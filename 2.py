#while 循环 和 break 

while True:
    print ("Please type your name.")
    name = input()
    if name == "amy":
       break
print ("Have a good day!")


name = ""
while name != 'amy':
    print ("type your name in a right way.")
    name = input()
print ("Thank you.")

while True:
    print("who are you")
    name = input()
    if name == "Gua":
        continue
    print("hello, Gua. what is the key word?")
    password = input()
    if password == "love cc":
        break
print("congratulations!")


