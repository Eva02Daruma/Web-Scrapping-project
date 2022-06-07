from bs4 import BeautifulSoup
import requests
import re

producto_buscar = input("Que tipo de producto deseas buscar?")

url = f"https://www.falabella.com/falabella-cl/search?Ntt={producto_buscar}"
page = requests.get(url).text
doc = BeautifulSoup(page , "html.parser")

page_text = doc.find_all(class_= "jsx-1794558402 jsx-1104282991 pagination-button-mkp")
next_page = int(page_text[0].text.strip())
cur_page = int(next_page) - 1
max_page = int(page_text[1].text.strip())
print(cur_page)
print(max_page)

for page in range(1 , max_page + 1 ):
    url = f"https://www.falabella.com/falabella-cl/search?Ntt={producto_buscar}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    items = doc.find_all(text=re.compile(producto_buscar))
    for item in items:
        print(item)