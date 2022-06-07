from bs4 import BeautifulSoup
import requests
from torch import parse_type_comment

url = "https://www.zmart.cl/scripts/prodView.asp?idProduct=81279"

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")


precios = doc.find_all( id = "PriceProduct")
parent = precios[0].parent

span = parent.find_all("span" , class_="ProdBox146_Precio")
div = parent.find("div")
for res in div:
    print(res.text)

#print(parent)
