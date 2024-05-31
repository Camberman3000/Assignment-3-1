#Flask app using Python
# Hello World
from flask import Flask

#Create an instance of the Flask class
app = Flask(__name__)

#Define the route for the URL / and return the string Hello World
@app.route('/')
def index():
    return "<h1>Hello World - Here is my first Flask app!</h1><p>My name is <b>Mark Montenieri</b></p>"

#Run the app (python specific) and listen for requests on port 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000)