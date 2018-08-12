
#w09c26

# More on Flask

In the last class, we ended with using Flasks render template. Flask uses the jinja template engine (you can find all you need about the template ending here http://jinja.pocoo.org/).

Flask is also built on werkzeug (http://werkzeug.pocoo.org/).

## The debug flag

When starting with debug, whenever we change our script - the serve will restart

When we run in debug mode, whenever there is an error, the web interface will display a full stack trace.

Also, we can put breakpoints in our code by simply add a "raise" command.

When we see a trace back output, we can hover over the right side of one of the lines and you can jump to python command line at that location of the code. The  "dump" command (which dumps all the variables at the current position in the code) can be useful here.

## Updating or example from last class

I made significant updates to the layout.html and main.css files from last class (there was at least one error, and also some crud, in the css file)

* improved formatting
* more flexible layout (for adding additional features)

__NOTE__: see http://jinja.pocoo.org/docs/2.9/templates/

If you're looking to test and experiment with different css layouts, you can save yourself allot time by working with one of the available online sites that help you develop css by giving you a real time view of your css results. For example, see http://www.cssdesk.com/64MKn to test out our css for this lecture.


### let's dig a big deeper into routing

I've created a new version of our flask demo site (flask.07.py).

This new version demonstrations
* __... how we can send and receive a variable, or information, from the URL call.__

```python
@app.route('/')
@app.route('/<name>')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)
```

* __... how we can read data from the URL and use this in our layout__

reading a var....

```python
@app.route('/')
@app.route('/<name>')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)
```

...and then using it in our layout

```html
{%extends "layout.html"%}
{%block content%}
<div class="home">
  <h1>{{ content }} Homepage</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```

* __how we can use filters to make sure we are converting our variable to the appropriate type__
```python
# set your about page here
@app.route('/add/<float:x>/<float:y>')
@app.route('/add/<float:x>/<int:y>')
@app.route('/add/<int:x>/<float:y>')
@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return render_template("add.html", content= '{} + {} = {}'.format(x, y, x+y))
```


* __how we can have multiple routines to a view (I was calling then handlers last class)__

```python
@app.route('/')
@app.route('/home')
@app.route('/home/<name>')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)
```

* __... how we can write python code to generate content that is named and sent to our template__

```python
@app.route('/weather/')
@app.route('/weather/<name>')  # be sure to include both forward slashes
def weather(name='Ames'):
    return render_template("weather.html", content='Current temp is {:3.1f}.'.format(get_temp()))
```

## more on cascading style sheets...

I've made significant updates to our layout and main.css files.

We won't cover CSS in any detail, but there are many good resources to be found on the internet.
http://flask.pocoo.org/docs/0.11/tutorial/css/

If you want to experiment with the css you see in this project, see here http://www.cssdesk.com/64MKn


## further look at...

If you're going to do any amount of development in Flask you'll need to dig deeper into Jinja to understand the details surrounding the rendering of html files. Specifically, how you can add/pass variables and custom code. I'd recommend your first step be to run through the tutorial found on the Flask website (http://flask.pocoo.org/docs/0.11/tutorial/introduction/)

Though we wont be covering this in this course, for a more complete view of what can be done with Flask, look at wtforms and how to create html forms. There's lot's of examples out there ... https://wtforms.readthedocs.io/en/latest/ , https://pythonspot.com/flask-web-forms/ etc.
