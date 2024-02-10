from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World2!'

@app.route('/contact')
def contact():  # put application's code here
    return 'Contact page'


if __name__ == '__main__':
    app.run()
