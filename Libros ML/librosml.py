from bs4 import BeautifulSoup
import urllib
from bs4.element import SoupStrainer
import requests

#El usuario introduce el título del libro a buscar
search=input("Introduzca el título del libro que desea: ")

#Combinamos la url de ML para buscar, el título que coloca el usuario
#y lo ordenamos por precio según la web de ML. Lo convertimos a texto
ml="https://libros.mercadolibre.com.ar/"
url=requests.get(ml+search+"_OrderId_PRICE").text

#Buscamos cada publicación
soup=BeautifulSoup(url,"lxml")
posts=soup.find_all("div",class_="ui-search-result__content-wrapper")

cont=0

#Seleccionamos el título y el precio para mostrarlos
#Usamos un contador para mostrar solo los primeros 5 títulos
for post in posts:
    title=post.find("h2",class_="ui-search-item__title").text
    price=post.find("span",class_="price-tag-fraction").text
    link=post.div.a["href"]
    print(f"Título del post: {title}")
    print(f"Precio: {price}")
    print(f"Ir: {link}")
    print("")
    cont+=1
    if cont==5:
        break