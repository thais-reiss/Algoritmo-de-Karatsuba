def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y))) 
    meio = n // 2                     

    x_maior = x // (10 ** meio)         
    x_menor = x % (10 ** meio)

    y_maior = y // (10 ** meio)
    y_menor = y % (10 ** meio)

    a = karatsuba(x_maior, y_maior)
    c = karatsuba(x_maior + x_menor, y_maior + y_menor)
    b = karatsuba(x_menor, y_menor)
    d = c - a - b
    return a * (10**(2*meio)) + d * (10**meio) + b

# Pra testar:
resultado = karatsuba(12024, 2563)
print(resultado)

