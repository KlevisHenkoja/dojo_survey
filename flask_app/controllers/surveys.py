from flask_app import app
from flask import render_template, redirect, request, session

@app.route('/')
def index():
    return render_template('dojoSurvey.html')

@app.route('/createSurvey', methods=['POST'])
def createSurvey():
    session['dojoCreated']= request.form
    session['name'] = request.form['name']
    data = {
        'name': request.form['name'],

    }
    createSurvey.save(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')