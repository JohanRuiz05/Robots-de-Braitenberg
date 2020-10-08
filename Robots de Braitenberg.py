import time
import os

tamano = 10
matriz1 = []

valorFila = 0
valorColumna = 0

def borrar ():
            if os.name == "posix":
                        os.system ("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                        os.system ("cls")
    
for j in range (1):
    matriz1.append ([])
    
    for i in range (tamano-3):
            matriz1[j].append ("Ω")

    for i in range (tamano):
            matriz1[j].append ("ø")

print ("SIMULACIÓN VEHÍCULOS DE BRAITENBERG")
print ("")
print ("La simulación consta de tres características:")
print ("")
print ("- La zona iluminada se representa con Ω")
print ("- La zona obscura se representa con ø")
print ("- El robot se representa con ¶")
       
print ("")
time.sleep(10)

matriz1[valorFila][valorColumna] = "¶"

for j in range (1):
    for i in range (tamano):
        print (matriz1[j][i], end = " ")
    print()
    time.sleep(3)
    borrar ()

print ()
    
while valorColumna <= tamano-5:
    
    valorColumna += 1
    
    matriz1[valorFila][valorColumna] ="¶"
    matriz1[valorFila][valorColumna-1] = "Ω"
    
    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
        print()
        if valorColumna != tamano-4:
            time.sleep(3)
            borrar ()
        else:
            borrar()
        
    print ("")

for j in range (1):
    for i in range (tamano):
        print (matriz1[j][i], end = " ")
    print()
    print ("")
    print ("Proceso terminado - Robot tímido")
    print ("")

