from bs4 import BeautifulSoup


with open("/home/buluag/gh/python_projects/software_projects/web_scraping/index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())  #tum girintileri gostermek icin kullanilir.

#title etiketiyle birlikte yazdirma
tag1 = doc.title
print(tag1)

#title etiketinin sadece icindeki ifadeyi yazdirma
tag2 = doc.title
print(tag2.string)

#icinde p gecen ifadeleri bulma
tags = doc.find_all("p")
print(tags)

#center etiketini etiketiyle beraber yazdirma
tag3 = doc.center 
print(tag3)

#clouds.jpg ifadesini yazdirma
img_tag = doc.find("img")
src_tag = img_tag["src"]
print(src_tag)

#BOTTOM ifadesini yazdirma
align_tag = img_tag["align"]
print(align_tag)

#butun p etiketlerini bir liste halinde yazdirma
p_tag = doc.find("p")
#b etiketini yazdirma
b_tag = p_tag.find("b")
#red rengini yazdirma
color_tag = b_tag["color"]
print(color_tag)

