# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("1 - Soma")
print("2 - Divisão")
print("3 - Multiplicação")
print("4 - Subtração")

operacao = input("Selecione uma operação (1/2/3/4): ")

# Receba os números como strings e converta para floats
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "1":
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")

elif operacao == "2":
    if numero2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado}")

elif operacao == "3":
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado}")

elif operacao == "4":
    resultado = numero1 - numero2
    print(f"Resultado da subtração: {resultado}")

else:
    print("Operação inválida.")