# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """

    if( n < 0 ):
        raise ValueError

    result = 1

    if(n == 0 or n == 1):
        return result

    for i in range(1,n+1):
        result*=i

    return result

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + c = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta = b**2 - 4*a*c

    if(delta < 0 ):
        return ()

    if(delta == 0):
        if( a == 0 and b == 0):
            return ()
        try:
            return (-b/2*a)
        except ZeroDivisionError:
            return (0)
        
    if(a == 0 and b != 0):
        return (-c/b)

    return ((-b + delta**(1/2)) / (2*a), (-b - delta**(1/2)) / (2*a))

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    x = lower
    step = (abs(lower)+abs(upper))/30000
    upper_limit = float(upper)
    result = 0
    while x < upper_limit:
        result += eval(function)
        x += step
    return result*step

if __name__ == '__main__':
    print(fact(5))
    print(roots(0, 0, 4))
    print(integrate('x ** 2 - 1', -1, 1))