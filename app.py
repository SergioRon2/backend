from flask import Flask, render_template, url_for
import numpy as np

app = Flask(__name__)

#  ruta original 

@app.route('/')
@app.route('/template.html')
def ruta1():
    titulo = 'Actividad Back-End'
    return render_template('template.html', titulo=titulo)

#  ruta notas 

@app.route('/notas.html')
@app.route('/notas.html/<float:nota1>/<float:nota2>/<float:nota3>')
def notas(nota1,nota2,nota3):
    tituloNotas = 'Ingresa las notas en la url de esta forma: /notas/(nota1)/(nota2)/(nota3)'

    proceso = (nota1*30)/100 + (nota2*30)/100 + (nota3*40)/100
    resultado = f'el promedio es: {proceso}'
    
    return render_template('notas.html', resultado=resultado, tituloNotas = tituloNotas)

#  esta es la ruta edad 

@app.route('/edad.html/<int:a>')
def edad(a):
    tituloEdad = 'Ingresa la edad en la url de esta forma: /edad/#'
    resultado = ''

    # todo lo que esta comentado es el intento de introducir imagenes

    if a == 0:
        resultado = ''
        # foto = ''
    elif a < 18:
        resultado = f'La persona es menor de edad, tiene {a} años'
        # foto = url_for('static', filename='static/img/menores.jpg')
    elif a < 60:
        resultado = f'La persona es adulta, pues tiene {a} años'
        # foto = url_for('static', filename='static/img/adulto.jpg')
    else:
        resultado = f'La persona es adulta mayor, tiene {a} años'
        # foto = url_for('static', filename='static/img/adulto-mayor.jpg')

    return render_template('edad.html', resultado=resultado, tituloEdad=tituloEdad)

    # foto = foto <-- esto va dentro de render_template 


#  esta es la ruta arreglos 

@app.route('/arreglos.html/<int:valores>/<int:columnas>/<int:filas>')
def arreglos(valores, columnas, filas):
    tituloArreglos = 'Ingresa los datos para el arreglo en la url de esta forma: /(valores)/(columnas)/(filas)'
    
    if filas == 0:
        arreglo = np.random.randint(valores, size=columnas)
    else:
        arreglo = np.random.randint(valores, size=(filas, columnas))

    resultado = f'El arreglo random es: {arreglo}'

    return render_template('arreglos.html', resultado=resultado, tituloEdad=tituloArreglos)


if __name__ == '__main__':
    app.run(debug=True)




