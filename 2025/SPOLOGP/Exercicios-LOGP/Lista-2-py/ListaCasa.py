#Exercício 1
x = int(input("Digite o número: "))
print(("Impar","Par")[x%2==0])asb = float(input("Digite o número chave: "))

#Exercício 2
input = abs(float(input("Digite o número normal: "))-asb)
print(input)

#Exercício 3
import math
x = float(input("Digite o número: "))
if x%1>0.5:
    print(math.ceil(x))
else:
    print(math.floor(x))

#Exercício 4    
x = []
for i in range(0,3):
    x.append(float(input(f"Digite a {i+1} nota ")))
x.sort()
print(x[0],x[2],x[1])

#Exercício 5 
x = float(input("Digite o número:"))
hr = float(input("Digite o tempo trabalhado:"))
if x<800:
    sal = x
elif 800>=x and x<=1600:
    sal=x-(x*0.08)-(x*0.05)
else:
    sal=x-(x*0.15)-(x*0.07)

if hr>160:
    extra = x/320*hr-160
    sal+=extra

print("salário:",sal)
