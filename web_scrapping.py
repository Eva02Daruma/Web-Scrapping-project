from bs4 import BeautifulSoup
import requests

url = "https://www.zmart.cl/scripts/prodView.asp?idProduct=81279"

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")


precios = doc.find_all(text = "$")

