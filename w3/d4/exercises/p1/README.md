## Markit API Wrapper

Today is your first challenge using a web API. Cool!

First install 'requests' using pip3. We'll be dependent on this library, as it is definitely the best [HTTP request library](http://docs.python-requests.org/en/latest/) in Python. Take a look at the code snippet and get an idea of what it's doing. We'll be using requests to get live stock market data.

The API we'll be using is [Markit on Demand](http://dev.markitondemand.com/)

How do HTTP requests work? Well, everytime you browse the web you are making http requests. You are asking for data from a URL. Your browser usually expects data in the form of HTML.

We could request HTML in our code also, but it's kind of a mess. Instead we're going to request [JSON](http://en.wikipedia.org/wiki/JSON), which Python will treat like a native object courtesy of the requests library.

Take a look at these links so you know what to expect from the API. Read through the docs for Markit on Demand.

http://dev.markitondemand.com/Api/v2/Lookup/json?input=Netflix

http://dev.markitondemand.com/Api/v2/Quote/json?symbol=AAPL

#### Step 1: Wrap the API calls in an object  
Wrap the calls to Markit on Demand in a class. I've already started it for you. Write the methods get_company_data and get_quote. company_search takes a company's name in English and returns some basic data, like the formal name, the exchange it is on, and most importantly it's ticker symbol. The API will likely return more than one. get_quote takes a ticker symbol and receives up to the minute quote data.

#### Step 2:  
Test that your functions are working in the python interpreter. What happens if you send an incorrect string and it can't find the company, does it throw an error? Fix this - we don't want your program crashing on users.