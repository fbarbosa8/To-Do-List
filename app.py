from flask import Flask, render_template, request, redirect

tarefas = []

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'home.html',
        titulo='Dashboard',
        descricao='Sistema simples de lista de tarefas usando Flask.'
    )


@app.route('/status')
def status():
    return {
        "status": "on"
    }


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        tarefa = request.form.get('tarefa')
        tarefas.append({
            'texto': tarefa,
            'concluida': False
        })
        print(tarefa)

    return render_template(
        'todo.html',
        titulo='To-Do List',
        tarefas=tarefas
    )


@app.route('/concluir/<int:index>', methods=['POST'])
def concluir(index):
    tarefas[index]['concluida'] = True
    return redirect('/todo')


@app.route('/excluir/<int:index>', methods=['POST'])
def excluir(index):
    try:
        tarefas.pop(index)
    except IndexError:
        pass
    return redirect('/todo')


if __name__ == '__main__':
    app.run(debug=True)
