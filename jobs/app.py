from flask import flask, render_template

app=flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')