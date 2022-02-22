#Fibonacci succession with recursive algorythms
def fibonacci(n):
    pos = 2
    lst = [0,1]
    while pos <= n:
        next = lst[pos-1]+lst[pos-2]
        lst.append(next)
        pos+=1
    
    return lst[n-1]

    #Determinación de n:    
    result = fibonacci(n-1) + fibonacci(n-2)

    return result

print(fibonacci(11))



