from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('filename.html')

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('filename.html')

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)

