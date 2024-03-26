num1=int(input("enter the 1st no:"))
num2=int(input("enter the 2nd no:"))
while(num2!=0):
    num1,num2=num2,num1%num2

print("gcd is",num1)
