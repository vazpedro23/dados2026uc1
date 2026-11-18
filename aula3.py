# Revisão de códigos
# Crie um algoritmo para dizer se uma pessoa é maior de idade ou não
idade = int(input("Digite sua idade: "))
#
if idade >= 18:
    print("Você é maior de idade!")
    print("Você pode tirar a carteira de motorista")
else:
    print("Você ainda não é maior de idade.")
    faltam = 18 - idade
    print(f"Falta(m) {falta} ano(s) para fazer 18.")
#
