
salario = float(input("Informe o salário:"))
percentual = 0
reajuste = 0.0


if salario <= 1200:
    percentual = 20

elif salario <= 1700:
    percentual = 15
    
elif salario <=2500:
    percentual = 10
else:
    percentual = 5  

reajuste = salario * (percentual / 100)


print(f"O salário antes do reajuste: {salario}")
print(F"O percentual de aumento aplicado: {percentual}%")
print(f"O valor do aumento: {reajuste}")
print(f"O novo salário, após o aumento: {salario + reajuste}")
