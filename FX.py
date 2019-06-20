import json
import webbrowser
from flask import Flask, redirect, url_for, request, jsonify, render_template
app = Flask(__name__)
# Hardcoded in currency rates below with GBP set as the base rate. Rates are based off of XE.com values.
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
    result=0 #final rate to convert by
    fee=25 #the 25 GBP fee
    
    # handling/converting cases whereby the input currency is not the base currency which in this case is GBP
    if in_currency not in currency["base"] and in_currency in currency["rates"]:
		    amount= amount/currency["rates"][in_currency]
    
    if in_currency != out_currency:
	  
     #optional task of adding fees, fee are applied before converstion
     if amount < 1000:
      amount=amount-fee
     else:
      amount=amount-(amount*0.01)
    
    #setting the final rate to convert by
    if out_currency in currency["rates"]:
            result=currency["rates"][out_currency]
    else:
     result=1
    if (amount*result) <0:
     #if converted amount is less than 0 due to fees
     return (f"Insufficient funds")
    else: 
       display= (f"{round((amount*result),2)} {out_currency}")
       #output to html page
       return render_template('result.html', display=display)

    

@app.route('/convert',methods = ['POST', 'GET'])
def convert():
      # retrieving date from forms 
      money = request.form['nm']
      in_rate= request.form ['in_rate']
      out_rate= request.form ['out_rate']
      #passing them to the result html page
      return redirect(url_for('success',amount = money, in_currency=in_rate, out_currency=out_rate))
   

@app.route('/currency', methods=['GET'])
def api_all():
    #view currency rates as JSON file at this page
    return jsonify(currency)
    
 
@app.route('/home', methods=['GET'])   
def api_home():
    #dymanically applying currency options to HTML select form
    currnecy_list = list(currency["rates"].keys())
    currnecy_list.insert(0, currency["base"])
    return render_template('home.html', in_rate=currnecy_list, out_rate=currnecy_list)
	

if __name__ == '__main__':
   app.run(debug = True)
