from os import system
from .data import camper
from .validate import menuNoValid

def save(nombre):
    camper.append(nombre)
    return print(f"Sucessfully Camper {nombre}\n")

def edit():
    print("Edit to camper\n")

def search():
    print("The camper is available\n")

def delete():
    print("Camper deleted\n")

def menu():
    while True:
        print("CRUD del camper")
        print("\t1. Guardar camper")
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        print("\t4. Eliminar camper")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1:
                system("clear")
                save()
            case 2:
                system("clear")
                search()
            case 3:
                system("clear")
                edit()
            case 4: 
                system("clear")
                delete()
            case 0:
                system("clear")
                break
            case _:
                menuNoValid(opc)


