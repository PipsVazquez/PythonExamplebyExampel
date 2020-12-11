import random #Llamar al módulo random


for iteraciones in range(0, 100): #For para sacar 100 números random
  numero_aleatorio = random.randint(0, 30) #le asigno un número random
  print(f'Esta es la iteracion {iteraciones} y es el numero {numero_aleatorio}')

  if numero_aleatorio == 25: #Condicion para romper el for
    break


