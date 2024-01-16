from flask import Flask, request, render_template, make_response 
import json
#import pandas as pd

app = Flask(__name__)

@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/name")  
def helloyoke():
    return "Hello, Yoke!"

@app.route("/home", methods=['POST'])
def homefn():
    print('We are in home')

    namein = request.form.get('fname')
    lastnamein = request.form.get('lname')
    print(namein)
    print(lastnamein)
    return render_template("home.html",name='nameid')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0', port=5001