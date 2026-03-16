#Exercício 1
velocidade = int(input('digite a velocidade: '))
tempo = int(input('digite o tempo: '))
distancia = velocidade*tempo
lu = distancia/12
print(f"velocidade\t{velocidade}\ntempo\t{tempo}\ndistancia\t{distancia}\nlitros usados\t{lu}")

#Exercício 2
tfa = int(input('Digite a temperatura em farenheit: '))
tce = ((tfa-32)*5/9)
print(f"temperatura em celsius: {tce}")PI = 3.141592

#Exercício 3
r = int(input('Digite o raio do cilindro: '))
h = int(input('Digite a altura do cilindro: '))
V = PI*(r*r)*h
print(f"Volume: {V}")

#Exercício 4
a = input('Digite o valor de A: ')
b = input('Digite o valor de B: ')
c = a
a = b
b = c
print("a:",a,"b:", b)

#Exercício 5
Val = int(input('digite um valor: '))
Val *= Val
print("Valor ao quadrado",Val)

#Exercício 6
V = int(input('Digite o valor: '))
Tx = int(input('Digite a taxa: '))
T = int(input('Digite o tempo: '))
P = V+(V*(Tx/100)*T)
print(f"prestação {P}")

#Exercício 7
Nc = int(input('Digite o numero de coelhos: '))
C = (Nc*0.7)/18+10
print(f"Custo: {C}")
