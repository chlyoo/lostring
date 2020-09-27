#LostRing 
Location Based AI Supported Lost and Found system 
###Summary
- Used <u>Python3</u>, <u>Flask</u> framework, <u>MongoDB</u> and <u>Jinja2 template</u>
- Public API, Kakao Map API
- Can search lost and found items.
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