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
