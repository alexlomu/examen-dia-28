from ejercicios import *
from ejercicios.ej2 import determinante_iterativo, determinante_recursivo

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al menú  ")
        print("========================")
        print("  Selecciona a que ejercicio quieres acceder  ")        
        print("========================")        
        print("[1] EJERCICIO 1 ")
        print("[2] EJERCICIO 2 ")
        print("[3] EJERCICIO 3 ")
        print("[4] EJERCICIO 4 ")
        print("[5] Salir del menú ")
        print("===================")


        opcion = input("> ")

        if opcion == "1":
            ej1()
        
        elif opcion =="2":
            print("=========================================================================")
            print("                      Has accedido al ejercicio 2                        ")
            print("=========================================================================")
            print("  Deseas resolver el determinante de forma recursiva(1) o iterativa(2)?  ")        
            print("=========================================================================")
            seleccion = int(input("Introduce 1 o 2 >>>"))
            if seleccion == 1:
                print(determinante_recursivo([2,3,4],[1,4,2],[5,3,1]))
            elif seleccion == 2:
                determinante_iterativo([[2,3,4],[1,4,2],[5,3,1]])


        elif opcion =="3":
            ej3()

        elif opcion =="4":
            ej4()
        
        elif opcion == "5":
            break

if __name__ == "__main__":
    iniciar()