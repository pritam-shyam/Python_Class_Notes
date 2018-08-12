# w09c26

# Cloud based App deployment

Cloud based computing has become a key method of deployment of many enterprise applications.

Organizations are increasingly leveraging cloud services and technology to help reduce the excessive capital outlays that typically accompany the installation an use of enterprise systems. It also greatly reduces the burden of ongoing maintenance of the supporting infrastructure.


## Technology options

Though there are many ways to deploy apps "in the cloud", we will focus primarily on the creation of Web based apps as "front ends" that allow  applications to be deployed using hosted web application services such as Heroku and Amazon Web Services.

## Web App Development in Python

How do we develop Web apps in Python?

Though you could always develop your own set of class and methods, it's probably best to build off what others have done. There are many python web 'frameworks' available. These frameworks include many of the basic functions you'll need to write any web based application (see: https://wiki.python.org/moin/WebFrameworks). Some of the most popular python web frameworks include Django and Flask. We will be using Flask (for a recent comparison look  [here](https://www.airpair.com/python/posts/django-flask-pyramid).)

Flask is what is called a "micro framework". It works well, and of quite flexible. Many companies use this framework. Django is another - it's considered a larger and/or higher level framework, and has a steeper learning curve that Flask. For this course, we will use Flask. If you want to get serious with web development --- learn javascipt (and related, AngularJS) for "front end", and django for "back end". SQLight can be used for websites, but it requires a persistent file system -- and this can be problematic on certain cloud based platforms (such as Heroku), so you may also need to look at PostGress, MySQL (or more proprietary systems such as Oracle and MS SQL server)

## Service options

For this course, I'll post a tutual about how we  can deploy our applications to "the cloud" using a popular cloud based platform -  Heroku (they have a free version that you will need to sign up for, and will be sufficient for our needs). Heroku is one of many examples of of PaaS (Platform as a service) provider (for a recent comparison look [here](https://www.g2crowd.com/categories/platform-as-a-service-paas))  

__NOTE:__ To build and deploy cloud based python web applications, you will first need to create a web application on our local machine.  In this class, we'll discuss how we do this using Flask

__NOTE2:__ Do the limited time we have in this course, I cannot cover all databases. SQLite a "nice primer", but if you plan to do some serious DB coding, look at the library SQLAlchemy. This can be used as a nice library to work with SQLite (which we'll typically use for "in memory" databases) and PostGres/MySQL/Oracle, etc.

# Basic Web Site Architecture technology

In case you're not already familiar (or need a refresher) we'll need to begin by introducing your to  general Web Architecture.

NOTE: I will speak to this more than you see written here. If you're not familiar with Web Architecture, you may want to take notes, and do some  further on the basics online.

The 'internet' exists because of non-proprietary protocols. Protocols serve as the linga franca that allow disparate systems to "talk" a common language.

![OSI ad TCP models](./images/network_layer_models.png)

(discuss the above network models)

At the _web application layer_ - HTTP servers listen to HTTP requests from HTML Browsers and respond with appropriate Web page content. HTML (the Hypertext Markup Language) and CSS (Cascading Style Sheets) are two of the core technologies used for Web page content. These standards (CSS and HTML) are not networking standards, but rather standard for how information is coded and displayed -- and which it interpreted and "rendered" by HTML browsers. HTML provides the structure of the page, CSS the (visual and aural) layout, for a variety of devices.

Once a HTTP server response to a request (from an HTML Client, or as we've see -- our own python programs), the data is transported using HTTP (or HTTPS if it's encrypted). Once the content is received by a web browser client, the HTML/CSS content is rendered and displayed. But, this data could also be encoded in other formats -- as we have seen when using our API calls (which were using HTTP as the protocol, but the data wasn't meant to be "rendered" directory by a browser, rather interpreted and read by another program). Now, wrt to display of "web content", the loading of a "page" often involves many transactions between the web client and the HTTP server -- as images, and other resources, are needed before the page can be fully rendered. This exchange of information can also continue during as the display of a page, as new content is updated.

Web page content can either be "static" or "dynamic". Static content is stored as files on the web server. Dynamic content is produced by software/code on the webserver. There are many, many, options for creating dynamic websites (we'll be using Python, obviously). Web clients can also be dynamic and accept code (Javascript is standard) from the HTTP server that programmatically responds to user requests in a more dynamic fashion.

For our Python Cloud deployment, our Python code will create content that will be "served" via HTTP to the requesting Web Client (HTML Browser).

# Building websites with Flask

Since our app will interact with users via the Web, we'll need to include a web development framework in our development process. For this project we'll use Flask.

## Your "Hello World" Flask server

First, you'll need to install Flask.

```
pip install flask
```

Now, we can use Python to create a local Web Application. Let's start with a simple "Hello World" app.

```python

from flask import Flask

# Create a flask application object and provide a variable name , in this case "app"
# The name given provided in the Flask initialization  is used to resolve resources
# from inside the package. Unless you are using flask within a custom package you'
# re creating, simply put __name__ here.
app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return "Hello world!"

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```
[^flask01.py^](./flask01.py)

From the command prompt start our program flask01.py and point your browser to http://127.0.0.1:8080 to see the results.


* Host: This is the local IP address that you wish the server to run on. Host 0.0.0.0 is local host. NOTE: Have you seen 127.0.0.1 (often called "loopback") used before? 0.0.0.0 will bind to all NICS and TCP stacks on the computer, while 127.0.01, doesn't get to the link layer at all -- and it only meant to test local applications.  By using 0.0.0.0 we say "bind to any addresses associated any NICS in this machine". Once you do this, other machines (that have a network route to yours) can now access your web service. Starting with your app bound to the loopback (127.0.0.1), is appropriate when you want only your local applications (local to you machine) be able to access what you do.

* Port: Set the port to anything you want - just make sure there is nothing else already running on this port. The standard HTTP port is port 80. When running on your local machine, a common one is 8080. The default for Flask is 5000. (generally, it's a good rule to stay away from any ports lower than 5000... and especially below 1024 (which include a number of commonly used reserved ports) )

* Debug: Set the debug flag to True to enable debugging of the application. In debug mode the debugger will kick in when an unhandled exception occurs and the integrated server will automatically reload the application if changes in the code are detected.

At this stage, you have your own local webserver running that will simply return the string "Hello World". You can access this server by pointing your browser to localhost:5000

This is simple, but later we will return HTML pages and apply CSS styling to your HTML. For now, just make sure you understand the basic application above.

### SIDENOTE on Decorators:

Notice the line containing `@app.rout()`. This is a decorator, yes ... They're back (que the horror music). But, this time we won't have to much around with customizing our own, we simply will use that ones that are part of the Flask library.

## Using the app.route decorator

The `@app.route()` decorator provides a entry point to access your content, think of it like a webserver directory with a default index.html file that is the content you wish to display`

```python

from flask import Flask

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return "Hello world!"

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return "What your you like to know about?"

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return "Sorry, we're not here. This all is just an illusion."

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```
[^flask02.py^](./flask02.py)

If we run the above program, we have a simple web app. Point your browser to address http://127.0.0.1:8080 (or your local IP) and see the page.

Also, note that we can add multiple routes (or paths) to the same function:

```python
from flask import Flask

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
@app.route('/home')
def home():
    return "Hello world!"

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return "What your you like to know about?"

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
@app.route('/contacts/')  # be sure to include both forward slashes
def contact():
    return "Sorry, we're not here. This is all an illusion."

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```
[^flask02a.py^](./flask02a.py)


## 'rendering' pages

Now, using Flask we can also serve and render template webpages. By default, any templates are stored in the subfolder templates. Putting these anywhere else without "telling" flask, will result in generating an error when we reference these. Also note that we do not need to include the template folder name in the path reference in our code. (see below)

Let's create three simple html pages and serve this in response to our three "routes" we've created thus far.

First, let's edit our program to render the templates. We start by importing "render_template" from the flask library, and then editing each of our app.routes to server the rendered_content of html pages (rather the simple strings we responded with before)

```python
from flask import Flask, render_template

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return render_template("./ex1/home.html")

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return render_template("./ex1/about.html")

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return render_template("./ex1/contact.html")

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```
[^click here for code^](./flask03.py)


Now, we need to create the template html files. This isn't a course in HTML, by you'll find that HTML is quite easy to learn the basics of (see [here](http://www.w3schools.com/html/)).

As  I mentioned at the start of this section, we store templates in the templates subfolder. We can also create folders within this template folder. I'll start by creating a subfolder called ex1 to hold our templates for this first example.

Now, let's create a simple home page called home.html (and store this is the subfolder ./templates/ex1

```html
<!DOCTYPE html>
<html>
<body>
  <h1>MIS407 Homepage</h1>
  <p>This is a test website</p>
</body>
</html>
```
[^home.html^](./templates/ex1/home.html)


And then copy this file and edit for each of the other two pages.


```html
<!DOCTYPE html>
<html>
<body>
  <h1>MIS407 About Page</h1>
  <p>This is a test website</p>
</body>
</html>
```
[^about.html^](./templates/ex1/about.html)


```html
<!DOCTYPE html>
<html>
<body>
  <h1>MIS407 Contact Page</h1>
  <p>This is a test website</p>
</body>
</html>
```
[^contact.html^](./templates/ex1/contact.html)


Now, if we run our program, we now are "serving up" web pages. Try it, and see the results.

Point your webrowser to http://127.0.0.1:8080

## Let's add an navigation menu

We could copy the same HTML code in each of the files we will add to our site, but this wouldn't be the best approach. Instead, it would be much easier to manage our web site content if we created a separate file to hold the navigation menu and then include this for each of our web pages we will serve.


```python
from flask import Flask, render_template

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return render_template("./ex2/home.html")

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return render_template("./ex2/about.html")

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return render_template("./ex2/contact.html")

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```
[^flask04.py^](./flask04.py)

NOTE: If you're familiar with HTML, you'll notice that we have some odd looking code in the html below. This embedded code is parsed by Flask and allows us to dynamically create webpages using these embedded bits of code.

Save the code below in the templates folder as layout.html

```html
<!DOCTYPE html>
<html>
<body>
  <header>
    <div class="container">
      <h1 class="logo">MIS407 Web App</h1>
      <strong><nav>
        <ul class="menu">
          <li><a href="{{ url_for('home') }}">Home</a></li>
          <li><a href="{{ url_for('about') }}">About</a></li>
          <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
      </nav></strong>
    </div>
  </header>
  <div class="container">
    {%block content%}
    {%endblock%}
  </div>
</body>
</html>
```
[^./templates/ex2/layout.html^](./templates/ex2/layout.html)

...and, then add the code blocks to (what are not) the child html templates.

NOTE: Here we "extend" the layout HTML we just wrote (notice the line {%extends "layout.html"%}) by inserting in the block content found within this file. We do this for each of our three "pages", home, about, and content.

```html
{%extends "./ex2/layout.html"%}
{%block content%}
<div class="home">
  <h1>MIS407 Homepage</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[./templates/ex2/home.html](./templates/ex2/home.html)

```html
{%extends "./ex2/layout.html"%}
{%block content%}
<div class="about">
  <h1>MIS407 About Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^./templates/ex2/about.html^](./templates/ex2/about.html)

```html
{%extends "./ex2/layout.html"%}
{%block content%}
<div class="contact">
  <h1>MIS407 Contact Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^./templates/ex2/contact.html^](./templates/ex2/contact.html)


Now, your can run flask04.py and point your browser to http://127.0.0.7:8080 to see the results.


## Adding CSS

Let's make this look a bit more "modern". Though HTML has information about how the content within it should be displayed, since HTML4 there has been an ongoing attempt to more clearly separate "what" should be displayed, from "how is should be displayed". CSS tells how the elements found within the HTML file should be displayed. This isn't to say you might have a "center" command within the HTML, but having details about how things should be displayed within the HTML is frowned upon.

Within our HTML file that get's sent to the requesting browser, we must include a "link" to our CSS file. The browser will then see this, and request the css file for instructions about how the content should be displayed.

There are plenty of resources available on the net to help you understand css, ie. https://www.w3schools.com/css/css_intro.asp

NOTE: This isn't a course on HTML and CSS. I'll provide only the basics here. What I'm focusing on is how to create the application portion, the "back end" portion of any web application. Increasing, web applications also involve complex "front end" code that consists of structure data (HTML), rendering data (CSS), and code (Javascript). And furthermore, these are now increasingly organized into higher level frameworks such as AngularJS.

PS: Unless you're trying to "learn" css, you wouldn't start from scratch. There are many free/open css templates out there, and generally you'd begin your project by starting with one of these and edit as you need. In my example below, I'm using a "custom" css -- so, it may not look the best -- I'm just trying to keep it simple for demonstration purposes.


copy all out files in the template/ex2 folder into a new folders called template/ex3. Moving into the ex3 folder, let's now update our layout html file to reference a css file.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Flask App</title>
  <link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}"
</head>
<body>
  <header>
    <div class="container">
      <h1 class="logo">MIS407 Web App</h1>
      <strong><nav>
        <ul class="menu">
          <li><a href="{{ url_for('home') }}">Home</a></li>
          <li><a href="{{ url_for('about') }}">About</a></li>
          <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
      </nav></strong>
    </div>
  </header>
  <div class="container">
    {%block content%}
    {%endblock%}
  </div>
</body>
</html>
```
[^./templates/ex3/layout.html^](./templates/ex3/layout.html)

Now, since we have referenced a CSS file, we need to add this to our site. The Flask package will look for static content (i.e. CSS and images) in a subfolder called "static". We can then organize our static folder to include subfolders for categories of static content (css subfolder, images subfolder, etc.)

Now, let's create a subfolder to hold our main.css and create out css file. For Flask, the default location for css files is ./static/css ... we'll save our css file as main.css (as per the filename we chose when we wrote the updated layout HTML above)

```css


/*
 * Main body
 */

 body {
  margin: 0;
  padding: 0;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #060;
}

/*
 *  The header area
 */

header {
  background-color: #DFB887;
  height: 35px;
  width: 100%;
  opacity: .9;
  margin-bottom: 10px;
}

header h1.logo {
  margin: 1px;
  font-size: 1.7em;
  color: #5f4f5f;
  text-transform: uppercase;
  float: left;
}

header h1.logo:hover {
  color: #ffa;
  text-decoration: none;
}

/*
 * The body content where we've create div's
 */

.container {
  width: 700px;
  margin: 0 auto;
}

div.home {
  padding: 10px 0 30px 0;
  background-color: #D6D6FA;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
}

div.about {
  padding: 10px 0 30px 0;
  background-color: #E6E6FA;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
}

div.contact {
  padding: 10px 0 30px 0;
  background-color: #F6F6FA;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
}


/*
* Formatting of our menu content
*/

.menu {
  float: right;
  margin-top: 8px;
}

.menu li {
  display: inline;
  margin: 0px 10px;
}


.menu li a {
  color: #404040;
  text-decoration: none;
}


```
[^./static/css/main.css^](./static/css/main.css)

Finally, we need update each of our three main pages (main, contact, and about) to use our new layout. Therefore we also need to update our main flask python script (now at flask05.py)

```python
from flask import Flask, render_template

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return render_template("./ex3/home.html")

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return render_template("./ex3/about.html")

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return render_template("./ex3/contact.html")

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```
[^click here for code^](flask05.py)

...now, each of the webpage templates references our updated layout.html.

```html
{%extends "./ex3/layout.html"%}
{%block content%}
<div class="home">
  <h1>MIS407 Homepage</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^./templates/ex3/home.html^](./templates/ex3/home.html)

```html
{%extends "./ex3/layout.html"%}
{%block content%}
<div class="about">
  <h1>MIS407 About Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^./templates/ex3/about.html^](./templates/ex3/about.html)

```html
{%extends "./ex3/layout.html"%}
{%block content%}
<div class="contact">
  <h1>MIS407 Contact Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^./templates/ex3/about.html^](./templates/ex3/about.html)


## For next class

In the code above, we have covered the basics of developing a Flask web service. This code though, is very "template" driven. We can create custom responses using output from our python code -- which we'll cover next class. We also need to "deploy" this application on a central server. We'll be using "heroku" for this.

NOTE: Next two classes (Friday before, and Monday after break) class will be a work at your own pace class - there will be no formal class. The lecture notes will be released Thursday. NOTE: For the test, you will not be request to deploy any applications to Heroku.
