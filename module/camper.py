
import json
from os import system
from .data import listacamper, generos
from .validate import menuNoValid

def save():
    info = {
        "Nombre": input("Ingrese el nombre del camper: \n"),
        "Apellido": input("Ingrese el apellido del camper: \n"),
        "Edad": int(input("Ingrese la edad del camper: \n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted (generos)]))
    }
    listacamper.append(info)
    with open("module/storage/camper.json","w") as f:
        data = json.dumps(listacamper, indent=4)
        f.write(data)
    return system("clear") , print("Sucessfully Camper\n")

def edit():
    while True:
        system("clear")
        print("""
            ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° 
            °                                   °     
            °     ACTUALIZACION  DE CAMPERS     °
            °                                   °
            ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °
            """)
        
        codigo = int(input("Ingrese el código del camper que deseas actualizar: "))
        print(f""" 
    ___________________________
            
    Codigo: {codigo}
    Nombre: {listacamper[codigo].get('Nombre')}
    Apellido: {listacamper[codigo].get('Apellido')}
    Edad: {listacamper[codigo].get('Edad')}
    Género: {listacamper[codigo].get('Genero')}
    ___________________________
    """)
        
        print("¿Este es el camper que deseas actualizar?")

        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if opc == 1:
            info = {
                "Nombre": input("Ingrese el nombre del camper: \n"),
                "Apellido": input("Ingrese el apellido del camper: \n"),
                "Edad": int(input("Ingrese la edad del camper: \n")),
                "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted (generos)]))
            }
                
            listacamper[codigo] = info 
            with open("module/storage/camper.json","w") as f:
                data = json.dumps(listacamper, indent=4)
                f.write(data)
            print("\nCAMPER ACTUALIZADO\n")
            break
                
        elif(opc == 3): print("Edit to camper")

   
            

def search():
    system("clear")
    print("""
          ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °
          °                             °     
          °      LISTA DE CAMPERS       °
          °                             °
          ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° 
          """)
    for i,numeracion in enumerate(listacamper):
        
        print(f"\nCódigo: {i}\n")
        print(f"Nombre: {numeracion.get('Nombre')}")
        print(f"Apellido: {numeracion.get('Apellido')}")
        print(f"Edad: {numeracion.get('Edad')}")
        print(f"Genero: {numeracion.get('Genero')}")
        print("___________________")
    
    print("The camper is available\n")

def delete():
    
    while True:  
        system("clear")
        print("""
                ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° 
                °                                   °     
                °     ELIMINACIÓN DE CAMPERS        °
                °                                   °
                ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °
                """)
        codigo = int(input("Ingrese el código del camper que deseas eliminar: "))
        print(f""" 
        ___________________________
                
        Codigo: {codigo}
        Nombre: {listacamper[codigo].get('Nombre')}
        Apellido: {listacamper[codigo].get('Apellido')}
        Edad: {listacamper[codigo].get('Edad')}
        Género: {listacamper[codigo].get('Genero')}
        ___________________________
        """)
            
        print("¿Este es el camper que deseas eliminar")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if (opc == 1):
            listacamper.pop(codigo)
            with open("module/storage/camper.json","w") as f:
                    data = json.dumps(listacamper, indent=4)
                    f.write(data)
            system("clear")
            print("\nCAMPER ELIMINADO\n")
            break
        elif (opc == 2):
            system("clear")
        elif (opc == 3):
            break
        print("Camper deleted\n")

def menu():
    bandera = True
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
                bandera = False
            case _:
                menuNoValid(opc)


