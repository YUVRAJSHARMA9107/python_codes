n=int(input("enter the number of terms of fibbonacci series"))
fib[n]=[0]*n

fib[0]=0
fib[1]=1
for i in range(2,n+1):
  fib[i-1]=fib[i-1]+fib[i-2]
print (fib[n])

