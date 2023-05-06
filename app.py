from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

todos = [
    {"task":"Task is Here", "done": True},
    ]


# Route To INDEX
@app.route('/', methods=['POST', 'GET'])
def Index():
    return render_template('index.html', todos=todos)


# Route To ADD NEW TASK
@app.route('/add', methods=['POST'])
def AddTask():
    if request.method == "POST":
        todos.append({'task': request.form['add_todo'], "done": False})
        return redirect(url_for('Index'))


# Route To DELETE TASK
@app.route('/del/<int:id>')
def DeleteTask(id):
    todos.pop(id)
    return redirect(url_for('Index'))


# Route To CHANGE TASK STATUS
@app.route('/status/<int:id>')
def DoneTask(id):
    task = todos[id]
    if task['done'] == True:
        task['done'] = False
    else:
        task['done'] = True
        
    return redirect(url_for('Index'))


# Route To EDIT TASK
@app.route('/edit/<int:id>', methods=['POST', "GET"])
def EditTask(id):
    task = todos[id]
    if request.method == "POST":
        task['task'] = request.form['add_todo']
        return redirect(url_for('Index'))

    return render_template('index.html', task=task, task_id=id)


if __name__ == "__main__":
    app.run(debug=True)