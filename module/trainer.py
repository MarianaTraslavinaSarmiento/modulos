from os import system
from .validate import menuNoValid

def save():
    print("Sucessfully Trainer\n")

def edit():
    print("Edit to trainer\n")

def search():
    print("Trainer is available\n")

def delete():
    print("Trainer deleted\n")

def menu():
    while True:
        print("CRUD del trainer")
        print("\t1. Guardar trainerr")
        print("\t2. Buscar trainer")
        print("\t3. Actualizar trainer")
        print("\t4. Eliminar trainer")
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
