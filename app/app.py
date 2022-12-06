from flask import Flask, render_template, request
from time import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='192.168.100.232', port=5500)