import dato_g

def campers_graduadoss ():
    graduadoo={}
    graduadoo["nombre"]=input("Ingrese el nombre del campers graduado para guardarlo en la base de tatos graduados")
    
    dato_g.data.append(graduadoo)
    dato_g.guardar_datos()
    


def mostrar_camper_graduados():
    print("Los campers graduados son: ")
    for graduadoo in dato_g.data:
        print("Los campers son:" , graduadoo["nombre"])