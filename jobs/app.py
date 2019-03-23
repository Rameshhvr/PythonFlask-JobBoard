<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    retrun render_template('index.html')	
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    retrun render_template('index.html')	
>>>>>>> 4b036bf0d864911fe2f20921c320db864496e0c3
