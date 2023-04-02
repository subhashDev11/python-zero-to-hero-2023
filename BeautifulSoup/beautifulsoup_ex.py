from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.python.org')
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.string)  # should print "Welcome to Python.org"
print(soup.find_all('a'))  # should print a list of all links in the document


print(soup.find_all('a', {'class': 'jump-to-menu'}))  # should print the jump-to-menu link
