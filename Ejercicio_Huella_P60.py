import random
import webbrowser

nombres = []
huellas = []
codigos = []
numPersonas = 0

def menu_opciones():
    while True:
        print("¿Qué acción desea realizar?: ")
        print('*  1) Ingresar usuarios')
        print('*  2) Mostrar usuarios')
        print('*  3) Buscar y enviar código de recuperación')
        print('*  4) Salir del sistema')
        opcion = input("Ingrese la opción: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion in [1, 2, 3, 4]:
                return opcion
            else:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
        else:
            print("Entrada no válida. Por favor, ingrese solo números.")

def ingreso_personal(numPersonas):

     while numPersona<1 or numPersona>20:
        print("NUMERO DE PERSONAS NO VALIDO.")
        print("MAXIMO 20 PERSONAS Y NO MENOS DE 1.")
        numPersona = int(input("Ingrese el número de personas a registrar: "))
    
    for i in range(numPersonas):
        print(f"Ingrese los datos de la persona {i + 1}")
        nombreUsuario = input("Nombre: ")
        huellaUsuario = input("Huella: ")
        nombres.append(nombreUsuario)
        huellas.append(huellaUsuario)
        codigos.append(random.randrange(1000, 9999))

def mostrar_registros(numPersonas):
    for i in range(numPersonas):
        print("-------------------------------------")
        print(f"Mostrando los datos de la persona {i + 1}")
        print("* Nombre:", nombres[i])
        print("* Huella dactilar:", huellas[i])
        print("* Código de acceso:", codigos[i])
        print("-------------------------------------")

def buscarEnviarCodigo(nombreUsuario):
    if nombreUsuario in nombres:
        indice = nombres.index(nombreUsuario)
        print("Usuario encontrado")
        print("¿Desea enviar el código a su número de teléfono?")
        opcion = input("Ingrese 'si' o 'no': ").lower()
        if opcion == "si":
            num = input("Ingrese el número de teléfono: ")
            url = f'https://api.whatsapp.com/send?phone={num}&text=El código de recuperación es: {codigos[indice]}'
            webbrowser.open(url)
    else:
        print("No existe ese usuario registrado")

def main():
    print("--------------- SISTEMA DACTILAR -------------")
    print("------------------- Bienvenido -------------------")
    
    while True:
        caso = menu_opciones()
        
        if caso == 1:
            numPersonas = int(input("Ingrese el número de personas a registrar: "))
            while numPersonas <= 0:
                print("El número de personas debe ser mayor que cero.")
                numPersonas = int(input("Ingrese el número de personas a registrar: "))
            ingreso_personal(numPersonas)

        elif caso == 2:
            mostrar_registros(numPersonas)

        elif caso == 3:
            personaBuscar = input("Ingrese nombre de la persona a enviar el código: ")
            buscarEnviarCodigo(personaBuscar)

        elif caso == 4:
            print("Saliendo del sistema...")
            break

        print("")

main()
