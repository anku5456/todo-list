from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    elif request.method == 'GET':
        if request.args.get('delete'):
            task_to_delete = request.args.get('delete')
            tasks.remove(task_to_delete)
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
