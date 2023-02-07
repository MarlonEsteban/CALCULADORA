import math
import cmath as cm
from numeros_complejos.Fun.operaciones import convercion as con
from numeros_complejos.Fun.operaciones import basica as bs
from numeros_complejos.Fun.operaciones import basica_1 as b1
from numeros_complejos.Fun.operaciones import basica_2 as b2
from numeros_complejos.Fun.operaciones import RES
from numeros_complejos.Fun.operaciones import induc
from numeros_complejos.Fun.operaciones import conden

    
while True:
    print("CALCULADORA DE NUMEROS COMPLEJOS")
    print("")
    print("="*50)
    print("  ||        INGRESE OPCION A REALIZAR      ||")
    print("="*50)
    print(""*2)
    print("1) Transformación de coordenadas ")
    print("2) Suma de coordenadas rectangulares")
    print("3) Resta de coordenadas rectangulares")
    print("4) Multiplicación de coordenadas polares")
    print("5) División de coordenadas polares")
    print("6) Operaciones de circuitos electricos")
    print("7) Salir")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        print("Transformación de coordenadas")
        print("Menu de transformaciones")
        print("1) Coordenadas polares a coordenadas rectangulaes")
        print("2) Coordenadas rectangulaes a Coordenadas polares")
        print("3) Regresar al menu principal")
        opcion=int(input("Seleccione la operacion a realizar: "))
        if opcion == 1:
            a = float(input("Ingresa el módulo: "))
            b= float(input("Ingresa el ángulo (en grados): "))
            print("")
            con.polar_a_rectangular(a,b)
            print("")
        elif opcion == 2:
            x= float(input("Ingresa el numero real (x): "))
            y= float(input("Ingresa el numero imaginario (y): "))
            print("")
            con.convercion(x, y)
            print("")
    elif opcion == 2:
        comp_num = []
        n = int(input("Ingrese la cantidad de números complejos que desea sumar: "))
        for i in range(n):
            real = float(input(f"Ingrese la parte real del número complejo {i+1}: "))
            imag = float(input(f"Ingrese la parte imaginaria del número complejo {i+1}: "))
            comp_num.append((real, imag))
            result = bs.suma_comp(comp_num)           
        print("")
        print("La suma de los números complejos es:", result)
        print("")
        
         
    elif opcion == 3:
        com_num = []
        n = int(input("Ingrese el número de números complejos que desea restar: "))
        for i in range(n):
            real = float(input(f"Ingrese la parte real del número complejo {i+1}: "))
            imag = float(input(f"Ingrese la parte imaginaria del número complejo {i+1}: "))
            com_num.append((real, imag))
            result = bs.res_comp(com_num)
        print("")
        print(f"La resta de los números complejos es: {result[0]},{result[1]}i")
        print("")
        
    elif opcion == 4:
         n = int(input("Ingrese el número de coordenadas polares a multiplicar: "))
         r = []
         theta = []
         for i in range(n):
             while True:
                 r_input = int(input("Ingrese el módulo de la coordenada polar {}: ".format(i + 1)))
                 if r_input >= 0:
                     break
                 print("El módulo no puede ser negativo")
             theta_input = int(input("Ingrese el argumento de la coordenada polar {} (en grados): ".format(i + 1)))
             r.append(r_input)
             theta.append(theta_input)

         result = b2.multiply_polar_coordinates(r, theta)
         
         z=round(cm.rect(result[0],math.radians(result[1])).real,3),round(cm.rect(result[0],math.radians(result[1])).imag,3)
         print("")
         print("El resultado de multiplicar las coordenadas polares es: (",result[0], ",",round(result[1],2), "°)")
         print("")
         print("El resultado en coordenadas rectangulares es:",z[0],",",z[1],"j")
         print("")
    elif opcion == 5:
        n = int(input("Ingrese el número de divisiones a realizar: "))
        numeros = []
        for i in range(n):
            while True:
                r = float(input("Ingrese el módulo del número en coordenadas polares {}: ".format(i+1)))
                if r < 0: print("El valor de r no puede ser negativo. Por favor, ingrese un valor válido.")
            else: break
            theta = math.radians(float(input("Ingrese el angulo de las coordenadas polares {} (en grados): ".format(i+1))))
            numeros.append(b1.Polar(r, theta))
        resultado = numeros[0]
        for i in range(1, n):
            resultado = resultado / numeros[i]
        z=round(cm.rect(resultado.r, resultado.theta).real,3),round(cm.rect(resultado.r, resultado.theta).imag,3)

        print("")
        print("El resultado de la división en coordenadas polares es: (r = {}, θ = {}°)".format(round(resultado.r,3),round(math.degrees(resultado.theta),3)))
        print("")
        print("El resultado de la división en coordenadas rectangulares es:",z[0],",",z[1],"j")
        print("")
        
    elif opcion == 6:
        print("Operaciones de circuitos electricos")
        print("Menu de operaciones")
        print("1) Resistencia equivalente con resultado en coordenadas polares y coordenadas rectangulaes")
        print("2) Transformacion de capacitores a fasores")
        print("3) Transformacion de inductores a fasores")
        print("4) Regresar al menu principal")
        opcion=int(input("Seleccione la operacion a realizar: "))
        if opcion == 1:
            num_resistencias = int(input("¿Cuántas resistencias hay en el circuito paralelo? "))
            resistencias = []
            for i in range(num_resistencias):
                magnitud = float(input(f"Ingrese la magnitud de la resistencia {i + 1}: "))
                angulo = math.radians(float(input(f"Ingrese el ángulo de la resistencia {i + 1} en grados: ")))
                resistencia = cm.rect(magnitud, angulo)
                resistencias.append(resistencia)
                
            resultado = RES.res_equ_pa(resistencias)
            print("")
            print("La resistencia equivalente en coordenadas rectangulares es:", resultado)
            print("")
            print("La resistencia equivalente en coordenadas polares es:",cm.polar(resultado))
            print("")
        elif opcion == 2:
            f=float(input("Ingrese la fecuencia de trabajo [Hercios (Hz)]:  "))
            C=float(input("Ingrese el valor del capacitor [faradios (f)]:  "))
            conden.impedan(f, C)
        elif opcion == 3:
            print("Ingrese los datos  ")
            f=float(input("Ingrese la fecuencia de trabajo [Hercios (Hz)]:  "))
            L=float(input("Ingrese el valor del inductor [henrios (H)]:  "))
            induc.impedancia(f, L)
    elif opcion == 7:
        print("Eso fue todo")
        break
    else:
         print("Opcion no valida")