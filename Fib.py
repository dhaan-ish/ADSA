def printFibo(n):
    if n < 1:
        print("Number of terms should be positive.")
        return
    
    Fibo = [0]

    if n > 1:
        Fibo.append(1)

    for i in range(2, n):
        t = Fibo[i-1] + Fibo[i-2]
        Fibo.append(t)

    print("The Fibonacci Series by Dynamic Programming Approach:")
    for val in Fibo:
        print(val, end=' ')

printFibo(7)
print()