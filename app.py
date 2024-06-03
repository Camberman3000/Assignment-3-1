#Flask app using Python
# Hello World
from flask import Flask, send_file, render_template_string


#Create an instance of the Flask class
app = Flask(__name__)

#Define the (root) route for the URL / and return the string Hello World
@app.route('/')
def index():
    return "<h1>Hello World - Here is my first Flask app!</h1><p>My name is <b>Mark Montenieri</b></p>"

#Define a route that accepts a string as a parameter and returns a greeting (ex: http://localhost:5000/greet/Mark)
@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {name}</h1> <p>Welcome to our site!</p>"


#Define a route that downloads a story file (ex: http://localhost:5000/download_story)
@app.route('/download_TheForgottenMelody')
def download_TheForgottenMelody():
    # Define the file path
    file_path = 'TheForgottenMelody.txt'
    return send_file(file_path, 'TheForgottenMelody.txt', as_attachment=True)


# Download link to the story
@app.route('/read_TheForgottenMelody')
def read_TheForgottenMelody():
# Create an html template that will display the link
    html_content = """
    <h1>The Forgotten Melody</h1>
    <p>Click the link below to download the story:</p>
    <a href="/download_TheForgottenMelody">The Forgotten Melody</a>
    """
    return render_template_string(html_content)
     
     

#Run the app (python specific) and listen for requests on port 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000)