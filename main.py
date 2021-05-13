from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/data/<username>')
def getdata(username):
    ...

@app.route('/user')
def user():
    ...

app.run()