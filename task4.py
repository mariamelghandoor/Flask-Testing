# Create a Flask-based To-Do List
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


tasks = []



def get_tasks():
    return tasks
def add_task(task):
    tasks.append(task)
    return tasks

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task_route():
    task = request.form.get('task')
    
    if not task:
        return jsonify({"error": "No task provided"}), 400
    tasks = add_task(task)

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
