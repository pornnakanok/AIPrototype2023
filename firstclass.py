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

@app.route("/home2")
def home2():
    return render_template("home.html",name='Yoke')#,name = 'Tohn', fav = name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0', port=5001