#Banksalad 사전과제 
US stock symbol max profit over the last 180 days
###Summary
- Used <u>Python3</u>, <u>Flask</u> framework and <u>Jinja2 template</u>
- yfinance library used for stock price data
- Can search buy and sell date for US stock symbol in the main website(http://localhost:5000).
- Offers same data of json type(http://localhost:5000/api/symbol) with POST method.
##Execution
- Install python3 dependencies
```console
pip3 install -r requirements.txt
pip3 install -r requirements_win.txt
```
- Run server
```console
python3 setup.py runserver
```
- Acces to the webpage
http://localhost:5000

- Search with stock symbol from the main page ex)AAPL, MSFT, GOOG

- Testing
```console
pytest test/modelTest.py
pytest test/presentationTest.py
pytest test/service_test.py
```
-System Design
Presentation Layer 
- api, main

Business Layer
- service

Persistence Layer
- model