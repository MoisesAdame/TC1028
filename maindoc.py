# Librerías importadas
import csv
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pprint

# Menú principal
def interface():
    # While loop, mantiene abierto el programa.
    while True:
        # Abriendo, leyendo y enlistando el documento csv.
        open_doc = open("shootings_wash_post.csv")
        read_doc = csv.reader(open_doc)
        main_data = list(read_doc)

        # Encabezado del Menú principal.
        print("_"*60,"\n")
        print("MUERTES CAUSADAS POR POLICÍAS EN ESTADOS UNIDOS")
        print("_"*60)

        # Opcionesde del menú principal.
        print("1. Datos de la Base de Datos.")
        print("2. Muertes por Estado.")
        print("3. Taza de Hombres vs. Mujeres.")
        print("4. Tipo de Arma Utilizada.")
        print("5. Edades.")
        print("6. Probabilidad de Morir según cierta edad (Monte-Carlo).")
        print("7. Salir.\n")

        # Selección de opción.
        seleccion_interface_main = int(input("Opción: "))

        # Opción 1, se muestra el encabezado de la tabla 1.
        if seleccion_interface_main == 1:
            print("_"*60,"\n")
            print("Datos de la Base de Datos".upper())
            print("_"*60)
            pprint.pprint(main_data[0])
        
        # Opción 2, se abre la función muertes por estado.
        elif seleccion_interface_main == 2:
            print("_"*60,"\n")
            print("Muertes por Estado".upper())
            print("_"*60)
            muertes_por_estado()
        
        # Opción 3, se abre la función taza hombres mujeres.
        elif seleccion_interface_main == 3:
            print("_"*60,"\n")
            print("Taza de Hombres vs. Mujeres".upper())
            print("_"*60)
            taza_hombres_mujeres()
        
        # Opción 4, se abre la función tipo de arma.
        elif seleccion_interface_main == 4:
            print("_"*60,"\n")
            print("Tipo de Arma Utilizada".upper())
            print("_"*60)
            tipo_de_arma()

        # Opción 5, se abre la función edades de asesinados.
        elif seleccion_interface_main == 5:
            print("_"*60,"\n")
            print("Edades".upper())
            print("_"*60)
            edades_de_asesinados()
        
        # Opción 6, se abre la función posibilidad de ser asesinado.
        elif seleccion_interface_main == 6:
            print("_"*60,"\n")
            print("Probabilidad de Morir según cierta edad (Monte-Carlo)".upper())
            print("_"*60)
            probabilidad_ser_asesinado()
        
        # Opción 7, se termina el programa y la while loop.
        elif seleccion_interface_main == 7:
            print("Hasta luego...")
            break

        else:
            print("Elige una opción válida.")

# Se define la función muertes por estado.
def muertes_por_estado():
    # Abriendo, leyendo y enlistando el documento csv.
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)
    
    # Diccionario que cuenta la cantidad de muertes por estado
    muertes_por_estado = {}
    for i in range(1,5553):
        # Si el estado ya está en keys, se le suma 1 al valor
        if main_data[i][9] in muertes_por_estado.keys():
            muertes_por_estado[main_data[i][9]] += 1
        
        # Si el estado no está en keys, se pone como valor inicial 1
        else:
            muertes_por_estado.setdefault(main_data[i][9],1)
    
    # Diagrama de Barras Estado vs. Catidad de muertes
    figura1_estado_cantidadmuertes = plt.figure()

    # Estableciendo el ancho y alto de la figura.
    figura1_estado_cantidadmuertes.set_figwidth(16)
    figura1_estado_cantidadmuertes.set_figheight(7)

    plt.bar(muertes_por_estado.keys(),muertes_por_estado.values(),color="hotpink")
    # Título de la figura 1
    plt.title("Muertes Causadas por Policías por Estado",fontdict={"fontsize":20})
    # Letrero eje x
    plt.xlabel("Estado",fontdict={"fontsize":15})
    # Letrero eje y
    plt.ylabel("Muertes",fontdict={"fontsize":15})
    
    # Menú Secundario: Muertes por estado
    # While loop, mantiene abierto el programa.
    while True:
        # Opciones
        print("1. Valores por Estado.")
        print("2. Histograma.")
        print("3. Salir.\n")

        # Selección de opción.
        seleccion_interface_edad = int(input("Opción: "))

        # Opción 1, se imprime el diccionario de las muertes por estado.
        if seleccion_interface_edad == 1:
            pprint.pprint(muertes_por_estado)
        
        # Opción 2, se muestra la figura1.
        elif seleccion_interface_edad == 2:
            plt.show()
        
        # Opción 3, se sale del Menú Secundario: Muertes por estado.
        # Se regresa al menú principal.
        elif seleccion_interface_edad == 3:
            break

        # Si no se elige una opción válida, se presenta el siguiente mensaje.
        else:
            print("Elige una opción válida.")

# Se define la función taza hombres mujeres.
def taza_hombres_mujeres():
    # Abriendo, leyendo y enlistando el documento csv.
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)

    # Se crea el diccionario de muertes "M" y "F", dejando el valor en 0.
    muertes_masculinos_y_femeninos = {"M":0,"F":0}

    for i in range(1,5553):
        # Con la foor loop si el csv es "M" se suma 1 a "M", 
        if main_data[i][6] == "M":
            muertes_masculinos_y_femeninos["M"] += 1
        
        # y si es "F", se le suma 1 a "F"
        elif main_data[i][6] == "F":
            muertes_masculinos_y_femeninos["F"] += 1
    
    # Se define la variable "gente total" que es la suma de "M"'s y "F"'s.
    gente_total = muertes_masculinos_y_femeninos["M"] + muertes_masculinos_y_femeninos["F"]

    # Usando la variable gente_total, obtenemos el porcentaje de "M" y "F" asesindados
    prevalencia_masculina = (muertes_masculinos_y_femeninos["M"]/gente_total)*100
    prevalencia_femenina = (muertes_masculinos_y_femeninos["F"]/gente_total)*100

    # Diagrama de Pie Taza Hombres vs. Mujeres
    figura2_diagrama_pie_sexo = plt.figure()

    # Estableciendo el ancho y alto de la figura.
    figura2_diagrama_pie_sexo.set_figwidth(10)
    figura2_diagrama_pie_sexo.set_figheight(6)

    plt.pie([prevalencia_masculina,prevalencia_femenina],#Porcentajes "M" vs "F".
            labels = ["95.57%","4.43%"],                 # Labels del diagrama de pie.
            labeldistance = 0.5,                         # Distancia de labels.
            colors = ["#00b7ff","hotpink"])              # Colores.
    
    # Título de figura2
    plt.title("Porcentaje de Hombres y Mujeres Asesinadas por Policías",
              fontdict={"fontsize":20})
    
    # Leyendas de diagrama de pie.
    plt.legend(["Hombres","Mujeres"])

    # Menú Secundario: Taza Hombres vs. Mujeres
    # While loop, mantiene abierto el programa.
    while True:
        # Opciones posibles.
        print("1. Porcentaje de Hombres vs. Mujeres Asesinados.")
        print("2. Diagrama de Pie")
        print("3. Salir.\n")

        # Selección de opción.
        seleccion_interface_sexo = int(input("Opción: "))

        # Si opción es 1, se imprimen los porcentajes.
        if seleccion_interface_sexo == 1:
            print(f"Porcentaje hombres asesinados: {round(prevalencia_masculina,2)}%")
            print(f"Porcentaje mujeres asesinados: {round(prevalencia_femenina,2)}%\n")
        
        # Si opción es 2, se muestra el diagrama de pie.
        elif seleccion_interface_sexo == 2:
            plt.show()

        # Si opción es 3, se sale del Menú Secundario.
        elif seleccion_interface_sexo == 3:
            break

        # Si no se elige una opción válida, se presenta el siguiente mensaje.
        else:
            print("Elige una opción válida.")

# Se define la función tipo de arma.
def tipo_de_arma():
    # Abriendo, leyendo y enlistando el documento csv.
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)

    # Se crea diccionario de los tipos de armas utlizadas
    armas = {}
    for i in range(1,5553):
        # Si el arma ya se registó, se le suma 1
        if main_data[i][4] in armas.keys():
            armas[main_data[i][4]] += 1
        
        # Si el arma no se ha registrado, se registra y se suma 1.
        else:
            armas.setdefault(main_data[i][4],1)

    # Se definen los porecntajes para los pirncipales tipos de armas usadas.
    porcentaje_pistola = round((armas['gun']/(len(main_data)-1))*100,2)
    porcentaje_cuchillo = round((armas['knife']/(len(main_data)-1))*100,2)
    porcentaje_sin_arma = round((armas['unarmed']/(len(main_data)-1))*100,2)
    porcentaje_arma_juguete = round((armas['toy weapon']/(len(main_data)-1))*100,2)
    porcentaje_vehiculo = round((armas['vehicle']/(len(main_data)-1))*100,2)
    porcentaje_otros = round(100 - porcentaje_vehiculo \
                                 - porcentaje_arma_juguete \
                                 - porcentaje_sin_arma \
                                 - porcentaje_cuchillo \
                                 -porcentaje_pistola,2)

    # Diagrama Pie Porcentaje de Armas más Utilizadas.
    figura3_diagrama_pie_armas = plt.figure()

    # Se define el ancho y largo de la figura3
    figura3_diagrama_pie_armas.set_figwidth(10)
    figura3_diagrama_pie_armas.set_figheight(6)

    # Se crea una lista de los porcentajes por arma.
    datos_armas = [porcentaje_pistola,
                   porcentaje_cuchillo,
                   porcentaje_sin_arma,
                   porcentaje_arma_juguete,
                   porcentaje_vehiculo,
                   porcentaje_otros]

    # Se crea una lista con las leyendas de los nombres de arma.
    leyendas_armas_nombre = ["Pistola","Cuchillo","Sin Arma","Arma de Juguete","Vehículo","Otro"]

    # Se crea una lista con las leyendas de los porcentajes de arma.
    leyendas_armas_porcentaje = []
    for i in datos_armas:
        leyendas_armas_porcentaje.append(str(i)+"%")

    # Se crea el diagrama de pie.
    plt.pie(datos_armas,labels=leyendas_armas_porcentaje)

    # Se establece el título del diagrama de pie
    plt.title("Porcentaje de Tipo de Armas", fontdict={"fontsize":20})

    # Se establecen el nombre de las armas con su respectiv vódigo de color.
    plt.legend(leyendas_armas_nombre,loc="center right",bbox_to_anchor=(1, 0, 0.5, 1))

    # Menú Secundario: Porcentaje de Uso de Armas.
    # While loop, mantiene abierto el programa.
    while True:
        # Posibles opciones
        print("1. Porcentaje de Utlización de Armas por los Asesinados.")
        print("2. Diagrama de Pie")
        print("3. Salir.\n")

        # Selección de la opción indicada.
        seleccion_interface_arma = int(input("Opción: "))

        # Si se elige la opción 1, se muestran los porcentajes de tipos
        # de armas utilizadas más frecuentes.
        if seleccion_interface_arma == 1:
            print("Porcentaje de Tipo de Armas:")
            print(f"Pistola: {porcentaje_pistola}%")
            print(f"Cuchillo: {porcentaje_cuchillo}%")
            print(f"Sin Arma: {porcentaje_sin_arma}%")
            print(f"Arma de Juguete: {porcentaje_arma_juguete}%")
            print(f"Vehículo: {porcentaje_vehiculo}%")
            print(f"Otro: {porcentaje_otros}%\n")
        
        # Si se elige la opción 2, se muestra el diegrama de pie.
        elif seleccion_interface_arma == 2:
            plt.show()
        
        # Si se sale la opción 3, se sale del Menú Secundario.
        elif seleccion_interface_arma == 3:
            break

        # Si no se elige una opción existente, se presenta el siguiente mensaje.
        else:
            print("Elige una opción válida.")

# Se define la función promedio, de una lista
def mi_promedio(lista):
    promedio = 0

    # Se suman todos los elementos de la lista
    for i in lista:
        promedio += i
    
    # Se divide promedio entre la cantidad de elementos de la lista
    promedio /= len(lista)  
    return promedio

# Se define la función moda, de una lista
def mi_moda(lista):
    # Se crea un diccionario para contar la cantidad de veces que se repite
    # un elemento de la lista.
    dict_moda = {}

    # Se crea una lista de los elementos más repetidos (moda)
    lista_moda = []

    for i in lista:
        # Si el elemento de la lista ya se registó, se le suma 1.
        if i in dict_moda.keys():
            dict_moda[i] += 1
        
        # Si el elemento no ha registrado, se le da por defaul el valor 1
        else:
            dict_moda.setdefault(i,1)

    # Para todos los valores en la lista, si al evaluar la key, se obtiene el
    # valor máximo de la lista de valores, se guarda en lista_moda la key que
    # coincidió.
    for i in dict_moda.keys():
        if dict_moda[i] == mi_max(list(dict_moda.values())):
            lista_moda.append(i)
    lista_moda = set(lista_moda)
    lista_moda = list(lista_moda)

    # Si en la moda solo hay un valor, se regresa solo ese valor
    if len(lista_moda) == 1:
        return lista_moda[0]

    # Si en la moda hay más de un valor, se regresa la lista con todos
    # los valores.
    else:
        return lista_moda

# Se define la función mediana, de una lista
def mi_mediana(lista):
    # Si la lista tiene una cantidad de elementos impar,
    # se regresa el valor de en medio de la lista.
    if len(lista)%2 != 0:
        return lista[int(len(lista)/2 +1)-1]
    
    # Si la lista tiene una cantidad de elementos par,
    # se regresa el promedio de los dos valores de en medio de la lista.
    else:
        return (lista[int(len(lista)/2)-1] + lista[int(len(lista)/2)])/2

# Se define la función max, de una lista
def mi_max(lista):
    # Se ordena de menor a mayor la lista.
    lista.sort()
    # Se regresa el último valor de la lista ordenada.
    return lista[-1]

# Se define la función min, de una lista
def mi_min(lista):
    # Se ordena de mayor a menor la lista.
    lista.sort(reverse = True)

    # Se regresa el último valor de la lista ordenada.
    return lista[-1]

# Se define la función rango, de una lista
def mi_rango(lista):
    # Se regresa la diferencia de el mayor y el menor elemento de la lista.
    return mi_max(lista) - mi_min(lista)

# Se define la función varianza, de una lista.
def mi_varianza(lista):
    # Se define la variable de varianza.
    varianza = 0

    # Se obtiene el promedio o media de la lista
    media = mi_promedio(lista)

    # Se suma para todos los elementos de la lista (x - µ)^2
    for i in lista:
        varianza += (i - media)**2
    
    # Se divide la suma entre todos los elementos menos 1.
    varianza /= (len(lista) - 1)
    return varianza

# Se define la función desviación, de una lista.
def mi_desviacion(lista):
    # Se iguala la desviacion a la varianza de la lista
    desviacion = mi_varianza(lista)

    # Se regresa la raíz cuadrada de la varianza. 
    return desviacion**0.5

# Se define la función edades de asesinados.
def edades_de_asesinados():
    # Se abre, lee y enlista el documento csv.
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)

    # Se define la lista todas las edades registradas en el documento
    lista_edades = []
    for i in range(1,5553):

        # Se añaden a la lista únicamente las edades que fueron registradas,
        # es decir, aquellas con una longitud mayor a 0. 
        if len(main_data[i][5]) > 0:
            lista_edades.append(int(main_data[i][5]))

    # Se define el diccionario rangos_edad, el cual, cuenta la cantidad
    # de personas que se encuentran entre un rango de edades de 10 años
    rangos_edad = {"0-9":0,"10-19":0,"20-29":0,"30-39":0,"40-49":0,"50-59":0,
                   "60-69":0,"70-79":0,"80-89":0,"90-99":0,"100 o más":0}

    # Mediante el siguiente for loop se cuenta la cantidad de personas en
    # cierto rango de edad.
    for i in lista_edades:
        if i <= 9:
            rangos_edad["0-9"] += 1
        elif i >= 10 and i <= 19:
            rangos_edad["10-19"] += 1
        elif i >= 20 and i <= 29:
            rangos_edad["20-29"] += 1
        elif i >= 30 and i <= 39:
            rangos_edad["30-39"] += 1
        elif i >= 40 and i <= 49:
            rangos_edad["40-49"] += 1
        elif i >= 50 and i <= 59:
            rangos_edad["50-59"] += 1
        elif i >= 60 and i <= 69:
            rangos_edad["60-69"] += 1
        elif i >= 70 and i <= 79:
            rangos_edad["70-79"] += 1
        elif i >= 70 and i <= 79:
            rangos_edad["70-79"] += 1
        elif i >= 80 and i <= 89:
            rangos_edad["80-89"] += 1
        elif i >= 90 and i <= 99:
            rangos_edad["90-99"] += 1
        else:
            rangos_edad["100 o más"] += 1

    # Diagrama de Barras de Rango de Edades
    figura4_diagrama_barras_edades = plt.figure()

    # Se define el ancho y largo de la figura4
    figura4_diagrama_barras_edades.set_figwidth(9)
    figura4_diagrama_barras_edades.set_figheight(6)

    # Se crea el diagrama de barras
    plt.bar(rangos_edad.keys(),rangos_edad.values(), color = "#a7ea99")

    # Se establece el título del diagrama de barras.
    plt.title("Personas Asesinadas Según un Rango de Edad", fontdict={"fontsize":20})

    # Título eje x
    plt.xlabel("Rango de Edad", fontdict={"fontsize":15})

    # Título eje y
    plt.ylabel("Cantidad Personas", fontdict={"fontsize":15})

    # Menú Secundario: Estadísticos de Edades.
    # While loop, mantiene abierta la función.
    while True:

        # Posibles opcines
        print("1.  Media de Edades.")
        print("2.  Moda de Edades.")
        print("3.  Mediana de Edades.")
        print("4.  Edad Máxima.")
        print("5.  Edad Mínima.")
        print("6.  Rango.")
        print("7.  Varianza de Edades.")
        print("8.  Desviación Estándar de Edades.")
        print("9.  Datos de Rangos de Edad.")
        print("10. Histograma por Rango de Edad (10 años).")
        print("11. Salir.\n")

        # Selector de opciones.
        seleccion_interface_edad = int(input("Opción: "))

        # Si se elige la opción 1, se muestra la media de edades.
        if seleccion_interface_edad == 1:
            print(f"Media: {round(mi_promedio(lista_edades),2)} años.\n")

        # Si se elige la opción 2, se muestra la moda de años.
        elif seleccion_interface_edad == 2:
            print(f"Edad o edades más comunes: {mi_moda(lista_edades)} años.\n")

        # Si se elige la opción 3, se muestra la mediana de la lista de edades
        elif seleccion_interface_edad == 3:
            print(f"Mediana: {mi_mediana(lista_edades)} años.\n")

        # Si seelige la opción 4, se muestra la edad máxima de la lista.
        elif seleccion_interface_edad == 4:
            print(f"Edad Máxima: {mi_max(lista_edades)} años.\n")
        
        # Si se elige la opción 5, se muestra la edad mínima de la lista.
        elif seleccion_interface_edad == 5:
            print(f"Edad Mínima: {mi_min(lista_edades)} años.\n")

        # Si se elige la opción 6, se muestra el rango de edades.
        elif seleccion_interface_edad == 6:
            print(f"Rango de Edades: {mi_rango(lista_edades)} años.\n")
        
        # Si se elige la opción 7, se muestra la varianza de las edades.
        elif seleccion_interface_edad == 7:
            print(f"Varianza de Edades: {round(mi_varianza(lista_edades),2)} años.\n")

        # Si se elige la opción 8, se muestra la desviación de edades.
        elif seleccion_interface_edad == 8:
            print(f"Desvaición de Edades: {round(mi_desviacion(lista_edades),2)} años.\n")
        
        # Si se elige la opción 9, se muestran los datos del 
        # diccionario rangos_edad 
        elif seleccion_interface_edad == 9:
            pprint.pprint(rangos_edad)
        
        # Si se elige la opción 10, se muestra el histograma de rangos de edad
        elif seleccion_interface_edad == 10:
            plt.show()
        
        # Si se elige la opción 11, se sale del Menú Secundario.
        elif seleccion_interface_edad == 11:
            break

        # Si se elige una opción no existente, se presenta el 
        # siguiente mensaje.
        else:
            print("Elige una opción válida.\n")

# Se define la función probabilidad_de_morir, la cual, con base em la media
# y la desviación estándar arrojadas por la base de datos, calcula la
# probabilidad de morir según un conjunto de edades asumiendo que las edades
# poseen una distribución normal.
def probabilidad_de_morir(media,desviacion,ptos,lim_inf,lim_sup):
    # Se define la figura5
    figura5_funcion_densidad_edades = plt.figure()

    # Se establece la relación ancho - largo de la figura
    figura5_funcion_densidad_edades.set_figwidth(9)
    figura5_funcion_densidad_edades.set_figheight(6)

    # Se definen las varibles dependiente e independiente para el plot de la
    # curva de gauss.
    x_bellcurve = np.linspace(media-50,media+50,10000)
    y_bellcurve = (np.exp(-((x_bellcurve - media)**2)/(2*desviacion**2)))/(np.sqrt(2*np.pi)*desviacion)

    # Se crea el plot de la curva de gauss.
    plt.plot(x_bellcurve,y_bellcurve, color="black")

    # Se establece el título de la figura5
    plt.title("Función de Densidad de la Probabilidad Normal (Edades)",fontdict={"fontsize":20})

    # SIMULACIÓN MONTE CARLO
    # Valores x y y de los puntos de la simulación Monte Carlo
    x_MonteCarlo = np.random.uniform(lim_inf,lim_sup,[1,ptos])
    y_MonteCarlo = np.random.uniform(0,(1)/(np.sqrt(2*np.pi)*desviacion),[1,ptos])

    # Se plottean los puntos dentro de la figura5
    plt.scatter(x_MonteCarlo,y_MonteCarlo,color="#b81616",marker=".")

    # Area Total de la superficie cubierta por los puntos
    area_total = (lim_sup - lim_inf)*((1)/(np.sqrt(2*np.pi)*desviacion))

    puntos_dentro = 0
    for i in range(ptos):
        # Se ceunta la cantidad de puntos que estan dento de la Curva de Gauss.
        if (y_MonteCarlo[0,i]) < (np.exp(-(((x_MonteCarlo[0,i]) - media)**2)/(2*desviacion**2)))/(np.sqrt(2*np.pi)*desviacion):
            puntos_dentro += 1
    
    # Se establece el texto que se mostrará en la caja de texto
    probabilidad_texto = f"P({round(lim_inf,1)}<Z<{round(lim_sup,1)})\
                          ={round((puntos_dentro/ptos)*area_total*100,2)}%"

    # Se establecen las propiedades de la caja de texto
    propiedades_caja_de_texto = {'ha': 'center', 'va': 'center', \
                                'bbox': {'fc': 'hotpink', 'pad': 0.8,"boxstyle":"round"}}

    # Se establece el texto que se mostrá en la figura 5
    plt.text(media+30, 0.025, probabilidad_texto ,propiedades_caja_de_texto, rotation=0,)

    plt.grid()
    plt.show()


def probabilidad_ser_asesinado():
    # Se abre, lee y enlista la información del documento csv.
    open_doc = open("shootings_wash_post.csv")
    read_doc = csv.reader(open_doc)
    main_data = list(read_doc)

    # Se define la lista de todas las edades de el documento csv.
    lista_edades = []
    for i in range(1,5553):
        if len(main_data[i][5]) > 0:
            lista_edades.append(int(main_data[i][5]))

    # Menú Secundario: Probabilidad de Ser Asesinado.
    # While loop, mantiene abierto el programa.
    while True:
        # Posibles opciones.
        print("1. Menor a cierta edad.")
        print("2. Mayor a cierta edad.")
        print("3. Entre  ciertas edades.")
        print("4. Salir.\n")

        # Selector de opción
        seleccion_interface_prob_edad = int(input("Opción: "))


        if seleccion_interface_prob_edad == 1:
            # Se pide edad y puntos de la simuclación
            edad_prob = int(input("Edad: "))
            ptos_monte_carlo = int(input("Puntos Simulación Monte-Carlo: "))

            # Se presenta el gráfico
            probabilidad_de_morir(mi_promedio(lista_edades),
                                       mi_desviacion(lista_edades),
                                       ptos_monte_carlo,
                                       mi_promedio(lista_edades)-50,
                                       edad_prob)

        elif seleccion_interface_prob_edad == 2:
            # Se pide edad y puntos de la simuclación
            edad_prob = int(input("Edad: "))
            ptos_monte_carlo = int(input("Puntos Simulación Monte-Carlo: "))

            # Se presenta el gráfico
            probabilidad_de_morir(mi_promedio(lista_edades),
                                       mi_desviacion(lista_edades),
                                       ptos_monte_carlo,edad_prob,
                                       mi_promedio(lista_edades)+50)
        
        elif seleccion_interface_prob_edad == 3:
            # Se pide edad y puntos de la simuclación
            print("La primera edad debe ser menor a la segunda.")
            edad_prob_1 = int(input("Edad 1: "))
            edad_prob_2 = int(input("Edad 2: "))

            # Si la edad 1 es mayor a la edad 2, se vuelven a pedir hasta
            # que se no se cumpla que la edad 1 es menor a la edad 2.
            while edad_prob_1 > edad_prob_2:
                print("ERROR: La primera edad debe ser menor a la segunda.")
                edad_prob_1 = int(input("Edad 1: "))
                edad_prob_2 = int(input("Edad 2: "))
            ptos_monte_carlo = int(input("Puntos Simulación Monte-Carlo: "))

            # Se presenta el gráfico
            probabilidad_de_morir(mi_promedio(lista_edades),
                                       mi_desviacion(lista_edades),
                                       ptos_monte_carlo,
                                       edad_prob_1,
                                       edad_prob_2)

        # Si la opción es 4, se sale del menú secudario.
        elif seleccion_interface_prob_edad == 4:
            break

        # Si no se elige una opción válida, se presenta el siguinete mensaje.
        else:
            print("Elige una opción válida.")


if __name__ == "__main__":
    interface()