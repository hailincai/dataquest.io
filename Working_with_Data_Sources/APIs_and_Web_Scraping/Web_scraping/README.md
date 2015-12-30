# Web Scraping  
In this article, we will show how to use the beautifulsoup libaray to parse the HTML page, and get information we want.  
## Load the beautifulsoup library  
```python
from bs4 import BeautifulSoup
```  
## Using beautifulsoup library to parse a HTML page  
```python
# after this code line, parser points to the HTML tag
parser = BeautifulSoup(<html page content>, 'html.parser')
``` 
## Find out elements by tag name  
```python
# find the body tag
body_tag = parser.find_all("body")[0]
#find all div elements under body
div_tags = body_tag.find_all("div")
```  
## Find out elements by css selector  
```python
# the selector method can be applied to both parser, and the html element
# simple selector by one css selctor
parser.select("#<id>")
parser.select(".<class>")
parser.select("<tag name>")
# nested css selector sample
# div p will select all p under div
parser.select("div p")
# div .class #id 
#  first find all nodes with div tag
#  second for each div node, find child nodes with .class
#  for each node from step 2, find the child nodes with #id
parser.select("div .class #id")
```