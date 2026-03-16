#Exercício 1
x = []
for i in range(0,3):
    x.append(float(input(f"Digite a {i+1} nota ")))
media=[sum(x)/3]
print(media)
if media[0]>6:
    print("Voce foi aprovado!")
else:
    print(f"Acabe com tudo, voce tirou: {media}") 
    
#Exercício 2
x = []
for i in range(0,3):
    x.append(float(input(f"Digite a {i+1} nota ")))
media=[sum(x)/3]
print(media)
if media[0]>6:
    print("Voce foi aprovado!")
else:
    media.append(float(input("Digite a nota do exame ")))
    newMedia = sum(media)/2
    if newMedia>=5:
        print("Aprovado por exame!")
    else:
        print(f"Acabe com tudo, voce tirou: {newMedia}")
        
#Exercício 3
x = []
for i in range(0,2):
    x.append(float(input(f"Digite o {i+1} numero")))    
print("A diferença entre eles é: ",abs(x[0]-x[1]))

#Exercício 4
x = []
for i in range(0,3):
    x.append(float(input(f"Digite o {i+1} numero: ")))
if x[0]<x[1]+x[2] and x[1]<x[0]+x[2] and x[2]<x[0]+x[1]:
    if x[0] == x[1] == x[2]:
        print("É equilátero")
    elif x[0]!=x[1]!=x[2]:
        print("É escaleno")
    else:
        print("É isóceles")
else:
    print("Não é triangulo")
    
#Exercício 5
x = []
for i in range(0,3):
    x.append(float(input(f"Digite o {i+1} numero: ")))
x.sort()
print(x)

#Exercício 6
υπάρχοντα = []
for i in range(0,3):
    υπάρχοντα.append(float(input(f"Digite o {i+1}o valor: ")))

Δ = υπάρχοντα[1]*υπάρχοντα[1]-4*υπάρχοντα[0]*υπάρχοντα[2]
print(Δ)
if Δ>0:
    print("raiz 1:",(-υπάρχοντα[1]+Δ**0.5)/2*υπάρχοντα[0],"raiz 2:",(-υπάρχοντα[1]-Δ**0.5)/2*υπάρχοντα[0])
elif Δ==0:
    print("raiz:",(-υπάρχοντα[1]+Δ**0.5)/2*υπάρχοντα[0])
else:
    print("Não há raizes reais")
    
#Exercício 7
x = abs((float(input(f"Digite o numero: "))))
print(x)

#Exercício 8
x = []
y = []
for i in range(0,3):
    x.append(int(input(f"Digite o {i+1} numero: ")))
    if x[i]%3==0 and x[i]%2==03:
        y.append(x[i])
print(y)

#Exercício 9
x = []
y = []
for i in range(0,2):
    x.append(int(input(f"Digite o {i+1} numero: ")))
    if x[i]%4==0 or x[i]%5==0:
        y.append(x[i])
print(y)

#Exercício 10
x = (int(input(f"Digite o numero: ")))
while(x>12 or x<1):
    print("LoL, esse mês não existe!")
    x = (int(input(f"Digite o numero: ")))

mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
for i in range (1,12):
    if x==i:
        print(mes[i-1])
