from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

"""@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['nm']
        return redirect(url_for('success', name=username))
    else:
        username = request.args.get('nm')
        return 'Upadhyay'"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
        if request.method == 'POST':
                user = request.form['nm']
                resp = make_response(render_template('readcookie.html'))
                resp.set_cookie('userID', user)
                return resp

@app.route('/getcookie')
def getcookie():
        name = request.cookies.get('userID')
        return '<h1> Hello ' + str(name) + '</h1>'

if __name__ == '__main__':
    app.run()
