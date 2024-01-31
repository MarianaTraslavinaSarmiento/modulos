from os import system
from module.validate import menuNoValid

def menu():
    while True:
        print("CRUD de la coordinación")
        print("\t1. Asignación de camper a trainer")
        print("\t2. Remover el camper del trainer")
        print("\t3. Listar cuántos camper hay por trainer")
        print("\t4. Filtrar los géneros de los campers por trainer ")
        opc = int(input())

        match (opc):
                case 1:
                    system("clear")
                case 2:
                    system("clear")
                case 3:
                    system("clear")
                case 4:
                    system("clear")
                case 0:
                    system("clear")
                    break

