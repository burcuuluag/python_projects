from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/p/1TS-000D-0WXP8?Item=1TS-000D-0WXP8&cm_sp=Homepage_SS-_-P3_1TS-000D-0WXP8-_-07112023"

result = requests.get(url)
#print(result.text)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())

#htmldeki fiyati bulmak istiyoruz
prices = doc.find_all(text="$")
parent = prices[0].parent
print(parent)
price = parent.find("strong")
print(price.string)
