from flask import Flask, render_template, flash, request, url_for, redirect




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/conocenos')
def conocenos():
    return render_template('conocenos.html')

@app.route('/asociados')
def asociados():
    return render_template('asociados.html')

@app.route('/normatividad')
def normatividad():
    return render_template('normatividad.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

if __name__ == '__main__':
    app.run(debug=True)