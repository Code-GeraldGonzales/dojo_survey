from flask_app import app
from flask import render_template, request, redirect, session

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
    session['user_name'] = request.form['user_name']
    session['user_locations'] = request.form['user_locations']
    session['user_languages'] = request.form['user_languages']

    return redirect('/process')


@app.route('/process')
def success():
    if 'user_name' not in session or 'user_locations' not in session or 'user_languages' not in session:
        return redirect('/')
    return render_template("process.html")

@app.route('/back', methods=["POST"])
def reset_user():
    session.clear()
    return redirect('/')








#  return f"Name: {user_name} Age: {user_age} Email: {user_email}"


    # print(request.form['user_name'])
    # print(request.form['user_age'])
    # print(request.form['user_email'])