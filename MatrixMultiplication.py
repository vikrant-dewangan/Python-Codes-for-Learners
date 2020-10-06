A = [[1,0],
    [0 ,1]]

B = [[1,0,1],
    [1,1,1]]

## We want to multiply A(2*2) and B(2*3), we get sol(2*3) 
sol = [[0,0,0],
         [0,0,0]]

for i in range(len(A)):
   for j in range(len(B[0])):
       for k in range(len(B)):
           sol[i][j] += A[i][k] * B[k][j]

for x in sol:
   print(x)
