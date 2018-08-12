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
    app.run(host="127.0.0.1", port=8080, debug=True)
