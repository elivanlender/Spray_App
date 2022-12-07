# coding=utf-8
from flask import Flask, render_template
from time import *
import Adafruit_BBIO.GPIO as GPIO

Out_1="P9_11"
Out_2="P9_12"
Out_3="P9_13"
Out_4="P9_14"
Out_5="P9_15"
Out_6="P9_16"
Out_7="P9_17"
Out_8="P9_18"
Out_9="P9_23"
Out_10="P9_24"
Out_11="P9_25"
Out_12="P9_26"
Out_13="P9_27"
Out_14="P9_30"
Out_15="P9_41"
Out_16="P9_42"
In_1="P8_7"
In_2="P8_8"
In_3="P8_9"
In_4="P8_10"
In_5="P8_11"
In_6="P8_12"
In_7="P8_14"
In_8="P8_15"
In_9="P8_16"
In_10="P8_17"
In_11="P8_18"
In_12="P8_26"

GPIO.setup(Out_1, GPIO.OUT)
GPIO.setup(Out_2, GPIO.OUT)
GPIO.setup(Out_3, GPIO.OUT)
GPIO.setup(Out_4, GPIO.OUT)
GPIO.setup(Out_5, GPIO.OUT)
GPIO.setup(Out_6 , GPIO.OUT)
GPIO.setup(Out_7, GPIO.OUT)
GPIO.setup(Out_8, GPIO.OUT)
GPIO.setup(Out_9, GPIO.OUT)
GPIO.setup(Out_10, GPIO.OUT)
GPIO.setup(Out_11, GPIO.OUT)
GPIO.setup(Out_12, GPIO.OUT)
GPIO.setup(Out_13, GPIO.OUT)
GPIO.setup(Out_14, GPIO.OUT)
GPIO.setup(Out_15, GPIO.OUT)
GPIO.setup(Out_16, GPIO.OUT)

GPIO.setup(In_1, GPIO.IN)
GPIO.setup(In_2, GPIO.IN)
GPIO.setup(In_3, GPIO.IN)
GPIO.setup(In_4, GPIO.IN)
GPIO.setup(In_5, GPIO.IN)
GPIO.setup(In_6, GPIO.IN)
GPIO.setup(In_7, GPIO.IN)
GPIO.setup(In_8, GPIO.IN)
GPIO.setup(In_9, GPIO.IN)
GPIO.setup(In_10, GPIO.IN)
GPIO.setup(In_11, GPIO.IN)
GPIO.setup(In_12, GPIO.IN)

app=Flask(__name__)

@app.route('/')
def index():
    GPIO.cleanup()
    GPIO.output(Out_1, GPIO.LOW)
    if GPIO.input(In_1):
        GPIO.output(Out_1, GPIO.HIGH)
    return render_template('index.html', DATO="Signal 1: Deactivated")

@app.route("/boton1", methods=['POST'])
def boton1():
    GPIO.cleanup()
    GPIO.output(Out_1,GPIO.HIGH)
    return render_template('index.html', DATO="Signal 1: Activated")

@app.route("/boton2", methods=['POST'])
def boton2():
    GPIO.cleanup()
    GPIO.output(Out_1,GPIO.LOW)
    return render_template('index.html', DATO="Signal 1: Deactivated")

@app.route("/boton3", methods=['POST'])
def boton3():
    while(1):
        GPIO.cleanup()
        while(GPIO.input(In_1)):
            GPIO.output(Out_1, GPIO.HIGH)
        GPIO.output(Out_1, GPIO.LOW)
    return render_template('index.html')
    

if __name__=='__main__':
    app.run(host='192.168.100.232', port=5500)