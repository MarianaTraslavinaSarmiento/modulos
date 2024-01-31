from os import system
from .validate import menuNoValid
from .data import listatrainer, generos
import json

def save():
    info = {
            "Nombre": input("Ingrese el nombre del trainer: \n"),
            "Apellido": input("Ingrese el apellido del trainer: \n"),
            "Edad": int(input("Ingrese la edad del trainer: \n")),
            "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted (generos)]))
        }    
    listatrainer.append(info)
    with open("module/storage/trainer.json","w") as f:
        data = json.dumps(listatrainer, indent=4)
        f.write(data)

    return system("clear"), print("Sucessfully Camper\n")

def edit():
    print("Edit to trainer\n")

def search():
    print(listatrainer)
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
