# Working with APIs  
This article will talk about the basic of how to retrieve the data from web API using GET method  
## Libraries used in this article  
* requests library  
Using this lirabry to get the content from web API using HTTP  
* json library  
If the web API returned data in JSON format, we will use this library to parse the content  
## Using requests library to HTTP call  
```python
# requests.GET sample
parameters = {}
headers = {}
response = requests.get("API URL", params=parameters, headers=headers)
# check response.status_code first, only process if it is 200
if (response.status_code == 200):
    #get the content_type from response.headers
    if (response.headers["content-type"] == "application/json"):
        #get the response content as json object
        #json object you can use as a dictionary
        data = response.json()

# requests POST sample, same format for PUT / PATCH 
# POS --- create new object
# PUT --- replace whole object
# PATCH --- update partial object
# this call will translate the python dict object to form-encoded parameter and send them
requests.post("API_URL", headers=headers, data=<dict>)
# this call will translate the python dict object for json string, and set the content-type to application/json when send the request
requests.post("API_URL", headers=headers, json=<dict>)

# requests DELETE sample, remove object from server side
requests.delete("API URL", headers=headers)
```  
## Using json library  
```python
json_str = "{'test1':'data1', 'test2':{'test21':'data21'}}"
json_obj = json.loads(json_str)
json_str1 = json.dump(json_obj)
```