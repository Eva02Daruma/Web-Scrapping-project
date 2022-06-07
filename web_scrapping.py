from bs4 import BeautifulSoup
import requests
import re

productId = '81279'
url = f"https://www.zmart.cl/scripts/prodView.asp?idProduct={productId}"

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")

def consultaproductoId(productId):
    #Consulta por titulo y precio del producto
    url = f"https://www.zmart.cl/scripts/prodView.asp?idProduct={productId}"
    result = requests.get(url)
    doc = BeautifulSoup(result.text , "html.parser")    
    #Precio del Producto
    precios = doc.find_all( id = "PriceProduct")
    parent = precios[0].parent
    divprecio = parent.find("div")
    count = 0
    for res in divprecio:
        if count == 2 :
            #String del precio es precioproducto
            precioproducto = res.text.strip()
        count = count + 1

       
    # Titulo del producto

    tituloproducto = doc.find_all( id = "ficha_producto" )
    parent = tituloproducto[0].parent
    h1titulo = parent.find_all("h1")
    tp = h1titulo[0].text
    tituloproducto = tp.strip()

    #Disponibilidad del Producto

    disponible =  doc.find_all( id = "ficha_producto")
    parent = disponible[0].parent
    divDisp = parent.find_all("div" , class_ = "txTituloRef")
    statusDisp = divDisp[0].text.strip()
    
    # Lo que se Imprime

    print(f" \n Titulo del Producto : {tituloproducto} \n Precio : ${precioproducto} \n Estado : {statusDisp}")


#Consultas 
consultaproductoId('82450')

consultaproductoId('82426')

consultaproductoId('82199')



# Ejercicio Tree Siblings 

urlPrincipal = f"https://www.zmart.cl/Scripts/default.asp"

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")

tbody = doc.tbody
trs = tbody.contents

print(trs[1].previous_sibling)