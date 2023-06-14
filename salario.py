salario = float(input("Digite o salario:"))
#if salario >= 10000 or salario <= 15000:
if 10000 <= salario <= 15000:
    inss = salario * 0.11
    imposto_renda = salario * 0.275
    print("inss:", inss, "imposto de renda:", imposto_renda)
    print("Salario Liquido:", (salario-inss-imposto_renda))
else:
    print("Salário está fora da faixa de impostos")
