import requests
from bs4 import BeautifulSoup


url = 'http://localhost:8080/'
response = requests.get(url)
raw_html = response.text
parser_html = BeautifulSoup(raw_html, 'html.parser')
print(parser_html.title.text)