#importar librerias
import os
import time
import random

#definir coleccion
pedido = []
nombre = {}
comuna = ("San Bernardo", "Calera de tango", "Buin")
sacos = {}

#definir funciones
def registrar_pedido(pedido):
    nombre = input("Ingrese el nombre y apellido del cliente: ").lower()
    comuna = input("Ingrese la comuna del cliente (San Bernardo/Calera de Tango/Buin): ").lower()
    sacos = int(input("Ingrese cual saco de kg desea (5/10/20): "))
    num = print(f"El numero de su pedido es: {random.randint}")

def listar_pedidos(pedido):
    print({
        "Nombre" : nombre,
        "Comuna" : comuna,
        "Sacos" : sacos
    })
def imprimir_hoja(pedido):
    print()
            
#menu
while True:
    print("Bienvenido a CatPremiun")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opcion = int(input("Ingrese una opcion del menu: "))
    if opcion == 1:
        registrar_pedido(pedido)
    elif opcion == 2:
        listar_pedidos(pedido)
    elif opcion == 3:
        imprimir_hoja(pedido)
    elif opcion == 4:
        break        
    else:
        print("La opcion ingresada no es valida. Seleccione nuevamente")


