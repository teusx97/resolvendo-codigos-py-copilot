# 1. Receber dois dados diferentes do usuário e concatná-los em uma string.

# Receber os dados do usuário
info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")

# Concatenar as informações
info_concatenada = info1 + " " + info2

# Exibir a informação concatenada
print("Informação concatenada: ", info_concatenada)

# 2. Solicitar uma string e um número do usuário e exibir a string repetida o número de vezes informado.

# Receber os dados do usuário
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
string_repetida = string * numero

# Exibir a string repetida
print("String repetida: " + string_repetida)

# 3. Solicitar dois numeros inteiros e exibir o resultado de alguma operação entre eles.

num1= int(input("Digite o primeiro número: "))
num2= int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = abs(num1 - num2)
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"

print("Resultado: ", resultado)