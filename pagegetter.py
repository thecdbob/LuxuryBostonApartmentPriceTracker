import requests
from bs4 import BeautifulSoup

base_url = 'https://7796310.onlineleasing.realpage.com/'
query_parameter = '?SiteId=4501693&SearchUrl=https%3A%2F%2F500oceanavenue.com%2Ffloorplans%2F&MoveInDate=07/26/2022#k=91194'

r = requests.get(base_url + query_parameter)
#print(r.status_code)
#print(r.content)

# use beautifulsoup to parse the html
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())