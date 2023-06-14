valores = input().split()
print(valores)
x = float(valores[0])
y = float(valores[1])
op = input()
if op == "+":
    resultado = x + y
elif op == "-":
    resultado = x - y
elif op == "*":
    resultado = x * y
elif op == "/":
    resultado = x / y
elif op == "**":
    resultado = x ** y
else:
    print(" O operador solicitado não é suportado.")
    erro = True
if erro != True:
    print(x, op, y, "=", resultado)
