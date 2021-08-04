
from flask import Flask
#import pymysql
import os
import webbrowser
from flask import Flask, render_template             


app = Flask(__name__)

@app.route("/")

def home():
    return render_template("fresh_tomatoes.html")

if __name__ == "__main__":
    app.run()