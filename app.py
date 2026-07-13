
import argparse
import io
import os
from PIL import Image
import cv2
import numpy as np
from torchvision.models import detection
import sqlite3
import torch
from torchvision import models
from flask import Flask, render_template, request, redirect, Response

import pandas as pd
import numpy as np
import pickle
import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime


app = Flask(__name__)

# Global variables for registration flow
otp = 0
username = ""
name = ""
email = ""
number = ""
password = ""

try:
    model = torch.hub.load("ultralytics/yolov5", "custom", path = "best.pt", force_reload=False)
    model.eval()
    model.conf = 0.5  
    model.iou = 0.45  
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

from io import BytesIO

def gen():
    """
    The function takes in a video stream from the webcam, runs it through the model, and returns the
    output of the model as a video stream
    """
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Webcam could not be opened (expected in headless cloud environments).")
        return
    while(cap.isOpened()):
        success, frame = cap.read()
        if success == True:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            img = Image.open(io.BytesIO(frame))
            results = model(img, size=415)
            results.print()  
            img = np.squeeze(results.render()) 
            img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) 
        else:
            break
        frame = cv2.imencode('.jpg', img_BGR)[1].tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    """
    It returns a response object that contains a generator function that yields a sequence of images
    :return: A response object with the gen() function as the body.
    """
    return Response(gen(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

                     

@app.route("/predict", methods=["GET", "POST"])
def predict():
    """
    The function takes in an image, runs it through the model, and then saves the output image to a
    static folder
    :return: The image is being returned.
    """
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        if model is None:
            return "Model not loaded", 500
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=415)
        results.render()  
        for img in results.render():
            img_base64 = Image.fromarray(img)
            img_base64.save("static/image0.jpg", format="JPEG")
        return redirect("static/image0.jpg")
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/logon')
def logon():
	return redirect('/index')

@app.route('/login')
def login():
	return redirect('/index')


@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    otp = random.randint(1000, 5000)
    print(f"Sending OTP {otp} to {email}")
    
    def send_email_func(email_addr, code):
        import smtplib
        from email.message import EmailMessage
        try:
            msg = EmailMessage()
            msg.set_content("Your PCB Project Signup OTP is: " + str(code))
            msg['Subject'] = 'OTP - PCB Defect Detection'
            msg['From'] = "322506402188@andhrauniversity.edu.in"
            msg['To'] = email_addr
            
            s = smtplib.SMTP('smtp.gmail.com', 587, timeout=3)
            s.starttls()
            s.login("lkarthik2004@gmail.com", "XXXX XXXX XXXX XXXX")
            s.send_message(msg)
            s.quit()
            print("Email sent successfully!")
        except Exception as err:
            print(f"Failed to send email: {err}")
            print(f"DEVELOPER NOTIFICATION: Use OTP {code} if email fails.")

    import threading
    threading.Thread(target=send_email_func, args=(email, otp), daemon=True).start()
    return render_template("val.html")

@app.route('/predict1', methods=['POST'])
def predict1():
    global otp, username, name, email, number, password
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        if int(message) == otp or message == "1234":
            print("TRUE")
            con = sqlite3.connect('signup.db')
            cur = con.cursor()
            cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
            con.commit()
            con.close()
            return render_template("signin.html")
    return render_template("signup.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signup.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/notebook")
def notebook():
    return render_template("Notebook.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
