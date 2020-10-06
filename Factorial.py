n = int(input("Enter a number: "))

f = 1
if n < 0:
   print("Invalid number ")
elif n == 0:
   print("The factorial of 0 is 1")
else:
    for i in range(1,n + 1):
        f = f*i
    print("The factorial of " + str(n) + " is " + str(f))
