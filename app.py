from flask import Flask, render_template

app = Flask(__name__)

#  ruta original 

@app.route('/')
def ruta1():
    titulo = 'Actividad Back-End'
    return render_template('template.html', titulo=titulo)

#  esta es la ruta edad 

@app.route('/edad')
def info_edad():
    tituloEdad = 'Arriba escribe la edad, justo despues de: /edad/'
    return render_template('template.html', titulo=tituloEdad)

#  creamos la funcion para que funcione 

@app.route('/edad/<int:a>')
def edad(a):
    if a < 18:
        return f'<h1>La persona es menor de edad, tiene {a} años</h1>'
    elif a < 60:
        return f'<h1>La persona es adulta, pues tiene {a} años</h1>'
    else:
        return f'<h1>La persona es adulta mayor, tiene {a} años</h1>'

if __name__ == '__main__':
    app.run(debug=True)