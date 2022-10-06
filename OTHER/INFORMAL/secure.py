import sys as sus
import os

skip = False

#skip = True # Add a "#" to the beginning of this line to not skip the following code

a1 = "NRVQ31ERBhXTEF0ZNRVR31EVBhXTUF0ZNRVQ31ERBhXTUF0ZNRVR31ERFhXTUF0ZNRVQ31EVBdXTUFUP"
a2 = "Test Testerson"
a3 = "Kane Tanaka"
a4 = "PUFWVkdWRlZZUm1RV1ZVTXpFbFZTNWtXd1lVVlVoRmFHSlZSeE1qVVdKbFRhQmpSVlJGV29Ka1VGRnpNUlpsVU9wRk1HVkZWWWhtUVdWVU16SWxWUzVrV3dZVVJVaEZhQ0pWUnhNVFVXSmxU"

if not skip:
    p1 = input("Input the correct password:\n")
    if p1 != a1:
        sus.exit(0)

    p2 = input("What is your name?\n")
    if p2 != a2:
        sus.exit(0)

    p3 = input("Who is the boomerest of them all?\n")
    if p3 != a3:
        sus.exit(0)

path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\d0-17.txt"

with open(path, "a+") as f:
    input("f1l3-pu7-f1r57-p37!!!\n")
    test = f.readline()
    f.close()
    os.remove(path)
    if test != a4:
        sus.exit(0)
        

print("The password is: !__P455W0RD__!")