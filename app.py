import os
import sys
sys.path.insert(0, '/home/jdbigham.com/cgi-bin/testFlask/lib/python2.7/site-packages') 

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4000)
