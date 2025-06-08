# def fact(n):                                        
    
#     return 1 if (n==1 or n==0) else n * fact(n - 1) 



# num = 5    
# print(fact(num))


def fibonacci_of(n):
    if n in {0, 1}:                
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2) 

print([fibonacci_of(n) for n in range(15)])
