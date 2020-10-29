from flask import Flask, render_template
import os
from threading import Thread

app = Flask(__name__)


def forward():
    print("Forward!")


def backward():
    print("Backward!")


def left():
    print("Left!")


def right():
    print("Right!")


def stop():
    print("Stop!")


@app.route("/")
def home():
    return render_template("MotorControlGUI2.html")


@app.route("/<action1>")
def action1(action1):
    global message
    if action1 == "forward":
        message = "forward"
        thread1 = Thread(target=forward)
        thread1.start()
    if action1 == "backward":
        message = "backward"
        thread2 = Thread(target=backward)
        thread2.start()
    if action1 == "left":
        message = "left"
        thread3 = Thread(target=left)
        thread3.start()
    if action1 == "right":
        message = "right"
        thread4 = Thread(target=right)
        thread4.start()
    if action1 == "stop":
        message = "stop"
        thread5 = Thread(target=stop)
        thread5.start()
    return ""


if __name__ == "__main__":
    app.run(debug=True)
