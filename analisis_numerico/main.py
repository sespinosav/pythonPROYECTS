try:
   from flask import Flask, render_template, request
except:
   #Install neccesary modules
   import os
   try:
      os.system('pythn3 -m pip install --upgrade')
      os.system('python3 -m pip install flask')
      os.system('pip install --upgrade')
      os.system('pip install flask')
      os.system('conda install flask')
      os.system('conda install -c anaconda flask')
      from flask import Flask, render_template, request
   except:
      print('Your OS doesn\'t understand default commands for install dependencies, so try run this file as administrator, or install flask module for yourself')
      import sys
      sys.exit()

try:
   import numpy as np
except:
   #Install neccesary modules
   import os
   try:
      os.system('pythn3 -m pip install --upgrade')
      os.system('python3 -m pip install numpy')
      os.system('pip install --upgrade')
      os.system('pip install numpy')
      os.system('conda install numpy')
      os.system('conda install -c anaconda numpy')
      import numpy as np
   except:
      print('Your OS doesn\'t understand default commands for install dependencies, so try run this file as administrator, or install numpy module for yourself')
      import sys
      sys.exit()

#Import controller
from controllerNM import ControllerNM
app = Flask(__name__)
nmc = ControllerNM()

@app.route('/')
def index():
   return render_template('index.jinja')

@app.route('/guie')
def guie():
   return render_template('guie.jinja')

@app.route('/numericalMethods', methods=["GET", "POST"])
def numericalMethods():
   """
   If numericalMethod need method so view result is false
   else if need variables to generate result of method, so
   result is true
   then result you can back to numericalMethods, so
   result is false and doesn't exist method
   """
   if request.method == "POST" and len(request.form) == 1:
      nmc.setMethod(request.form['method'])
      nmc.setResult(False)
   elif request.method == "POST" and len(request.form) > 1:
      nmc.setMethod(request.form['variable2'])
      nmc.setMethod(False)
      nmc.setResult(True)
   else:
      nmc.setMethod(False)
      nmc.setResult(False)
   return render_template('numericalMethods.jinja', nmc=nmc)

@app.route('/makeMatrix')
def makeMatrix():
   return render_template('makeMatrix.jinja')

@app.route('/conversor')
def conversor():
   return render_template('conversor.jinja')

@app.route('/user/<name>')
def user(name):
   return render_template('user.jinja', name=name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.jinja',e=e), 404

if __name__ == '__main__':
   app.run(debug=True)
