from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hey! I'm a test Flask application.<br />Try to add /hello/&lt;your name&gt; to the address line and see what happens"

@app.route('/hello/<username>')
def hello(username):
    return 'Hello %s!' % username

if __name__ == '__main__':
    app.run()