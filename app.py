# Import libraries and packages, they contain additional functions.
from flask import Flask, render_template
# Create web application using Flask
app = Flask("Orlando_De_Leon_Resume")
# Create our routes
@app.route('/')
def home():
 return render_template('index.html')
# Start the web application
app.run(
 debug=True
)