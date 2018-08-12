# w11c31

# Deploying our web site - let's push this code to the cloud

## PaaS and Flask

We'll be using Heroku. Heroku supports many development languages and environments. In our case, we will be using Python and creating a Web Interface to our application.

## Deploying website into the "cloud"

With out experience with the command line and git, deploying on Heroku is relatively easy. Cloud based services also allow us to focus on app functionality and programming instead of server/infrastructure issues.

I've broken the deployment process down to 8 steps.

### Step 1 - Set up Virtual environment

First, we need to set up a virtual environment (and it's a good practice is to have a "clean" installation of python, specific to our application).

This isn't a virtual machine, but rather a virtual python environment. This simply allows us to create a python library specifically for our project. Up until this point, when we do a "pip install" we've been installing our libraries in one central library for all out python projects. There are times though where we may want to operate a separate library specific to our project. For our Heoku deployment, we just want to push the essentials to Heroku, therefor we will create a virtual environment.

First, we need to venv library.

```
pip install virtualvenv
```

let's mkdir a "mysite" and then go into this directory and create a new python virtualvenv

```
python -m venv virtual
```

Now, we need to install any libraries I'm using.

install flask
```
$ virtual\Scripts\pip install flask
```

install requests (which we use for the weather page)
```
$ virtual\Scripts\pip install requests
```

Now, run our site to make sure it's working OK in our virtual environment.
```
$ virtual\Scripts\python mis407site\flask08.py
```

### Step2: Create an account in Heroku

http://www.heroku.com

Once you have an account, you can log in an see my "dashboard"

We will create our app using the command line.

#### Step 3: Download the heroku toolbelt.

heroku provides a command line utility to help us manage our website.

https://devcenter.heroku.com/articles/heroku-command-line

NOTE: The heroku toolbelt should already be installed on rm1117 lab computers.


#### Step 4: Once installed, "login" .

```
$ heroku login
Enter your Heroku credentials.
Email: <your email that you used to sign up>
Password (typing will be hidden):
Logged in as <your email>
```

#### Step 5: Create an app (a place to receive our code on the website)

```
$ heroku create mis407-demo
Creating mis407-demo... done
https://mis407-demo.herokuapp.com/ | https://git.heroku.com/mis407-demo.git
```

NOTE: If I want to see a list of you current apps.

```
$ heroku apps
=== timsmith@iastate.edu Apps
mis407-demo
```

Now, we can go to our dashboard, and see that we have a new app.

NOTE: The app name will need to be unique (different from this app name -- try adding your initials to the name to make it unique)

### Step 6: Create 3 files that will be needed by Heroku

Before we push our app to Heroku we need three files, requirements.tx Procfile and

Also, I need to install gnuicorn (Heroku needs this to run our webserver)

```
$virtual\Scripts\pip install gunicorn
```

#### Step 6a: Create a requirements.txt
This file contains a list of dependencies we want Heroku to use in the remote environment (we need a way to ask the server to install Flask and requests packages)

```
$ virtual\Scripts\pip freeze
click==6.6
Flask==0.11.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
requests==2.11.1
Werkzeug==0.11.11
```

We cut and paste this list into a new file called requirements.txt

#### Step 6b: Create a Procfile

Just use Atom to create a file called "Procfile" (note: there is not extension)

In this file we type:

```
web: gunicorn flask07:app
```
This file tells Heroku we have a gunicorn application whose mainfile is flask08 and whose main app (flask app) is called app (note: this must be the same name as the variable we instantiated the Flask object to)

#### Step 6c: Create a runtime.txt.

This file tells Heroku which python it should use to run our code.

```
python-3.5.2
```

#### Step 7: Deploy using Git.

To load our application into Heroku, we use git.

First, set up our origin to be the heroku server. We need the heroku toolbelt for this....

```
$ cd mysite/mis407site
$ git init
$ heroku git:remote -a mis407-demo
```

Now, we can work with/manage our Heroku app like it was a GitHub repo.

```
$ git add .
$ git commit -am "Initial push MIS407 app"
$ git push heroku master
```

(see: https://dashboard.heroku.com/apps/mis407-demo/deploy/heroku-git)

After you've done this, you should be able to go to your console and see that the app has been successfully deployed and built.

![heroku dashboard](images/heroku_dash_after.png)

#### Step 8: Test

Now, go to your new site and check that everything is working OK.


------

If you have trouble with the above, there are plenty of tutorials out there. Take a look at Heroku.com (or mr google)
