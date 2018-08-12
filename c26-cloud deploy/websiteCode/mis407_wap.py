from flask import Flask, render_template
from weather import get_temp
import markdown as md
import csv

app = Flask(__name__)

WEB_APP_NAME="MIS407"

@app.route('/')
@app.route('/home')
@app.route('/home/<name>')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)

@app.route('/about/')
@app.route('/about/<name>')
def about(name=WEB_APP_NAME):
    return render_template("about.html", content=name)

@app.route('/contact/')
@app.route('/contact/<name>')
def contact(name=WEB_APP_NAME):
    return render_template("contact.html", content=name)

@app.route('/weather/')
@app.route('/weather/<name>')  
def weather(name='Ames'):
    return render_template("weather.html", content='Current temp is {:3.1f}.'.format(get_temp()))

# set your about page here
@app.route('/add/<float:x>/<float:y>')
@app.route('/add/<float:x>/<int:y>')
@app.route('/add/<int:x>/<float:y>')
@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return render_template("add.html", content= '{} + {} = {}'.format(x, y, x+y))

# set your about page here
@app.route('/markdown/')
def markdown():
    with open("README.md", 'r') as fin:
        content_md = fin.read().strip()
    return render_template("markdown.html", content=md.markdown(content_md))

# set your about page here
@app.route('/table/')
def table():
    dict = {"Apples": 10, "Pears": 34, "Oranges":19}
    return render_template("table.html", content=dict)

# set your about page here
@app.route('/read_csv/')
def read_csv():
    with open('test.csv') as inFile:
        data  = list(csv.reader(inFile))
    return render_template("read_csv.html", content=data)

# run the Flask app (which will launch a local webserver)
if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=8080, debug=True)
