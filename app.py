from flask import Flask, url_for, render_template, request, redirect
import random

app = Flask(__name__)

to_dos = [
    {
        'id': 1,
        'name': "Write My Composition",
        'checked': False,
    },
    {
        'id': 1,
        'name': "Take Out The Trash",
        'checked': True,
    },
]

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    for to_do in to_dos:
        if (request.method == "POST"):
            to_do_name = (request.form['to_do_name'])
            to_do['checked'] = not to_do['checked']
            break

    return render_template('index.html')

@app.route("/checked/<int:to_do_id>", methods=['GET', 'POST'])
def checked_to_do(to_do_id):
    for to_do in to_dos:
        if to_do['id'] == to_do_id:
            to_dos.remove(to_do)
            break
    return redirect(url_for('home'))

@app.route("/checked/<int:to_do_id>", methods=['GET', 'POST'])
def delete_to_do(to_do_id):
    global to_dos
    for to_do in to_dos:
        if to_do['id'] == to_do_id:
            to_dos.remove(to_do)
    return redirect(url_for('home'))