from flask import Flask, request, session, render_template, url_for, redirect, send_from_directory
from werkzeug import secure_filename
from os import urandom, listdir
from functools import wraps

app = Flask(__name__)
app.secret_key = urandom(24)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'username' in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('index.html', files=listdir('uploads/'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(request.args.get('next', url_for('index')))

    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/%s' % secure_filename(f.filename))
        return redirect(url_for('index'))
    else:
        return render_template('upload.html')

@app.route('/download/<filename>')
@login_required
def download(filename):
    return send_from_directory('uploads/', filename)

@app.context_processor
def inject_menu():
    return dict(menu={str.capitalize(page): url_for(page) for page in ['index', 'upload', 'logout']})

if __name__ == '__main__':
    app.run(debug=True)