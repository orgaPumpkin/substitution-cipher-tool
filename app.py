from flask import Flask, render_template

app = Flask(__name__)

@app.get('/test/<name>')
def test(name):
    return render_template('test.html', name=name)

@app.get('/')
def root():
    return render_template('index.html')
