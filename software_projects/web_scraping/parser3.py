from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
print(result)

doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify)

tbody = doc.find_all("tbody")
print(tbody)