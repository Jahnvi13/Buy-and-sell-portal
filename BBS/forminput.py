# coding: utf-8
from flask import Flask, render_template, request
from script import inputUserData
app = Flask(__name__)

@app.route('/')
def test():
   #return render_template('test.html')
   return render_template("formnew.html")

@app.route('/UserEntry', methods=['POST','GET'])
def UserEntry():
  aname = request.form['name']
  adegreeprogram = request.form['first-name']
  aemail= request.form['email']
  apurpose = request.form['purpose']
  aitem = request.form['item']
  amessage = request.form['message']
  aprice=request.form['price']
  print("he in userentry")

  #called inside userentry
  inputUserData(aname, adegreeprogram, aemail, apurpose, aitem, amessage, aprice)
  return "Your response has been recorded"


@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html", result = result)

if __name__ == '__main__':
   app.run(debug = True)

