from bs4 import BeautifulSoup
import requests
import re

productId = '81279'
url = f"https://www.zmart.cl/scripts/prodView.asp?idProduct={productId}"

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")

def consultaproductoId(productId):
    url = f"https://www.zmart.cl/scripts/prodView.asp?idProduct={productId}"
    result = requests.get(url)
    doc = BeautifulSoup(result.text , "html.parser")    
    #Precio del Producto
    precios = doc.find_all( id = "PriceProduct")
    parent = precios[0].parent

    span = parent.find_all("span" , class_="ProdBox146_Precio")
    divprecio = parent.find("div")
    count = 0
    for res in divprecio:
        if count == 2 :
            #String del precio es precioproducto
            precioproducto = res.text
        count = count + 1

       

    # Titulo del producto

    tituloproducto = doc.find_all( id = "ficha_producto" )
    parent = tituloproducto[0].parent
    h1titulo = parent.find_all("h1")
    tp = h1titulo[0].text
    tituloproducto = tp.strip()
    
    # Lo que se Imprime

    print(f" \n Titulo del Producto : {tituloproducto} \n Precio : ${precioproducto}")





consultaproductoId('82450')

consultaproductoId('82426')



#otra prueba para precio

# nprecios = doc.find_all( text = re.compile("\$.*"), limit=1)
# for nprecio in nprecios:
#     print(nprecio.strip())
# #nparent = precios[0].parent