from os import system#system("cls")
platinum=[  1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
gold=[  21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
silver=[    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
asientos=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
          41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
          51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
          61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
          71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
          81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
          91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
asientos_visual=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
          41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
          51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
          61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
          71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
          81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
          91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
ventas=[]
def Comprar_entradas():
    
    cant_entradas=int(input("Cuantas entradas quiere comprar?\n"))
    if cant_entradas<1 or cant_entradas>3:
        print("Cantidad no valida, por favor compre entre 1 o 3 entradas.\n")
    else:
        seccion=input("""En que seccion quiere sentarse?
        1.-Asientos Platinum, $120.000, Asientos 1-20
        2.-Asientos Gold, $80.000, Asientos 21-50
        3.-Asientos Silver, $50.000, Asientos 51-100\n""")
        compra=[cant_entradas]
        if seccion=="1":
                precio=120000
        elif seccion =="2":
                precio=80000
        elif seccion =="3":
                precio=50000
        
        match cant_entradas:
            case 3:
                entrada1=int(input("Seleccione un asiento y presione enter\n"))
                if seccion=="1":
                    if entrada1<0 or entrada1>20:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                if seccion=="2":
                    if entrada1<21 or entrada1>50:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                if seccion=="3":
                    if entrada1<51 or entrada1>100:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                entrada2=int(input("Seleccione otro asiento y presione enter\n"))
                if seccion=="1":
                    if entrada2<0 or entrada2>20:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada2
                if seccion=="2":
                    if entrada2<21 or entrada2>50:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada2
                if seccion=="3":
                    if entrada2<51 or entrada2>100:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada2
                entrada3=int(input("Seleccione el ultimo asiento y presione enter\n"))
                if seccion=="1":
                    if entrada3<0 or entrada3>20:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada3
                if seccion=="2":
                    if entrada3<21 or entrada3>50:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada3
                if seccion=="3":
                    if entrada3<51 or entrada3>100:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada3
                run_cliente=(f"Ingrese su RUN sin puntos ni digito verificador para finalizar su compra de {cant_entradas} entradas por ${precio*cant_entradas}\n")
                asientos[compra[0]]=run_cliente
                asientos[compra[1]]=run_cliente
                asientos[compra[2]]=run_cliente
                asientos_visual[entrada1] = "X"
                asientos_visual[entrada2] = "X"
                asientos_visual[entrada3] = "X"
                ventas.append=(precio*cant_entradas)
            case 2:
                entrada1=int(input("Seleccione un asiento y presione enter\n"))
                if seccion=="1":
                    if entrada1<0 or entrada1>20:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                if seccion=="2":
                    if entrada1<21 or entrada1>50:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                if seccion=="3":
                    if entrada1<51 or entrada1>100:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                entrada2=int(input("Seleccione otro asiento y presione enter\n"))
                if seccion=="1":
                    if entrada2<0 or entrada2>20:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada2]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada2
                if seccion=="2":
                    if entrada2<21 or entrada2>50:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada2]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada2
                if seccion=="3":
                    if entrada2<51 or entrada2>100:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada2]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada2
                run_cliente=(f"Ingrese su RUN sin puntos ni digito verificador para finalizar su compra de {cant_entradas} entradas por ${precio*cant_entradas}\n")
                asientos[compra[0]]=run_cliente
                asientos[compra[1]]=run_cliente
                asientos_visual[entrada1] = "X"
                asientos_visual[entrada2] = "X"
                ventas.append=(precio*cant_entradas)
            case 1:
                entrada1=int(input("Seleccione un asiento y presione enter\n"))
                if seccion=="1":
                    if entrada1<0 or entrada1>20:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                if seccion=="2":
                    if entrada1<21 or entrada1>50:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                if seccion=="3":
                    if entrada1<51 or entrada1>100:
                        print("Ese asiento no está en su seccion.\n")
                    elif asientos_visual[entrada1]=="X":
                        print("Ese asiento no está disponible")
                    else:
                        compra.append=entrada1
                run_cliente=(f"Ingrese su RUN sin puntos ni digito verificador para finalizar su compra de {cant_entradas} entradas por ${precio*cant_entradas}\n")
                asientos[entrada1+1]=run_cliente
                asientos_visual[entrada1] = "X"
                ventas.append=(precio*cant_entradas)
                print("Operacion realizada correctamente.\n")
                input("Presione enter para continuar...")

def Visualizar_asientos():
    print("Estos son los asientos disponibles:\n")
    for num in asientos_visual:
        print(asientos_visual[num-1], end=" ")
        if num==10 or num==20 or num==30 or num == 40 or num == 50 or num == 60 or num==70 or num==80 or num==90:
           print("\n")
    input("Presione enter para continuar...")

def ver_asistentes():
    print("Estos son los RUN de los asistentes pertenecientes a cada asiento:\n")
    for num in asientos:
        if (asientos[num-1]<10000000):
            print(f"Asiento {asientos_visual[num-1]}: vacio\n")
        else:
            print(f"Asiento {asientos_visual[num-1]}: {asientos[num-1]} \n")

def ganancias():
    print("Las ganancias totales son:\n")
    for num in ventas:
        ventas[num] + ventas[num+1]
    print(f"${ventas}")
    input("Presione enter para continuar...")




while(True):
    from os import system
    system("cls")
    op=input("""CREATIVOS.CL
    MICHAEL JAM CONCIERTO VIP
    Seleccione una opcion:
        1.-Comprar entradas
        2.-Mostrar asientos disponibles
        3.-Ver listado de asistentes
        4.-Mostrar Ganancias totales
        5.-Salir\n""")
    match op:
        case "1":
            Comprar_entradas()
        case "2":
            Visualizar_asientos()
        case "3":
            ver_asistentes()
        case "4":
            ganancias()
        case "5":
            break
        case other:
            print("Seleccione una opcion valida.\n")
##https://github.com/MatiasColomer/examenpgy1121
