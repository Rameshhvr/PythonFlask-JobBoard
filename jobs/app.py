from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    retrun render_template('index.html')	
