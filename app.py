from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():  # put application's code here
    return 'welcome to my first flask page'

@app.route("/About")
def about():
    return 'About page'

if __name__ == '__main__':
    app.run(debug = True)
