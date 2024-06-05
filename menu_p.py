import datas
import data_t
import prime
import ruta_en
import camper_g
import matricula

def menu_principal():
    print("")
    print("||  ｡☆✼★━━━━━━━━━━━━★✼☆｡   ||")
    print("|| Bienvenido a campusland ||")
    print("||  ｡☆✼★━━━━━━━━━━━━★✼☆｡   ||")
    while True:
        print("ingres su rol\n 1. coordinador:\n 2. trainer:\n 3.camper:\n 4.Salir:")
        rol = 0
        try:
            rol = int(input("Ingrese la opción de su rol: "))
        except Exception:
            print("Valor incorrecto!!")            
        if rol == 1:
            print("----------------------------------------------")
            prime.letrero1()
            print("1. trainers\n 2.campers \n 3.Rutas de entrenamiento\n 4. Reportes \n 5. Salir")
            opcion=int(input("ingrese la opcion que desea realizar: "))
            if opcion == 1:
                print("1. registar trainer\n 2. modificar trainer")
                opct=int(input("ingrese la opcion a realizar: "))
                if opct == 1:
                    data_t.cargar_datos()
                    data_t.registrar_trainer()
                elif opct ==2:
                    data_t.cargar_datos()
                    print("Que opccion desea modificar del trainer:\n 1. horario\n 2. area de entrenamiento\n 3.agregar grupo al trainer\n 4. Mostrar Trainers\n 5. Salir")
                    
                    opctm=int(input("ingrese la opcion que desea modificar: "))
                    if opctm ==1:
                        data_t.cargar_datos()
                        data_t.imprimir_documentos_y_nombres()
                        data_t.horario_del_trainer()
                    elif opctm ==2:
                        data_t.cargar_datos()
                        data_t.area_del_trainer()
                        data_t.imprimir_documentos_y_nombres()
                    elif opctm == 3:
                        data_t.cargar_datos()
                        data_t.grupo_del_trainer()
                        data_t.imprimir_documentos_y_nombres()
                    elif opctm == 4:
                        data_t.imprimir_documentos_y_nombres()
                    elif opctm == 5:
                        print("")

            elif opcion==2:
                print("-------------------------------------------")
                print("1. registrar camper \n 2.modificar camper \n 3.Matricula")
                opcc=int(input("ingrese la opcion a la que desea acceder: "))
                if opcc == 1:
                    print("-------------------------------------------")
                    datas.cargar_datos()
                    datas.registrar_camper()
                elif opcc == 2: 
                    print("-------------------------------------------")
                    print("1.estado del camper\n 2.riesgo \n 3.ruta\n 4. eliminar camper\n 5.asignar grupo al camper ")
                    opccm=int(input("ingrese a la opcion del camper que desea modificar: "))
                    if opccm == 1:
                        print("-------------------------------------------")
                        datas.imprimir_camper_info()
                        datas.cargar_datos()
                        datas.estado_camper()
                    elif opccm == 2:
                        print("-------------------------------------------")
                        datas.imprimir_camper_info()
                        datas.cargar_datos()
                        datas.riesgo_camper()
                    elif opccm == 3:
                        print("-------------------------------------------")
                        datas.imprimir_camper_info()
                        print("rutas:\n nodaJS\n java\n javaScript")
                        datas.cargar_datos()
                        datas.ruta_camper()
                    elif opccm == 4:
                        print("-------------------------------------------")
                        datas.imprimir_camper_info()
                        datas.cargar_datos()
                        datas.eliminar_camper()
                    elif opccm == 5:
                        print("-------------------------------------------")
                        datas.imprimir_camper_info()
                        datas.cargar_datos()
                        datas.grupo_camper()

                elif opcc == 3:
                    print("-------------------------------------------")
                    matricula.matricula_camper()
            elif opcion == 3:
                print("------------------------------------------")
                print("Binevenido a Rutas de entrenamineto")
                print("\n1. Crear Nueva Ruta \n2. Mostrar Rutas \n3.Salir al menu Principal")
                oppc= int(input())
                if oppc == 1:
                    print("-------------------------------------------")
                    ruta_en.ruta_entreno()
                elif oppc == 2:
                    print("-------------------------------------------")
                    ruta_en.mostrar_rutas()
                elif oppc == 3:
                    print("-------------------------------------------")
                    print("")

            elif opcion == 4 :
                print("----------------------------------")
                print("Bienvenido a reportes")
                print("Que desea hacer ")
                print("\n1.Mostrar campers que estan Inscritos\n2.Campers que pasaron el examen inicial\n3. Entrenadores que se encuentran trabajando con CampusLands\n4. Campers que se encuentran con bajo rendimiento\n5.Campers y los trainer que se encuentren asociados a una ruta de entrenamiento\n6.Ingresar un nuevo camper graduado\n7.Mostrar campers graduados \n8.volver al menu anterior")
                opcrprte= int(input("Ingreseuna opcion"))
                if opcrprte == 1:
                    print("-------------------------------------------")
                    datas.imprimir_camper_info()
                elif opcrprte == 2:
                    print("-------------------------------------------")
                    matricula.mostrar_camper_admitidos()
                elif opcrprte == 3:
                    print("-------------------------------------------")
                    data_t.imprimir_documentos_y_nombres()
                elif opcrprte == 6:
                    print("-------------------------------------------")
                    camper_g.campers_graduadoss()
                elif opcrprte == 7:
                    print("-------------------------------------------")
                    camper_g.mostrar_camper_graduados()


               


        elif rol == 2:
            print("--------------------------------------------------")
            print("1.dar notas a un camper\n 2.mostar grupo\n 3.salir")
            prime.letrero2()
            opctn= int(input("ingrese la opcion que desea realizar"))    
            if opctn == 1:
                print("-------------------------------------------")
                datas.imprimir_camper_info()
                datas.cargar_datos()
                datas.nota_camper()
            elif opctn == 3:
                print("-------------------------------------------")
                print ("saliendo")

        elif rol == 3:
            print("---------------------------------------------")
            print("1. ver notas\n 2. salir")
            opci=int(input())
            datas.cargar_datos()
            datas.imprimir_nota_camper()
        elif rol == 4:
            print("-------------------------------------------")
            print("-------------------")
            print("  Usted ha salido ")
            print("-------------------")

            break


print(menu_principal())