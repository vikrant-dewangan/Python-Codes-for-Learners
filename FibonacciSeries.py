def fibonacciSeries(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input n should be positive") 
    elif n == 0: 
        print(0) 
    elif n == 1: 
        print(1)
    else:
        print(a)
        for i in range(2,n+1): 
            print(b)
            c = a + b 
            a = b 
            b = c  

n = int(input("Enter a number to find fibonacci series : "))
fibonacciSeries(n)
