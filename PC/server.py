#!/usr/bin/env python
from flask import Flask, render_template, request, url_for, redirect, jsonify
import os
import webbrowser

# Create the server
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

#@app.route('/hello')
#def hello():
 #   return 'Hello, World'

@app.route('/postTest', methods=['POST','GET'])
def postTest():
    if request.method == 'POST':
        postData = request.form['text']
    #return jsonify(text=postData)
    #return redirect(url_for('text',text=postData))
        with open("dataFromServer.txt","wb") as fo:
              fo.write("Text input from server is: " + postData)
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        filename = 'file:///Users/nidhipatel/Desktop/pi/dataFromServer.txt'
        webbrowser.get(chrome_path).open(filename)      
        return postData
    

if __name__ == '__main__':
   #app.debug = True
   #app.run()  
   app.run(host="0.0.0.0")





