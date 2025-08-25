#Conditional Statement
#1
a = int(input("enter your age :"))
if a > 18 :
    print("eligible to vote")
elif(a == 18):
    print("wait for some time")
else:
    print("not eligible to vote")

#2
A = int(input("Enter your marks: "))

if A > 100 or A < 0:
    print("Your marks are invalid")
elif A >= 90:
    print("You scored A+ grade")
elif A >= 75:
    print("You scored A grade")
elif A >= 60:
    print("You scored B grade")
elif A >= 40:
    print("You scored C grade")
else:
    print("You failed your exam") 

#3 Even or Odd
num = int(input("enter your number :"))
if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")
    