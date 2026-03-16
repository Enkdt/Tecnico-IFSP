#Exercício 1
for i in range (1,21,2):
    print(i)

#Exercício 2
a=0
for i in range (1,101):
    a+=i
print(a) 

#Exercício 3
num = int(input("Digite o número que deseja realizar a tabuada: "))
max = int(input("Digite o máximo que quer chegar na tabuada: "))
for i in range(max+1):
    print(f"{num}*{i} = {num*i}")

#Exercício 4
i=0
n =  float(input("Digite um número"))
while n>50 or n<=0:
    n = float(input("Numero invalido! Digite outro"))
while(n*3<250):
    i+=1
    n*=3
print(f"numero de iterações {i}\nNumero final:{n}")

#Exercício 5
for i in range(0,201,4):
    print(i)

#Exercício 6
for i in range(15,201,1):
    print("O quadrado de "+str(i)+" é:",i*i)

#Exercício 7
for i in range(1,15,1):
    sq*=i
    print(sq)

#Exercício 7 versão user
sq = float(input("Digite o numero que deseja elevar"))
ran = input("Digite o valor máximo e mínimo para começar").split()
while len(ran)!=2:
    print("Valores inválidos, digite outros")
    ran = input("Digite o valor máximo e mínimo para começar").split()
ran = list(map(int,ran))
x = 1
for i in range(ran[0],ran[1]+1,1):
    x*=sq
    print(f"O número {sq:.2f} elevado a {i} é: {x:.2f}")

#Exercício 8
new=0
antPrev = 0
prev = 1
for i in range(1,16,1):
    new = antPrev + prev
    print(prev)
    antPrev = prev
    prev = new

#Exercício 9
sq = float(input("Digite o numero que deseja elevar"))
ran = input("Digite o valor máximo e mínimo para começar").split()
while len(ran)!=2:
    print("Valores inválidos, digite outros")
    ran = input("Digite o valor máximo e mínimo para começar").split()
ran = list(map(int,ran))
x = 1
for i in range(ran[0],ran[1]+1,1):
    x*=sq
    print(f"O número {sq:.2f} elevado a {i} é: {x:.2f}")

#Exercício 10
sq = float(input("Digite o numero que deseja elevar"))
ran = int(input("Digite por quanto deseja elevar"))
x=1
for i in range(0,ran,1):
    x*=sq
    print(x)

print(f"O número {sq} elevado a {i+1} é: {x}")

#Exercício 11
li = []
for i in range(0,5,1):
    a = float(input("Digite o número que deseja adicionar a lista"))
    li.append(a)
li.sort()
print(li)
