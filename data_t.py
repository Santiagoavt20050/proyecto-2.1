import data_t

import json

data = {}

RUTA_ARCHIVO = "gestiontrainer.json"

def guardar_datos():
    global data, RUTA_ARCHIVO
    try:
        with open(RUTA_ARCHIVO, "w") as file:
            json.dump(data, file, indent=4)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")
        
def cargar_datos():
    global data
    global RUTA_ARCHIVO
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente!!")
    except Exception:
        print("Error al cargar datos")

def registrar_trainer():
    global data
    doc = int(input("Ingrese el documento del trainer: "))
    trainer = {
        "Nombre": input("Ingrese el nombre del trainer: "),
        "Apellido": input("Ingrese los apellidos del trainer: "),
        "Direccion": input("Ingrese la dirección del trainer: "),
    }
    try:
        trainer["Telefono"] = int(input("Ingrese el número de contacto: "))
    except ValueError:
        print("Ingrese un valor válido para el número de contacto!")
        return
    trainer.update({"Horario": "", "Area de Trabajo": "", "Grupo del Trainer": ""})
    data[doc] = trainer

    guardar_datos()
    
def horario_del_trainer():
    global data
    doc = input("Ingrese el documento del trainer: ")
    if doc in data:
        data[doc]["horario"] = input("Ingrese el horario del trainer: ")
        print("Horario actualizado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún trainer registrado.")

def area_del_trainer():
    global data
    doc = input("Ingrese el documento del trainer : ")
    if doc in data:
        areatrainer = input("Ingrese el area del trainer: ")
        data[doc]["area del trainer"] = areatrainer
        print("area del trainer actualizada")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún trainer registrado.")

def grupo_del_trainer():
    global data
    doc = input("Ingrese el documento del trainer : ")
    if doc in data:
        grupotrainer = input("Ingrese el grupo del trainer: ")
        data[doc]["area del trainer"] = grupotrainer
        print("area del trainer actualizada")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún trainer registrado.")

        
def imprimir_documentos_y_nombres():
    global data
    print("Documentos y Nombres de Trainers:")
    for doc, trainer in data.items():
        print(f"Documento: {doc}, Nombre: {trainer['Nombre']}")