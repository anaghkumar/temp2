Json to String 

    json.dumps(a)
    
Json to String using an API using requests and “json.dumps”

    import json
    import requests
    
    # Get dummy data using an API
    res = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    
    # Convert data to dict
    data = json.loads(res.text)
    
    # Convert dict to string
    data = json.dumps(data)
    
    print(data)
    print(type(data))



 

<!-- https://www.geeksforgeeks.org/working-with-json-data-in-python/ -->


`What’s the use of Middleware in Django?
`
- Middleware is something that executes between the request and response. In simple words, you can say it acts as a bridge between the request and response. Similarly In Django when a request is made it moves through middlewares to views and data is passed through middleware as a response. 

