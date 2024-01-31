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

    return system("clear"), print("Sucessfully trainer\n")

def edit():
    while True:
        system("clear")
        print("""
            ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° 
            °                                   °     
            °     ACTUALIZACION  DE TRAINER     °
            °                                   °
            ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °
            """)
        
        codigo = int(input("Ingrese el código del trainer que deseas actualizar: "))
        print(f""" 
    ___________________________
            
    Codigo: {codigo}
    Nombre: {listatrainer[codigo].get('Nombre')}
    Apellido: {listatrainer[codigo].get('Apellido')}
    Edad: {listatrainer[codigo].get('Edad')}
    Género: {listatrainer[codigo].get('Genero')}
    ___________________________
    """)
        
        print("¿Este es el trainer que deseas actualizar?")

        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if opc == 1:
            info = {
                "Nombre": input("Ingrese el nombre del trainer: \n"),
                "Apellido": input("Ingrese el apellido del trainer: \n"),
                "Edad": int(input("Ingrese la edad del trainer: \n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted (generos)]))
            }
                
            listatrainer[codigo] = info 
            with open("module/storage/trainer.json","w") as f:
                data = json.dumps(listatrainer, indent=4)
                f.write(data)
            print("\nTRAINER ACTUALIZADO\n")
            break
             
        elif(opc == 3): print("Edit to trainer")

   

def search():
    system("clear")
    print("""
          ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °
          °                             °     
          °      LISTA DE TRAINERS      °
          °                             °
          ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° 
          """)
    for i,numeracion in enumerate(listatrainer):
        
        print(f"\nCódigo: {i}\n")
        print(f"Nombre: {numeracion.get('Nombre')}")
        print(f"Apellido: {numeracion.get('Apellido')}")
        print(f"Edad: {numeracion.get('Edad')}")
        print(f"Genero: {numeracion.get('Genero')}")
        print("___________________")

  

def delete():
    while True:
        system("clear")
        print("""
                    ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° 
                    °                                   °     
                    °     ELIMINACIÓN DE TRAINERS       °
                    °                                   °
                    ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °
                    """)
        codigo = int(input("Ingrese el código del trainer que deseas eliminar: "))
        print(f""" 
            ___________________________
                    
            Codigo: {codigo}
            Nombre: {listatrainer[codigo].get('Nombre')}
            Apellido: {listatrainer[codigo].get('Apellido')}
            Edad: {listatrainer[codigo].get('Edad')}
            Género: {listatrainer[codigo].get('Genero')}
            ___________________________
            """)
        print("¿Este es el trainer que deseas eliminar?")
        print ("1. Si")
        print ("2. No")
        print ("3. Salir")
        opc = int(input())

        if opc == 1:
            listatrainer.pop(codigo)
            with open("module/storage/trainer.json","w") as f:
                    data = json.dumps(listatrainer, indent=4)
                    f.write(data)
            print("\nTRAINER ELIMINADO\n")
            break
        elif opc == 2:
            system("clear")
        elif opc == 3:
            break


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
