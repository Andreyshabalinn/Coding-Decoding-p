def gcd(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a 

a = int(input("Введите первое число ")) 
b = int(input("Введите второе число ")) 
print(gcd(a,b))