from bs4 import BeautifulSoup
import requests

with open("/home/buluag/gh/python_projects/software_projects/web_scraping/index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())

option_tag_all = doc.find_all("option")
#print(option_tag_all)

option_tag_first = doc.find("option")
print(option_tag_first)

#course-type yazdirmak icin
course_type = option_tag_first["value"]
print(course_type)

#course-type yerine hello world yazdiralim yani html'yi guncelleyelim
option_tag_first["value"] = "hello world!"
print(option_tag_first["value"])

print(option_tag_first.attrs)

tags = doc.find_all(["p", "div", "li"])
print(tags)