from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)