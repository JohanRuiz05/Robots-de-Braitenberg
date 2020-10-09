import time
import os

tamano = 10

def borrar ():
            if os.name == "posix":
                        os.system ("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                        os.system ("cls")

def robotTimido():

    matriz1 = []
    valorFila = 0
    valorColumna = 0
    
    for j in range (1):
        matriz1.append ([])
        
        for i in range (tamano-3):
                matriz1[j].append ("Ω")

        for i in range (tamano):
                matriz1[j].append ("ø")

    matriz1[valorFila][valorColumna] = "¶"

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
        print()
        time.sleep(1)
        borrar ()

    print ()
    
    while valorColumna <= tamano-4:

        valorColumna += 1
    
        matriz1[valorFila][valorColumna] ="¶"
        matriz1[valorFila][valorColumna-1] = "Ω"
    
        for j in range (1):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()
            if valorColumna != tamano-3:
                time.sleep(1)
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
        matriz1[valorFila][valorColumna] ="Ω"
        valorColumna = 0
        time.sleep(5)
        borrar ()
        print ("")

def robotIndeciso():

    matriz1 = []
    valorFila = 0
    contador = 0
    valorColumna = 0
   
    for j in range (1):
        matriz1.append ([])
        
        for i in range (tamano-3):
                matriz1[j].append ("Ω")

        for i in range (tamano):
                matriz1[j].append ("ø")

    matriz1[valorFila][valorColumna] = "¶"

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
        print()
        time.sleep(1)
        borrar ()

    print ()
    
    while valorColumna <= tamano-4:

        valorColumna += 1
    
        matriz1[valorFila][valorColumna] ="¶"
        matriz1[valorFila][valorColumna-1] = "Ω"
    
        for j in range (1):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()
            if valorColumna != tamano-3:
                time.sleep(1)
                borrar ()
            elif valorColumna == tamano-3 and contador < 2:
                matriz1[valorFila][valorColumna] ="ø"
                valorColumna -= 2
                contador += 1
                time.sleep(1)
                borrar()
                
        print ("")

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
            
        print()
        print ("")
        print ("Proceso terminado - Robot indeciso")
        time.sleep(5)
        borrar ()
        print ("")

def robotParanoico():

    matriz1 = []
    valorFila = 0
    valorColumna = 0
    
    for j in range (1):
        matriz1.append ([])
        
        for i in range (tamano-3):
                matriz1[j].append ("Ω")

        for i in range (tamano):
                matriz1[j].append ("ø")

    matriz1[valorFila][valorColumna] = "¶"

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
        print()
        time.sleep(1)
        borrar ()

    print ()
    
    while valorColumna <= tamano-4:

        valorColumna += 1
    
        matriz1[valorFila][valorColumna] ="¶"
        matriz1[valorFila][valorColumna-1] = "Ω"
    
        for j in range (1):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()
            if valorColumna != tamano-3:
                time.sleep(1)
                borrar ()
                
        print ("")

    if valorColumna == tamano-3:
                matriz1[valorFila][valorColumna] ="ø"
                valorColumna -= 1
                matriz1[valorFila][valorColumna] ="¶"
                time.sleep(1)
                borrar ()

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
            
        print()
        print ("")
        print ("Proceso terminado - Robot paranoico")
        time.sleep(5)
        borrar ()
        print ("")

def robotObstinado():

    matriz1 = []
    valorFila = 0
    valorColumna = 0

    for j in range (1):
        matriz1.append ([])
        
        for i in range (tamano-3):
                matriz1[j].append ("Ω")

        for i in range (tamano):
                matriz1[j].append ("ø")

    matriz1[valorFila][valorColumna] = "ø"
    matriz1[valorFila][7] = "Ω"
    matriz1[valorFila][8] = "Ω"

    valorColumna = 1

    matriz1[valorFila][valorColumna] = "¶"

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
        print()
        time.sleep(1)
        borrar ()

    print ()
    
    while valorColumna <= tamano-3:

        valorColumna += 1
    
        matriz1[valorFila][valorColumna] ="¶"
        matriz1[valorFila][valorColumna-1] = "Ω"

        global contador
    
        for j in range (1):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()
            if valorColumna != tamano-1:
                time.sleep(1)
                borrar ()
            else:
                borrar()
                
        print ("")

    while valorColumna >= tamano-8:
    
        matriz1[valorFila][valorColumna-1] ="¶"
        matriz1[valorFila][valorColumna] = "Ω"

        valorColumna -= 1

        global contador
    
        for j in range (1):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()
            if valorColumna != tamano-9:
                time.sleep(1)
                borrar ()
            else:
                borrar()
                
        print ("")

    for j in range (1):
        for i in range (tamano):
            print (matriz1[j][i], end = " ")
        print()
        print ("")
        print ("Proceso terminado - Robot obstinado")
        time.sleep(5)
        borrar ()
        print ("")

def robotConductor():

    matriz1 = []
    contador = 0
    while contador <4:
        matriz1.append ([])
        contador += 1
        
    for i in range (tamano):
            matriz1[1].append ("Ω")
            matriz1[2].append ("Ω")

    for i in range (tamano):
            matriz1[0].append ("ø")
            matriz1[3].append ("ø")
    
    valorFila = 1
    valorColumna = 0

    matriz1[1][0] ="¶"

    print ()
    time.sleep (1)
    
    while valorColumna <= tamano-1:
    
        matriz1[valorFila][valorColumna] ="¶"
        matriz1[valorFila][valorColumna] = "Ω"

        if valorColumna == 0 or valorColumna == 2 or valorColumna == 4 or valorColumna == 6 or valorColumna == 8:
            valorFila += 1
            matriz1[valorFila][valorColumna] ="¶"
                
        else:
            matriz1[valorFila][valorColumna-1] = "Ω"

        if valorColumna == 1 or valorColumna == 3 or valorColumna == 5 or valorColumna == 7 or valorColumna == 9:
            valorFila -= 1
            matriz1[valorFila][valorColumna] ="¶"
        else:
            matriz1[1][valorColumna-1] = "Ω"
    
        for j in range (4):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()

        time.sleep (1)
        valorColumna += 1
        borrar ()
        print ("")

    for j in range (4):
            for i in range (tamano):
                print (matriz1[j][i], end = " ")
            print()

    print ()   
    print ("Proceso terminado - Robot conductor")
    time.sleep(5)
    borrar ()
    print ("")

borrar ()
print ("SIMULACIÓN VEHÍCULOS DE BRAITENBERG")
print ("")
print ("La simulación consta de tres características:")
print ("")
print ("- La zona iluminada se representa con Ω")
print ("- La zona obscura se representa con ø")
print ("- El robot se representa con ¶")
print ("")
time.sleep(10)
borrar ()

robotTimido ()
robotIndeciso ()
robotParanoico ()
robotObstinado ()
robotConductor ()
