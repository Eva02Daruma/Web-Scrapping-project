from bs4 import BeautifulSoup
import requests
import re

producto_buscar = input("Que tipo de producto deseas buscar?")

url = f"https://www.zmart.cl/Scripts/prodSearch.asp?strSearch={producto_buscar}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
div = doc.find(id="ResultadoBusqueda")
#print(div)
items = div.find_all(text=re.compile(producto_buscar))

#Nombre del Producto 
nombreProducto = div.find_all( class_ = "ProdBox146_Descripcion")


#Precio del Producto
precios = div.find_all( class_ = "ProdBox146_Precio")
parent = precios[0].parent
countP = 0
#Check para cantidad de elementos
for precio in precios:
    countP = countP + 1
for titulo in nombreProducto:
    print(titulo.text)
print(f"el contador llego hasta {countP}")

for i in range(0 , countP):
    print(nombreProducto[i].text)
    print(precios[i].text)


#print(precioproducto)
