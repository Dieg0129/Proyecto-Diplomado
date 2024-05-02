from flask import Flask, render_template, request, url_for, redirect
import numpy as np


app= Flask(__name__) #Se inicializa la aplicación


@app.route('/')
def index():
    #return "Hola" 
    
    data ={
        'titulo': 'Formulario ICFES',
        'bienvenida': 'Ingresa tus resultados en las Pruebas Saber 11',
    }
    return render_template('index.html', data = data) #Retornar una plantilla html

@app.route('/index2')
def index2():
    #return "Hola" 

    return render_template('index2.html') #Retornar una plantilla html


############################################################################

@app.route('/promedio', methods=['POST'])
def promedio():
    # Obtener los datos enviados por el formulario
    formulario1 = float(request.form['formulario1'])
    formulario2 = float(request.form['formulario2'])
    formulario3 = float(request.form['formulario3'])
    formulario4 = float(request.form['formulario4'])
    formulario5 = float(request.form['formulario5'])
    formulario6 = float(request.form['formulario6'])

    # Inicializar result_soc con un valor predeterminado

    if formulario6 >= 347.60 or formulario6 >= 296.72:
        result_glo = "Con respecto a sus resultados, se encuentra en un nivel SUPERIOR"
        percentil_nivel = percentiles_cluster0(formulario6) 

        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)

    elif formulario6 >= 293.53 or formulario6 >= 264.66:
        result_glo = "Con respecto a sus resultados, se encuentra en un nivel ALTO"
        percentil_nivel = percentiles_cluster2(formulario6)

        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)
    elif formulario6 >= 261.62 or formulario6 >= 227.69:
        result_glo = "Con respecto a sus resultados, se encuentra en un nivel MEDIO"
        percentil_nivel = percentiles_cluster1(formulario6)

        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)
    elif formulario6 >= 225.26 or formulario6 >= 184.5:
        result_glo = "Con respecto a sus resultados, se encuentra en un nivel BAJO"
        percentil_nivel = percentiles_cluster3(formulario6)

        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)

    else:
        result_glo = "Con respecto a sus resultados, se encuentra en un nivel BAJO"
        percentil_nivel = percentiles_cluster3(formulario6)
        #Resultados en sociales
        result_soc = determinar_nivel_social(formulario1)
        #Resultados en matematicas
        result_mat = determinar_nivel_matematicas(formulario2)
        #Resultados en Lectura Critica
        result_LectC= determinar_nivel_LectCri(formulario3)
        #Resultados en Ingles
        result_Ing=determinar_nivel_Ingles(formulario4)
        #Resultados en Ciencias Naturales
        result_CN=determinar_nivel_CNatura(formulario5)


    # Retornar el resultado a la plantilla HTML
    return render_template('resultado.html',resultado_percentil=percentil_nivel, resultado=result_glo, resultado2=result_soc, resultado3=result_mat, resultado4=result_LectC, resultado5=result_Ing, resultado6=result_CN, formulario1=formulario1, 
                           formulario2=formulario2, formulario3=formulario3, formulario4=formulario4, formulario5=formulario5, formulario6=formulario6)

#FUNCIONES#####

def determinar_nivel_social(puntajeSoc):
        if puntajeSoc >= 66.73 or puntajeSoc >= 56.69:
            return "Con respecto a sus resultados, se encuentra en un nivel SUPERIOR"
        elif puntajeSoc >= 63 or puntajeSoc >= 43:
            return "Con respecto a sus resultados, se encuentra en un nivel ALTO"
        elif puntajeSoc >= 51.45 or puntajeSoc >= 39.5:
            return "Con respecto a sus resultados, se encuentra en un nivel MEDIO"
        elif puntajeSoc >= 46.5 or puntajeSoc >= 32:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO"
        else:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO"
        
def determinar_nivel_matematicas(puntajeMat):
        
        if puntajeMat >= 71.57 or puntajeMat >= 57:
            return "Con respecto a sus resultados, se encuentra en un nivel SUPERIOR"
        elif puntajeMat >= 60 or puntajeMat >= 54.25:
            return "Con respecto a sus resultados, se encuentra en un nivel ALTO"
        elif puntajeMat >= 57 or puntajeMat >= 45:
            return "Con respecto a sus resultados, se encuentra en un nivel MEDIO"
        elif puntajeMat >= 49 or puntajeMat >= 34.83:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO"
        else:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO"

def determinar_nivel_LectCri(puntajeLect):
        if puntajeLect >= 71.05 or puntajeLect >= 53:
            return "Con respecto a sus resultados, se encuentra en un nivel SUPERIOR"
        elif puntajeLect >= 61.5 or puntajeLect >= 50:
            return "Con respecto a sus resultados, se encuentra en un nivel ALTO "
        elif puntajeLect >= 59 or puntajeLect >= 44:
            return "Con respecto a sus resultados, se encuentra en un nivel MEDIO "
        elif puntajeLect >= 54 or puntajeLect >= 31:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO "
        else:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO "

def determinar_nivel_Ingles(puntajeIngl):
        if puntajeIngl >= 79 or puntajeIngl >= 59.69:
            return "Con respecto a sus resultados, se encuentra en un nivel SUPERIOR "
        elif puntajeIngl >= 62.63 or puntajeIngl >= 44:
            return "Con respecto a sus resultados, se encuentra en un nivel ALTO "
        elif puntajeIngl >= 58 or puntajeIngl >= 39:
            return "Con respecto a sus resultados, se encuentra en un nivel MEDIO "
        elif puntajeIngl >= 49 or puntajeIngl >= 32:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO "
        else:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO "

def determinar_nivel_CNatura(puntajeNatu):
        if puntajeNatu >= 69 or puntajeNatu >= 57:
            return "Con respecto a sus resultados, se encuentra en un nivel SUPERIOR "
        elif puntajeNatu >= 58 or puntajeNatu >= 48.83:
            return "Con respecto a sus resultados, se encuentra en un nivel ALTO "
        elif puntajeNatu >= 60 or puntajeNatu >= 39:
            return "Con respecto a sus resultados, se encuentra en un nivel MEDIO "
        elif puntajeNatu >= 47 or puntajeNatu >= 36:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO "
        else:
            return "Con respecto a sus resultados, se encuentra en un nivel BAJO "

def percentiles_cluster0(percentil0):
    puntajes_Calcular = [308, 302, 296.7238095, 303, 308, 304.4375, 315, 298.8560606,
                         312.2903226, 310.7583893, 321.8676471, 318.92, 343, 317, 347.6031746]

    percentiles = np.percentile(puntajes_Calcular, [0, 25, 50, 75, 100])

    def determinar_percentil(dato, percentiles):
        if dato < percentiles[1]:
            return "Su puntaje está por debajo del 25º del percentil de los evaluados"
        elif dato < percentiles[2]:
            return "Su puntaje está en el 25º al 50º del percentil de los evaluados"
        elif dato < percentiles[3]:
            return "Su puntaje está en el 50º al 75º del percentil de los evaluados"
        else:
            return "Su puntaje está por encima del 75º del percentil de los evaluados"

    resultado_p0 = determinar_percentil(percentil0, percentiles)
    return resultado_p0

def percentiles_cluster2(percentil2):
    puntajes_Calcular = [264.6666667, 273.0352113, 277.4444444, 267.2803738, 281.5, 274.8644068,
         274.3986486, 276.0819113, 272.9918699, 266.6666667, 274.4509804,
         286.7142857, 281.4246032, 278, 284.2088608, 290.0172414, 277, 282.75,
         268, 285.9677419, 293.5326087, 282, 276]

    percentiles = np.percentile(puntajes_Calcular, [0, 25, 50, 75, 100])

    def determinar_percentil(dato, percentiles):
        if dato < percentiles[1]:
            return "Su puntaje está por debajo del 25º del percentil de los evaluados"
        elif dato < percentiles[2]:
            return "Su puntaje está en el 25º al 50º del percentil de los evaluados"
        elif dato < percentiles[3]:
            return "Su puntaje está en el 50º al 75º del percentil de los evaluados"
        else:
            return "Su puntaje está por encima del 75º del percentil de los evaluados"

    resultado_p2 = determinar_percentil(percentil2, percentiles)
    return resultado_p2

def percentiles_cluster1(percentil1):
    puntajes_Calcular = [253, 240, 232.4736842, 234.0540541, 227.6923077, 231.125, 228.0833333,
         232.3513514, 236.8421053, 240, 241.6666667, 241.3333333, 237.5384615,
         243.875, 239.952381, 238.3469388, 235.2612613, 240.5925926, 233.3684211,
         240.1176471, 246.3737374, 245.12, 248.3793103, 241.0344828, 247.7391304,
         250.1111111, 243.0869565, 249.4027778, 253.9285714, 249.9365079, 243.7142857,
         233, 258.3181818, 260.6206897, 255.1390728, 247.3333333, 252.2857143,
         247.05, 255.3846154, 252.5955882, 246.483871, 251.4, 258.4823529, 259.5967742,
         261.627451, 245.1818182, 255.1538462, 257]

    percentiles = np.percentile(puntajes_Calcular, [0, 25, 50, 75, 100])

    def determinar_percentil(dato, percentiles):
        if dato < percentiles[1]:
            return "Su puntaje está por debajo del 25º del percentil de los evaluados"
        elif dato < percentiles[2]:
            return "Su puntaje está en el 25º al 50º del percentil de los evaluados"
        elif dato < percentiles[3]:
            return "Su puntaje está en el 50º al 75º del percentil de los evaluados"
        else:
            return "Su puntaje está por encima del 75º del percentil de los evaluados"

    resultado_p1 = determinar_percentil(percentil1, percentiles)
    return resultado_p1

def percentiles_cluster3(percentil3):
    puntajes_Calcular = [208, 195, 215.5, 193, 225.2666667, 184.5, 222.4210526, 218, 217, 187, 214]

    percentiles = np.percentile(puntajes_Calcular, [0, 25, 50, 75, 100])

    def determinar_percentil(dato, percentiles):
        if dato < percentiles[1]:
            return "Su puntaje está por debajo del 25º del percentil de los evaluados"
        elif dato < percentiles[2]:
            return "Su puntaje está en el 25º al 50º del percentil de los evaluados"
        elif dato < percentiles[3]:
            return "Su puntaje está en el 50º al 75º del percentil de los evaluados"
        else:
            return "Su puntaje está por encima del 75º del percentil de los evaluados"

    resultado_p3 = determinar_percentil(percentil3, percentiles)
    return resultado_p3

#FUNCIÓN PÁGINA NO ENCONTRADA#
def pagina_no_encontrada(error):
    return redirect(url_for('index')) #Redirecciona a otra pagina

#FINAL FUNCIONES##################################
    

if __name__ == '__main__': #Si esta desde el main, entonces se corre el pograma
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)