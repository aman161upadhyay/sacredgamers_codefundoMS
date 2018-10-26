
from flask import Flask, redirect, url_for, request, make_response,render_template
import csv
app = Flask(__name__)
from flask_mail import Mail, Message
app.secret_key = 'tSd1zNl8ElzjpAZ0fcQ!7RpejAG3eGD3'
cities = ["Mumbai","Chennai","Kolkata","Delhi"]
@app.route('/success/<city>')
def success(city):
   index = cities.index(city)
   temp = 0
   with open('result.csv',"r") as file:
      rd = csv.reader(file)
      for item in rd:
         if(temp == index):
            return render_template('index.html',data=item)
         temp += 1


@app.route('/setcity')
def setcity():

   if(request.args.get('city')):
      city = request.args.get('city')
      resp = make_response(redirect(url_for('success',city = city)))
      resp.set_cookie('city', city)
      return resp

   else:
      return redirect(url_for('index'))

@app.route('/')
def index():
	 
	if not request.cookies.get('city'):
		return render_template('login.html')
	return redirect(url_for('success',city = request.cookies.get('city')))

@app.route('/logout')
def logout():
   resp = make_response(redirect(url_for('success',city = city)))
   resp.set_cookie('city', '', expires=0)
   return resp


if __name__ == '__main__':
   app.run(debug = True)