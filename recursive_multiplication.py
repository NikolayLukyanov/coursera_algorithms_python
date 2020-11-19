# x = 10^n/2*a + b, y = 10^n/2*c + d
# x*y = 10^n*ac + 10^n/2(ad+bc) + bd
# recurcively compute ac, ad, bc, bd, then x*y

def check_list_int(x) -> bool:
    if type(x) is not list:
        print(type(x))
        return False
    for item in x:
        if type(item) is not int:
            print(item, type(item))
            return False
    return True

def int_to_list(x: int) -> list:
    
def recursive_multiplication(x: list, y: list) -> int:
    if check_list_int(x) is False or check_list_int(y) is False:
        raise ValueError("both multipliers should be list of integer")
    if abs(len(x) - len(y)) > 1:
        raise ValueError("this algorithm only for equal size numbers")
    if (len(y) == 1):
        return x[0]*y[0]
    if (len(x) == 1 and len(y) == 2):
        return recursive_multiplication([0,x[0]], y)
    # assuming that multiplication by 10^n does not need to be implemented
    result =  (10**((len(y)//2 + len(y)%2)*2))*recursive_multiplication(x[:len(y)//2], y[:len(y)//2]) + (10**((len(y)//2 + len(y)%2)))*(recursive_multiplication(x[:len(y)//2], y[len(y)//2:]) + recursive_multiplication(y[:len(y)//2], x[len(y)//2:])) + recursive_multiplication(x[len(y)//2:], y[len(y)//2:])
    return result
