try:
   from flask import Flask, render_template, request, url_for
except:
   #Install neccesary modules
   import os
   try:
      os.system('pip install --upgrade')
      os.system('pip install flask')
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
      os.system('pip install --upgrade')
      os.system('pip install numpy==1.19.3')
      import numpy as np
   except:
      print('Your OS doesn\'t understand default commands for install dependencies, so try run this file as administrator, or install numpy module for yourself')
      import sys
      sys.exit()

#Import controller
import os
from numericalMethods import NM
from controllerNM import ControllerNM
from controllerMatrix import ControllerMatrix
from controllerConversor import ControllerConversor
import sys

app = Flask(__name__)
nmc = ControllerNM(NM())
mc = ControllerMatrix()
cc  = ControllerConversor()

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
      nmc.setUp(request.form)
      nmc.setMethod(False)
      nmc.setResult(True)
   else:
      nmc.setMethod(False)
      nmc.setResult(False)
   return render_template('numericalMethods.jinja', nmc=nmc)

@app.route('/makeMatrix', methods=["GET", "POST"])
def makeMatrix():
   data = None
   if request.method == "POST" and len(request.form) == 1 and not mc.getN():
      mc.setN(request.form['n'])
      mc.setResult(False)
   elif request.method == "POST" and '0' in request.form:
      data = request.form
      mc.setN(False)
      mc.setResult(True)
   else:
      mc.setN(False)
      mc.setResult(False)
   return render_template('makeMatrix.jinja', mc=mc,data=data)

@app.route('/conversor', methods=["GET", "POST"])
def conversor():
   data = None
   if request.method == "POST":
      data = request.form
      cc.setResult(True)
   else:
      cc.setResult(False)
   return render_template('conversor.jinja', cc=cc,data=data)

@app.route('/user/<name>')
def user(name):
   return render_template('user.jinja', name=name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.jinja',e=e), 404


#snippet for update static files in web debugging
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
   app.run(debug=True)
