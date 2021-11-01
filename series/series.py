""" Calculates and returns the nth number fo the fibonacci series"""
def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
""" Calculates and returns the nth number fo the lucas series"""
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


""" Calculates and returns the nth number of various summation series series"""        
def sum_series(n, f=0, s=1):
    if n == 0:
        return f
    elif n == 1:
        return s
    else:
        return sum_series(n-2, f, s)+sum_series(n-1, f, s)
