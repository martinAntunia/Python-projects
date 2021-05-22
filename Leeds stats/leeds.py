from bs4 import BeautifulSoup
import urllib
from numpy.lib.function_base import append
import requests
import pandas as pd

#Página de la Premier League con estadísticas
web=requests.get("https://www.premierleague.com/clubs/9/Leeds-United/squad").text

#De cada tarjeta de cada jugador tomo el link a cada jugador
soup=BeautifulSoup(web,"lxml")

jugadores=soup.find_all("a",class_="playerOverviewCard")

#Función para tomar el link que muestra las estadísticas de cada jugador y devuelve todo su contenido
def tomaLink(jugador):
    link="https://www.premierleague.com"+jugador["href"].replace("overview","stats")

    estadisticas=requests.get(link).text
    soup_estadisticas=BeautifulSoup(estadisticas,"lxml")
    return(soup_estadisticas)

def almacenaJugadores():
    for jugador in jugadores:
        #Las primeras estadísticas de cada jugador están en un enlace que luego se modifica
        link="https://www.premierleague.com"+jugador["href"]

        estadisticas=requests.get(link).text
        soup_estadisticas=BeautifulSoup(estadisticas,"lxml")

        edad=soup_estadisticas.find("span",class_="info--light").text.replace("(","").replace(")","")
        
        #En algunos casos no hay datos de altura
        altura=soup_estadisticas.find("ul",class_="pdcol3").find("div",class_="info")
        if altura==None:
            pass
        else:
            altura=altura.text.replace("cm","")

        #Llamo a la función que definí más arriba
        soup_estadisticas=tomaLink(jugador)

        #Agrego a cada lista cada dato
        nombres.append(soup_estadisticas.find("div",class_="name").text)
        numeros.append(soup_estadisticas.find("div",class_="number").text)
        posicion=soup_estadisticas.find_all("div",class_="info")[1].text
        posiciones.append(posicion)
        apariciones.append(soup_estadisticas.find("span",class_="statappearances").text.strip())
        goles.append(soup_estadisticas.find("span",class_="statgoals").text.strip())
        asistencias.append(soup_estadisticas.find("span",class_="statgoal_assist").text.strip())
        amarillas.append(soup_estadisticas.find("span",class_="statyellow_card").text.strip())
        rojas.append(soup_estadisticas.find("span",class_="statred_card").text.strip())
        edades.append(edad)
        alturas.append(altura)


def almacenaArqueros():
    for lugar,jugador in enumerate(jugadores):
        soup_estadisticas=tomaLink(jugador)

        #Si el jugador es arquero, los datos van para las listas de arquero. Lo mismo hago con las distintas posiciones
        if posiciones[lugar]=="Goalkeeper":
            atajadas.append(soup_estadisticas.find("span",class_="statsaves").text.strip())
            penales_atajados.append(soup_estadisticas.find("span",class_="statpenalty_save").text.strip())
            vallas_invictas.append(soup_estadisticas.find("span",class_="statclean_sheet").text.strip())
            goles_recibidos.append(soup_estadisticas.find("span",class_="statgoals_conceded").text.strip())
            for index,lista in enumerate(listas_arquero):
                lista.append(listas[index][lugar])

def almacenaDefensores():
    for lugar,jugador in enumerate(jugadores):
        soup_estadisticas=tomaLink(jugador)

        if posiciones[lugar]=="Defender":
            vallas_invictas_defensa.append(soup_estadisticas.find("span",class_="statclean_sheet").text.strip())
            tackles.append(soup_estadisticas.find("span",class_="stattackle_success").text.strip())
            cruces.append(soup_estadisticas.find("span",class_="statinterception").text.strip())
            aereo_ganado.append(soup_estadisticas.find("span",class_="statduel_won").text.strip())
            aereo_perdido.append(soup_estadisticas.find("span",class_="statduel_lost").text.strip())
            for index,lista in enumerate(listas_defensa):
                lista.append(listas[index][lugar])

def almacenaMediocampistas():
    for lugar,jugador in enumerate(jugadores):
        soup_estadisticas=tomaLink(jugador)

        if posiciones[lugar]=="Midfielder":
            recuperaciones.append(soup_estadisticas.find("span",class_="statball_recovery").text.strip())
            pases.append(soup_estadisticas.find("span",class_="stattotal_pass_per_game").text.strip())
            for index,lista in enumerate(listas_mediocampo):
                lista.append(listas[index][lugar])

def almacenaAtacantes():
    for lugar,jugador in enumerate(jugadores):
        soup_estadisticas=tomaLink(jugador)

        if posiciones[lugar]=="Forward":
            goles_partido.append(soup_estadisticas.find("span",class_="statgoals_per_game").text.strip())
            goles_cabeza.append(soup_estadisticas.find("span",class_="statatt_hd_goal").text.strip())
            eficacia_remates.append(soup_estadisticas.find("span",class_="statshot_accuracy").text.strip())
            ocasiones_perdidas.append(soup_estadisticas.find("span",class_="statbig_chance_missed").text.strip())
            for index,lista in enumerate(listas_ataque):
                lista.append(listas[index][lugar])

#Defino todas las listas, las generales y las particulares de cada posición

nombres=[]
numeros=[]
posiciones=[]
edades=[]
alturas=[]
apariciones=[]
goles=[]
asistencias=[]
amarillas=[]
rojas=[]

listas=[nombres,alturas,edades,apariciones,goles,asistencias,amarillas,rojas]

atajadas=[]
penales_atajados=[]
vallas_invictas=[]
goles_recibidos=[]

vallas_invictas_defensa=[]
tackles=[]
cruces=[]
aereo_ganado=[]
aereo_perdido=[]

recuperaciones=[]
pases=[]

goles_partido=[]
goles_cabeza=[]
eficacia_remates=[]
ocasiones_perdidas=[]

nombres_arquero=[]
alturas_arquero=[]
edades_arquero=[]
apariciones_arquero=[]
goles_arquero=[]
asistencias_arquero=[]
amarillas_arquero=[]
rojas_arquero=[]

listas_arquero=[nombres_arquero,alturas_arquero,edades_arquero,apariciones_arquero,goles_arquero,asistencias_arquero,amarillas_arquero,
rojas_arquero]

nombres_defensa=[]
alturas_defensa=[]
edades_defensa=[]
apariciones_defensa=[]
goles_defensa=[]
asistencias_defensa=[]
amarillas_defensa=[]
rojas_defensa=[]

listas_defensa=[nombres_defensa,alturas_defensa,edades_defensa,apariciones_defensa,goles_defensa,asistencias_defensa,amarillas_defensa,
rojas_defensa]

nombres_mediocampo=[]
alturas_mediocampo=[]
edades_mediocampo=[]
apariciones_mediocampo=[]
goles_mediocampo=[]
asistencias_mediocampo=[]
amarillas_mediocampo=[]
rojas_mediocampo=[]

listas_mediocampo=[nombres_mediocampo,alturas_mediocampo,edades_mediocampo,apariciones_mediocampo,goles_mediocampo,asistencias_mediocampo,
amarillas_mediocampo,rojas_mediocampo]

nombres_ataque=[]
alturas_ataque=[]
edades_ataque=[]
apariciones_ataque=[]
goles_ataque=[]
asistencias_ataque=[]
amarillas_ataque=[]
rojas_ataque=[]

listas_ataque=[nombres_ataque,alturas_ataque,edades_ataque,apariciones_ataque,goles_ataque,asistencias_ataque,amarillas_ataque,rojas_ataque]

#Llamo a todas las funciones que almacenan en la lista. Si ya tengo alguna tabla, puedo obviarla y llamar las faltantes
almacenaJugadores()
almacenaArqueros()
almacenaDefensores()
almacenaMediocampistas()
almacenaAtacantes()

#Almaceno en DataFrame las listas que irán a cada tabla
datos=pd.DataFrame({"Nombre":nombres,"Número":numeros,"Posición":posiciones,"Edad":edades,"Altura":alturas,"Apariciones":apariciones,
"Goles":goles,"Asistencias":asistencias,"Amarillas":amarillas,"Rojas":rojas})

datos_arquero=pd.DataFrame({"Nombre":nombres_arquero,"Altura":alturas_arquero,"Edad":edades_arquero,"Aparaciones":apariciones_arquero,
"Goles":goles_arquero,"Asistencias":asistencias_arquero,"Amarillas":amarillas_arquero,"Rojas":rojas_arquero,"Atajadas":atajadas,
"Penales atajados":penales_atajados,"Vallas invictas":vallas_invictas,"Goles recibidos":goles_recibidos})

datos_defensa=pd.DataFrame({"Nombre":nombres_defensa,"Altura":alturas_defensa,"Edad":edades_defensa,"Aparaciones":apariciones_defensa,
"Goles":goles_defensa,"Asistencias":asistencias_defensa,"Amarillas":amarillas_defensa,"Rojas":rojas_defensa,"Vallas invictas":vallas_invictas_defensa,
"Tackles efectivos":tackles,"Cruces":cruces,"Aéreos ganados":aereo_ganado,"Aéros perdidos":aereo_perdido})

datos_mediocampo=pd.DataFrame({"Nombre":nombres_mediocampo,"Altura":alturas_mediocampo,"Edad":edades_mediocampo,"Aparaciones":apariciones_mediocampo,
"Goles":goles_mediocampo,"Asistencias":asistencias_mediocampo,"Amarillas":amarillas_mediocampo,"Rojas":rojas_mediocampo,"Recuperaciones":recuperaciones,
"Pases":pases})

datos_ataque=pd.DataFrame({"Nombre":nombres_ataque,"Altura":alturas_ataque,"Edad":edades_ataque,"Aparaciones":apariciones_ataque,
"Goles":goles_ataque,"Asistencias":asistencias_ataque,"Amarillas":amarillas_ataque,"Rojas":rojas_ataque,"Goles/partido":goles_partido,
"Goles cabeza":goles_cabeza,"Remates eficaces":eficacia_remates,"Ocasiones perdidas":ocasiones_perdidas})

#Con Pandas genero las tablas
datos.to_csv("leeds.csv",index=False)
datos_arquero.to_csv("arqueros.csv",index=False)
datos_defensa.to_csv("defensores.csv",index=False)
datos_mediocampo.to_csv("mediocampistas.csv",index=False)
datos_ataque.to_csv("atacantes.csv",index=False)