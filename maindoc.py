import csv
import matplotlib.pyplot as plt
import numpy as np
import pprint

def interface():
    print("""La siguiente es una estadística de las muertes ocasionadas en Estados Unidos por policías.""")
    while True:
        open_doc = open("shootings_wash_post.csv")
        read_doc = csv.reader(open_doc)
        main_data = list(read_doc)
        print()
        print("1. Datos de la Base de Datos.")
        print("2. Muertes por Estado.")
        print("3. Taza de Hombres vs. Mujeres.")
        print("4. Tipo de Arma Utilizada.")
        print("5. Edades.")
        print("6. Probabilidad de Morir según cierta edad (Monte-Carlo).")
        print("7. Salir.\n")
        seleccion_interface_main = int(input("Opción: "))
        if seleccion_interface_main == 1:
            pprint.pprint(main_data[0])
        elif seleccion_interface_main == 2:
            muertes_por_estado()
        elif seleccion_interface_main == 3:
            taza_hombres_mujeres()
        elif seleccion_interface_main == 4:
            tipo_de_arma()
        elif seleccion_interface_main == 5:
            edades_de_asesinados()
        elif seleccion_interface_main == 6:
            probabilidad_ser_asesinado()
        elif seleccion_interface_main == 7:
            break

def muertes_por_estado():
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)
    
    states = {}
    for i in range(1,5553):
        if main_data[i][9] in states.keys():
            states[main_data[i][9]] += 1
        else:
            states.setdefault(main_data[i][9],1)
    states_list_names = list(states.keys())
    states_list_values = list(states.values())

    f = plt.figure()
    f.set_figwidth(16)
    f.set_figheight(7)
    plt.bar(states.keys(),states.values(),color="hotpink")
    plt.title("Muertes Causadas por Policías por Estado",fontdict={"fontsize":20})
    plt.xlabel("Estado",fontdict={"fontsize":15})
    plt.ylabel("Muertes",fontdict={"fontsize":15})
    
    while True:
        print("1. Valores por Estado.")
        print("2. Histograma.")
        print("3. Salir.\n")
        seleccion_interface_edad = int(input("Opción: "))
        if seleccion_interface_edad == 1:
            pprint.pprint(states)
        elif seleccion_interface_edad == 2:
            plt.show()
        elif seleccion_interface_edad == 3:
            break


def taza_hombres_mujeres():
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)

    masculinos_y_femeninos = {"M":0,"F":0}
    for i in range(1,5553):
        if main_data[i][6] == "M":
            masculinos_y_femeninos["M"] += 1
        elif main_data[i][6] == "F":
            masculinos_y_femeninos["F"] += 1
    gente_total = masculinos_y_femeninos["M"] + masculinos_y_femeninos["F"]
    prevalencia_masculina = (masculinos_y_femeninos["M"]/gente_total)*100
    prevalencia_femenina = (masculinos_y_femeninos["F"]/gente_total)*100



    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(6)
    plt.pie([prevalencia_masculina,prevalencia_femenina],labels=["95.57%","4.43%"],labeldistance=0.5,colors=["#00b7ff","hotpink"])
    plt.title("Porcentaje de Hombres y Mujeres Asesinadas por Policías",fontdict={"fontsize":20})
    plt.legend(["Hombres","Mujeres"])
    

    while True:
        print("1. Porcentaje de Hombres vs. Mujeres Asesinados.")
        print("2. Diagrama de Pie")
        print("3. Salir.\n")

        seleccion_interface_sexo = int(input("Opción: "))
        if seleccion_interface_sexo == 1:
            print(f"Porcentaje hombres asesinados: {round(prevalencia_masculina,2)}%")
            print(f"Porcentaje mujeres asesinados: {round(prevalencia_femenina,2)}%\n")
        elif seleccion_interface_sexo == 2:
            plt.show()
        elif seleccion_interface_sexo == 3:
            break

def tipo_de_arma():
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)
    armas = {}
    for i in range(1,5553):
        if main_data[i][4] in armas.keys():
            armas[main_data[i][4]] += 1
        else:
            armas.setdefault(main_data[i][4],1)
    

    porcentaje_pistola = round((armas['gun']/(len(main_data)-1))*100,2)
    porcentaje_cuchillo = round((armas['knife']/(len(main_data)-1))*100,2)
    porcentaje_sin_arma = round((armas['unarmed']/(len(main_data)-1))*100,2)
    porcentaje_arma_juguete = round((armas['toy weapon']/(len(main_data)-1))*100,2)
    porcentaje_vehiculo = round((armas['vehicle']/(len(main_data)-1))*100,2)
    porcentaje_otros = round(100 - porcentaje_vehiculo - porcentaje_arma_juguete - porcentaje_sin_arma - porcentaje_cuchillo -porcentaje_pistola,2)

    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(6)
    datos_armas = [porcentaje_pistola,porcentaje_cuchillo,porcentaje_sin_arma,porcentaje_arma_juguete,porcentaje_vehiculo,porcentaje_otros]
    leyendas_armas_nombre = ["Pistola","Cuchillo","Sin Arma","Arma de Juguete","Vehículo","Otro"]
    leyendas_armas_porcentaje = []
    for i in datos_armas:
        leyendas_armas_porcentaje.append(str(i)+"%")
    plt.pie(datos_armas,labels=leyendas_armas_porcentaje)

    plt.title("Porcentaje de Tipo de Armas", fontdict={"fontsize":20})
    plt.legend(leyendas_armas_nombre,loc="center right",bbox_to_anchor=(1, 0, 0.5, 1))


    while True:
        print("1. Porcentaje de Utlización de Armas por los Asesinados.")
        print("2. Diagrama de Pie")
        print("3. Salir.\n")

        seleccion_interface_arma = int(input("Opción: "))
        if seleccion_interface_arma == 1:
            print("Porcentaje de Tipo de Armas:")
            print(f"Pistola: {porcentaje_pistola}%")
            print(f"Cuchillo: {porcentaje_cuchillo}%")
            print(f"Sin Arma: {porcentaje_sin_arma}%")
            print(f"Arma de Juguete: {porcentaje_arma_juguete}%")
            print(f"Vehículo: {porcentaje_vehiculo}%")
            print(f"Otro: {porcentaje_otros}%\n")
        elif seleccion_interface_arma == 2:
            plt.show()
        elif seleccion_interface_arma == 3:
            break



def mi_promedio(lista):
    promedio = 0
    for i in lista:
        promedio += i
    promedio /= len(lista)  
    return promedio

def mi_moda(lista):
    dict_moda = {}
    lista_moda = []
    for i in lista:
        if i in dict_moda.keys():
            dict_moda[i] += 1
        else:
            dict_moda.setdefault(i,1)

    for i in dict_moda.keys():
        if dict_moda[i] == mi_max(list(dict_moda.values())):
            lista_moda.append(i)
    lista_moda = set(lista_moda)
    lista_moda = list(lista_moda)

    if len(lista_moda) == 1:
        return lista_moda[0]
    else:
        return lista_moda


def mi_mediana(lista):
    if len(lista)%2 != 0:
        return lista[int(len(lista)/2 +1)-1]
    else:
        return (lista[int(len(lista)/2)-1] + lista[int(len(lista)/2)])/2

def mi_max(lista):
    lista.sort()
    return lista[-1]

def mi_min(lista):
    lista.sort(reverse = True)
    return lista[-1]

def mi_rango(lista):
    return mi_max(lista) - mi_min(lista)

def mi_varianza(lista):
    varianza = 0
    media = mi_promedio(lista)
    for i in lista:
        varianza += (i - media)**2
    varianza /= (len(lista) - 1)
    return varianza

def mi_desviacion(lista):
    desviacion = mi_varianza(lista)
    return desviacion**0.5



def edades_de_asesinados():
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)
    lista_edades = []
    for i in range(1,5553):
        if len(main_data[i][5]) > 0:
            lista_edades.append(int(main_data[i][5]))


    rangos_edad = {"0-9":0,"10-19":0,"20-29":0,"30-39":0,"40-49":0,"50-59":0,"60-69":0,"70-79":0,"80-89":0,"90-99":0,"100 o más":0}
    for i in range(1,5553):
        if len(main_data[i][5]) > 0:
            if int(main_data[i][5])<= 9:
                rangos_edad["0-9"] += 1
            elif int(main_data[i][5])>= 10 and int(main_data[i][5])<= 19:
                rangos_edad["10-19"] += 1
            elif int(main_data[i][5])>= 20 and int(main_data[i][5])<= 29:
                rangos_edad["20-29"] += 1
            elif int(main_data[i][5])>= 30 and int(main_data[i][5])<= 39:
                rangos_edad["30-39"] += 1
            elif int(main_data[i][5])>= 40 and int(main_data[i][5])<= 49:
                rangos_edad["40-49"] += 1
            elif int(main_data[i][5])>= 50 and int(main_data[i][5])<= 59:
                rangos_edad["50-59"] += 1
            elif int(main_data[i][5])>= 60 and int(main_data[i][5])<= 69:
                rangos_edad["60-69"] += 1
            elif int(main_data[i][5])>= 70 and int(main_data[i][5])<= 79:
                rangos_edad["70-79"] += 1
            elif int(main_data[i][5])>= 70 and int(main_data[i][5])<= 79:
                rangos_edad["70-79"] += 1
            elif int(main_data[i][5])>= 80 and int(main_data[i][5])<= 89:
                rangos_edad["80-89"] += 1
            elif int(main_data[i][5])>= 90 and int(main_data[i][5])<= 99:
                rangos_edad["90-99"] += 1
            else:
                rangos_edad["100 o más"] += 1

    f = plt.figure()
    f.set_figwidth(9)
    f.set_figheight(6)
    plt.bar(rangos_edad.keys(),rangos_edad.values())
        

    while True:
        print("1.  Media de Edades.")
        print("2.  Moda de Edades.")
        print("3.  Mediana de Edades.")
        print("4.  Edad Máxima.")
        print("5.  Edad Mínima.")
        print("6.  Rango.")
        print("7.  Varianza de Edades.")
        print("8.  Desviación Estándar de Edades.")
        print("9.  Histograma por Rango de Edad (10 años).")
        print("10. Salir.\n")

        seleccion_interface_edad = int(input("Opción: "))

        if seleccion_interface_edad == 1:
            print(f"Media: {round(mi_promedio(lista_edades),2)} años.\n")
        elif seleccion_interface_edad == 2:
            print(f"Edad o edades más comunes: {mi_moda(lista_edades)} años.\n")
        elif seleccion_interface_edad == 3:
            print(f"Mediana: {mi_mediana(lista_edades)} años.\n")
        elif seleccion_interface_edad == 4:
            print(f"Edad Máxima: {mi_max(lista_edades)} años.\n")
        elif seleccion_interface_edad == 5:
            print(f"Edad Mínima: {mi_min(lista_edades)} años.\n")
        elif seleccion_interface_edad == 6:
            print(f"Rango de Edades: {mi_rango(lista_edades)} años.\n")
        elif seleccion_interface_edad == 7:
            print(f"Varianza de Edades: {round(mi_varianza(lista_edades),2)} años.\n")
        elif seleccion_interface_edad == 8:
            print(f"Desvaición de Edades: {round(mi_desviacion(lista_edades),2)} años.\n")
        elif seleccion_interface_edad == 9:
            plt.show()
        elif seleccion_interface_edad == 10:
            break

def prob_age(media,desviacion,ptos,lim_inf,lim_sup):

    f = plt.figure()
    f.set_figwidth(9)
    f.set_figheight(6)
    x_bellcurve = np.linspace(media-50,media+50,10000)
    y_bellcurve = (np.exp(-((x_bellcurve - media)**2)/(2*desviacion**2)))/(np.sqrt(2*np.pi)*desviacion)


    plt.plot(x_bellcurve,y_bellcurve, color="black")
    plt.title("Función de Densidad de la Probabilidad Normal (Edades)",fontdict={"fontsize":20})

    x_mc_1 = np.random.uniform(lim_inf,lim_sup,[1,ptos])
    y_mc_1 = np.random.uniform(0,(1)/(np.sqrt(2*np.pi)*desviacion),[1,ptos])
    plt.scatter(x_mc_1,y_mc_1,color="#008bc7",marker=".")


    area_total = (lim_sup - lim_inf)*((1)/(np.sqrt(2*np.pi)*desviacion))

    pi_1 = 0
    for i in range(ptos):
        if (y_mc_1[0,i]) < (np.exp(-(((x_mc_1[0,i]) - media)**2)/(2*desviacion**2)))/(np.sqrt(2*np.pi)*desviacion):
            pi_1 += 1
    
    prob = f"P({round(lim_inf,1)}<Z<{round(lim_sup,1)})={round((pi_1/ptos)*area_total*100,2)}%"

    pops = {'ha': 'center', 'va': 'center', 'bbox': {'fc': 'hotpink', 'pad': 0.8,"boxstyle":"round"}}

    plt.text(media+30, 0.025, prob ,pops, rotation=0,)

    plt.grid()
    plt.show()


def probabilidad_ser_asesinado():
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)
    lista_edades = []
    for i in range(1,5553):
        if len(main_data[i][5]) > 0:
            lista_edades.append(int(main_data[i][5]))

    while True:
        print("1. Menor a cierta edad.")
        print("2. Mayor a cierta edad.")
        print("3. Entre  ciertas edades.")
        print("4. Salir.\n")

        seleccion_interface_prob_edad = int(input("Opción: "))

        if seleccion_interface_prob_edad == 1:
            edad_prob = int(input("Edad: "))
            ptos_monte_carlo = int(input("Puntos Simulación Monte-Carlo: "))
            prob_age(mi_promedio(lista_edades),mi_desviacion(lista_edades),ptos_monte_carlo,mi_promedio(lista_edades)-50,edad_prob)
        elif seleccion_interface_prob_edad == 2:
            edad_prob = int(input("Edad: "))
            ptos_monte_carlo = int(input("Puntos Simulación Monte-Carlo: "))
            prob_age(mi_promedio(lista_edades),mi_desviacion(lista_edades),ptos_monte_carlo,edad_prob,mi_promedio(lista_edades)+50)
        elif seleccion_interface_prob_edad == 3:
            print("La primera edad debe ser menor a la segunda.")
            edad_prob_1 = int(input("Edad 1: "))
            edad_prob_2 = int(input("Edad 2: "))
            while edad_prob_1 > edad_prob_2:
                print("ERROR: La primera edad debe ser menor a la segunda.")
                edad_prob_1 = int(input("Edad 1: "))
                edad_prob_2 = int(input("Edad 2: "))
            ptos_monte_carlo = int(input("Puntos Simulación Monte-Carlo: "))
            prob_age(mi_promedio(lista_edades),
                     mi_desviacion(lista_edades),
                     ptos_monte_carlo,
                     edad_prob_1,
                     edad_prob_2)

        elif seleccion_interface_prob_edad == 4:
            break


if __name__ == "__main__":
    interface()