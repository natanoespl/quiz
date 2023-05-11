print("Seja bem vindo ao meu QUIZ!")

nome = input("Antes de começarmos, qual o seu nome? ")
print("Olá, " +nome)

jogando = input("Você quer jogar? ")

if jogando.lower() != "sim":
    quit()

print("Que bom! Vamos jogar :)")
score = 0

resposta = input("Qual o significado da sigla CPU? ")
if resposta.lower() == "central processing unit":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

resposta = input("Qual o significado da sigla GPU? ")
if resposta.lower() == "graphics processing unit":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

resposta = input("Qual o significado da sigla RAM? ")
if resposta.lower() == "random access memory":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

resposta = input("Qual o significado da sigla PSU? ")
if resposta.lower() == "power supply":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")    

if score > 1: 
    print("Parabéns," ,nome, "você acertou " + str(score) + " questões!")
    print("A sua porcentagem de acertos foi de: " +str((score / 4) * 100) + "%.")

elif score == 1:
    print("Parabéns," ,nome, "você acertou " +str(score) + " questão")
    print("A sua porcentagem de acertos foi de: " +str((score / 4) * 100) + "%.")

else:
    print("Infelizmente você errou todas as questões!")
