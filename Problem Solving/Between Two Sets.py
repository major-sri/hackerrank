def gcd(a,b):
   
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    
    return a * b / gcd(a, b)

def GCD(terms):
   
    result = terms[0]
    for i in range(1, len(terms)):
        result = gcd(result, terms[i])
    return result

def LCM(terms):
   
    result = 1
    for t in terms:
        result = lcm(result, t)
    return result

def getTotalX(a, b):
    lcm_value = LCM(a)
    gcd_value = GCD(b)
    counter = 0
    multiple_lcm = lcm_value
    while multiple_lcm <= gcd_value:
        if (gcd_value % multiple_lcm) == 0:
            counter += 1
        multiple_lcm += lcm_value
    return counter