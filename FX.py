import json
import webbrowser
from flask import Flask, redirect, url_for, request, jsonify, render_template
app = Flask(__name__)

currency ={
    "base": "GBP",
    "rates": {
        "AUD": 1.83687,
        "CAD": 1.67941,
        "CHF": 1.25609,
        "CNY": 8.72818,
        "EUR": 1.12586,
        "JPY": 136.633,
        "USD": 1.26426}}

@app.route('/success/<float:amount><in_currency> <out_currency>')
def success(amount, in_currency, out_currency):
    result=0
    fee=25
    
    if in_currency not in currency["base"] and in_currency in currency["rates"]:
		    amount= amount/currency["rates"][in_currency]
    
    if in_currency != out_currency:
			       
     if amount < 1000:
      amount=amount-fee
     else:
      amount=amount-(amount*0.01)
		      
    if out_currency in currency["rates"]:
            result=currency["rates"][out_currency]
    else:
     result=1
    if (amount*result) <0:
     return (f"Insufficient funds")
    else: 
       display= (f"{round((amount*result),2)} {out_currency}")
       return render_template('result.html', display=display)

    

@app.route('/convert',methods = ['POST', 'GET'])
def login():
      money = request.form['nm']
      in_rate= request.form ['in_rate']
      out_rate= request.form ['out_rate']
      return redirect(url_for('success',amount = money, in_currency=in_rate, out_currency=out_rate))
   

@app.route('/currency', methods=['GET'])
def api_all():
    return jsonify(currency)
    
 
@app.route('/home', methods=['GET'])   
def api_home():
    currnecy_list = list(currency["rates"].keys())
    currnecy_list.insert(0, currency["base"])
    return render_template('home.html', in_rate=currnecy_list, out_rate=currnecy_list)
	

if __name__ == '__main__':
   app.run(debug = True)
