# imports 
import os
import subprocess
from flask import Flask, request, make_response
from flask import Blueprint, render_template, redirect, url_for, request, flash
import converter as conv
import speechEmotionRecognition as sp
  
# initializing Flask app 
app = Flask(__name__) 
  

@app.route('/')
def login():
    return render_template('index.html')
    
    
@app.route('/uploadLabel',methods=['GET','POST'])
def uploadLabel():
    try:
        print('ENTREI AQUI')
        isthisFile=request.files.get('file')
        print(isthisFile)
        print(isthisFile.filename)
        isthisFile.save("./input1/"+isthisFile.filename)
        conv.converter()
    except:
        print('Algo aconteceu')
    
    return redirect(url_for('login'))


@app.route('/novo',methods=['GET','POST'])
def novo():
    sp.init()
    #x=subprocess.check_output(['python', 'test.py'])
    #print(x)
    return "CONSEGUIIIIIIIIII"
  
if __name__ == "__main__": 
    # serving the app directly 
    app.run() 
