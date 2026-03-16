#Exercício 1
x = float(input("Digite o valor em real para ser transformado em dolar"))
x /=2.4
print("valor em dolar:",x)

#Exercício 2
x = float(input("Digite o valor em dolar para ser transformado em reais"))
x *=2.4
print("valor em reais:",x)

#Exercício 3
from math import ceil
ap = float(input("Digite a altura da parede")) *  float(input("Digite a largura da parede"))
aa = float(input("Digite a altura do azulejo")) *  float(input("Digite a largura do azulejo"))
print(ceil(ap/aa))

#Exercício 4
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
A = a * b
P = 2 * a + 2 * b
print("Área:", A)
print("Perímetro:", P)

#Exercício 5
m = float(input("digite a massa: "))
h = float(input("digite a altura: "))
IMC = m / (h ** 2)
print("IMC:", IMC)

#Exercício 6
import math
r = float(input("digite o raio: "))
A = math.pi * r ** 2
C = 2 * math.pi * r
print("Área:", A)
print("Comprimento:", C)

#Exercício 7
R = float(input("digite o raio da esfera: "))
V = (4/3) * math.pi * R ** 3
A = 4 * math.pi * R ** 2
print("Volume:", V)
print("Área:", A)

#Exercício 8
n1 = float(input("digite a 1ª nota: "))
n2 = float(input("digite a 2ª nota: "))
n3 = float(input("digite a 3ª nota: "))
n4 = float(input("digite a 4ª nota: "))
media = (n1 + n2 + n3 + n4) / 4
print("Média final:", media)

#Exercício 9
P1 = float(input("digite a nota P1: "))
P2 = float(input("digite a nota P2: "))
Ativ = float(input("digite a nota das atividades: "))
media = (P1 * 4 + P2 * 4 + Ativ * 2) / 10
print("Média:", media)

#Exercício 10
a = input("digite o valor de a: ")
b = input("digite o valor de b: ")
c = a
a = b
b = c
print("a:", a)
print("b:", b)

#Exercício 11
a = input("digite o valor de a: ")
b = input("digite o valor de b: ")
a, b = b, a
print("a:", a)
print("b:", b)

#Exercício 12
espaco = float(input("digite o espaço percorrido: "))
tempo = float(input("digite o tempo gasto: "))
velocidade_media = espaco / tempo
print("Velocidade média:", velocidade_media)

#Exercício 13
s0 = 2
v0 = 3
a = 10
t = float(input("digite o valor de t: "))
s = s0 + v0 * t + 0.5 * a * t ** 2
print("s:", s)

