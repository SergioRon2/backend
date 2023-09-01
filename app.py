from flask import Flask, render_template

app = Flask(__name__)

#  ruta original 

@app.route('/')
def ruta1():
    titulo = 'Actividad Back-End'
    return render_template('template.html', titulo=titulo)

#  ruta notas 

@app.route('/notas/<float:nota1>/<float:nota2>/<float:nota3>')
def notas(nota1,nota2,nota3):
    resultado = (nota1*30)/100 + (nota2*30)/100 + (nota3*40)/100
    return f'el promedio es: {resultado}'
    return render_template('notas.html', resultado=resultado)

#  esta es la ruta edad 

@app.route('/edad/<int:a>')
def edad(a):
    tituloEdad = 'Ingresa la edad en la url de esta forma: /edad/#'
    if a < 18:
        return f'<h1>La persona es menor de edad, tiene {a} años</h1>'
    elif a < 60:
        return f'<h1>La persona es adulta, pues tiene {a} años</h1>'
    else:
        return f'<h1>La persona es adulta mayor, tiene {a} años</h1>'
        return render_template('edad.html', tituloEdad=tituloEdad)

if __name__ == '__main__':
    app.run(debug=True)




    