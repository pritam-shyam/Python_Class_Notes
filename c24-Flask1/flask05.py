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
