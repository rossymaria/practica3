from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los inscritos
inscritos = []

@app.route("/")
def lista_inscritos():
    return render_template('index.html', inscritos=inscritos)

@app.route("/nuevo", methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        turno = request.form['turno']
        seminarios = request.form.getlist('seminarios')

        nuevo_inscrito = {
            'id': len(inscritos) + 1,  
            'fecha': fecha,
            'nombre': nombre,
            'apellidos': apellidos,
            'turno': turno,
            'seminarios': ', '.join(seminarios)  
        }

        inscritos.append(nuevo_inscrito)
        return redirect(url_for('lista_inscritos'))

    return render_template('nuevo.html')

@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    inscrito = next((i for i in inscritos if i['id'] == id), None)

    if request.method == 'POST':
        if inscrito:
            inscrito['fecha'] = request.form['fecha']
            inscrito['nombre'] = request.form['nombre']
            inscrito['apellidos'] = request.form['apellidos']
            inscrito['turno'] = request.form['turno']
            inscrito['seminarios'] = ', '.join(request.form.getlist('seminarios'))
        return redirect(url_for('lista_inscritos'))

    return render_template('editar.html', inscrito=inscrito)

@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    global inscritos
    inscritos = [i for i in inscritos if i['id'] != id]
    return redirect(url_for('lista_inscritos'))

if __name__ == "__main__":
    app.run(debug=True)