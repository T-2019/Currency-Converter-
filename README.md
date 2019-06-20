# Currency-Converter

A Python based FX API service for a bank which calculates the currency conversion

### Prerequisites

*This Python API service runs on a flask server so flask will need to be install to run.*


### Running the API

#### If git clone:

git clone https://github.com/T-2019/Currency-Converter-.git

cd Currency-Converter-

python FX.py

#### If zip file:

Unzip the file and run FX.py in an IDE of your choice (I use geany)

*In both cases please ensure result.html and home.html remain in the templates folder*


### Using the API

After running FX.py on the flask server please navigate to the address the server is running on followed by "/home". In my case this is 127.0.0.1:5000/home. 

This is the front end of the API and where you enter the amount you wish to convert and the to and from currencies. After enter/selecting these details click convert and you'll be redirected to a page showing the converted value (or an "Insufficient funds" page if the amount entered is below 0)

### Notes

"/currency" displays in JSON format the currency rates used for calculations

An "Insufficient funds" page is displayed if after applying the fees (flat 25GBP for amouns below 1000 GBP and 1% if >= 1000GBP) the final amount falls below 0. Please note Fees are applied prior to conversion.


Thank you for your time!
