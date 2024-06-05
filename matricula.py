import datas_mat

def matricula_camper ():
    matriculas={}
    print("Bienvenido a las matriculas de campus")
    print("aqui se encuentran los camper que lograron pasar la primera prueba ")
    matriculas["nom_matricula"]= input("nombre_del_camper")
    matriculas["Estado"]= "En proceso de inscricion"
    datas_mat.data.append(matriculas)
    datas_mat.guardar_datos()
    
def mostrar_camper_admitidos():
    print("Los Campers inscritos son:")
    for matriculas in datas_mat.data: 
        print("Camper que paso la prueba", matriculas["nom_matricula"], "En Estado" , matriculas ["Estado"])