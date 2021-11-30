from bs4 import BeautifulSoup
from hashlib import sha256
from random import choice
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests


if __name__ != "__main__":
    exit()


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot=commands.Bot(command_prefix = "c!")

#  variables globales
primer_numero = []
signo = ""
segundo_numero = []
var1 = 0
var2 = 0

#  Estado del bot

@bot.event
async def on_ready():
    #personalizado = discord.CustomActivity("Soy un pez")
    await bot.change_presence(activity=discord.Game(name="Ser un pez"))
    print("bot esta listo")



#  comprueba si el resultado de cualquier operacion termina en decimal

def comprobacion_numero(resultado):
    resultado = str(resultado)
    decimal = False
    for n in resultado:
        if n == "0":
            decimal = False
        else:
            decimal = True
    return decimal



#  OPERACIONES MATEMATICAS
@bot.command()
async def suma(ctx,num1,num2):
    resp = float(num1) + float(num2)
    if comprobacion_numero(resp) == False:
        resp = int(resp)
    await ctx.send(resp)

@bot.command()
async def multiplica(ctx,num1,num2):
    resp = float(num1) * float(num2)
    if comprobacion_numero(resp) == False:
        resp = int(resp)
    await ctx.send(resp)

@bot.command()
async def resta(ctx,num1,num2):
    resp = float(num1) - float(num2)
    if comprobacion_numero(resp) == False:
        resp = int(resp)
    await ctx.send(resp)

@bot.command()
async def divide(ctx,num1,num2):
    resp = float(num1) / float(num2)
    if comprobacion_numero(resp) == False:
        resp = int(resp)
    await ctx.send(resp)

@bot.command()
async def eleva(ctx,num1,num2):
    resp = float(num1) ** float(num2)
    if comprobacion_numero(resp) == False:
        resp = int(resp)
    await ctx.send(resp)


#  calculo con deteccion de signo

@bot.command()
async def calcula(ctx,operacion):
    calculo_error = False
    global var1
    global var2
    global signo
    global primer_numero
    global segundo_numero
    p = "abierto"
    numeros = [0,1,2,3,4,5,6,7,8,9]
    signos = ["+","-","*","/","÷","**","^"]
    puntuacion = [".",","]
    operacion = str(operacion)
    operacion = list(operacion)
    print(operacion)
    for n in operacion:
        if p == "abierto":
            if n not in signos:
                primer_numero.append(n)
            else:
                p = "cerrado"
                signo = n
        if p == "cerrado" and n not in signos:
            segundo_numero.append(n)
    print(primer_numero)
    print(signo)
    print(segundo_numero)
    var1 = "".join(primer_numero)

    #  borrar valores de variable primer_numero y segundo_numero
    primer_numero = str(primer_numero)
    primer_numero = ""
    primer_numero = list(primer_numero)   #  lo hice de esta forma ya que la funcion top es demaciado lenta

    var2 = "".join(segundo_numero)

    segundo_numero = str(segundo_numero)
    segundo_numero = ""
    segundo_numero = list(segundo_numero)


    #  variables ready

    var1 = float(var1)
    var2 = float(var2)




    #  SUMA
    if signo == "+":
        respuesta = var1 + var2
        if comprobacion_numero(respuesta) == False:
            respuesta = int(respuesta)
            print(respuesta)
        await ctx.send(respuesta)

    #  RESTA
    elif signo == "-":
        respuesta = var1 - var2
        if comprobacion_numero(respuesta) == False:
            respuesta = int(respuesta)
        await ctx.send(respuesta)

    #  MULTIPLICA
    elif signo == "*":
        respuesta = var1 * var2
        if comprobacion_numero(respuesta) == False:
            respuesta = int(respuesta)
        await ctx.send(respuesta)

    #  DIVIDE
    elif signo == "/" or signo == "÷":
        try:
            respuesta = var1 / var2
        except ZeroDivisionError:
            await ctx.send("Lo sentimos, no es posible el calculo")
            calculo_error = True
        if calculo_error == False:
            if comprobacion_numero(respuesta) == False:
                respuesta = int(respuesta)
            await ctx.send(respuesta)

    #  ELEVA
    elif signo == "**" or signo == "^":
        respuesta = var1 ** var2
        if comprobacion_numero(respuesta) == False:
            respuesta = int(respuesta)
        await ctx.send(respuesta)


    #  reset var
    var1 = ""
    var2 = ""


#  Al cachipun
@bot.command()
async def cachipun(ctx,tirada1):
    respuestas = ["piedra","papel","tijera"]
    tirbot = choice(respuestas)
    tirada1 = tirada1.lower()

    if bool(tirada1) == True:
        if tirada1 == "tijeras":
            tirada1 = "tijera"

        if tirada1 in respuestas:
            await ctx.send(tirbot)

            if tirada1 == tirbot:
                await ctx.send("Empate")    
            elif tirada1 == "piedra" and tirbot == "papel" or tirada1 == "papel"and tirbot == "tijera" or tirada1 == "tijera" and tirbot == "piedra":
                await ctx.send("jaja izi")
            else:
                await ctx.send("me falta practica :(")
        else:
            await ctx.send("parece que no sabes jugar XD")
    else:
        await ctx.send("falto tu jugada")



#   BUSQUEDA DE GOOGLE

@bot.command()
async def busca(ctx,*args):
    await ctx.send("funcionalidad en desarrollo")

    headers = {
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
        }

    resultado = requests.get(f"https://www.google.com/{args}",headers=headers)
    resultado_en_texto = resultado.text
    soup = BeautifulSoup(resultado_en_texto,"lxml")
    #campo_informacion = soup.find("")
    #print(campo_informacion)




#  Generador de hash

@bot.command()
async def hash(ctx, *args):
    entrada = []

    for n in args:
        entrada.append(n)
        word = " ".join(entrada)
    print(word)

    if bool(word) == False:
        await ctx.send("64 caracteres maximo")
    
    elif len(word) > 64:
        await ctx.send("64 caracteres maximo")

    else:
        word = word.encode()
        objeto_hash = sha256(word).hexdigest()
        await ctx.send(f"El hash resultante es: {objeto_hash}")


#  Analizador de url

@bot.command()
async def scanurl(ctx, link):
    respuesta = requests.get(f"https://urlvoid.com/scan/{link}")
    resultado_html = respuesta.text

    soup = BeautifulSoup(resultado_html,"lxml")
    campo_informacion1 = soup.find("tbody")

    labels_tr = []
    for i in campo_informacion1.find_all("tr",limit=8):
        labels_tr.append(i)

    tr1 = labels_tr[0]
    tr2 = labels_tr[1]  #  unused
    tr3 = labels_tr[2]
    tr4 = labels_tr[3]
    tr5 = labels_tr[4]  #  unused
    tr6 = labels_tr[5]
    tr7 = labels_tr[6]
    tr8 = labels_tr[7]

    info1 = tr1.find("strong").get_text()   #  direccion web
    info2 = tr3.find("span", class_="label label-success").get_text()   #  encontrado en 0 de 44 listas negras

    #  conseguir label adecuado
    td = 0
    for i in tr4.find_all("td"):
        td += 1
        if td == 2:
            tr4 = i  #  segunda etiqueta td conseguida
    

    tr4 = str(tr4)
    info3 = tr4.replace("<td>","")
    info3 = info3.replace("</td>","")   #  fecha de registro de dominio

    info4 = tr6.find("strong").get_text()   #  IP de dns

    #  conseguir label adecuado
    td = 0
    for i in tr7.find_all("td"):
        td += 1
        if td == 2:
            tr7 = i
    tr7 = str(tr7)
    info5 = tr7.replace("<td>","")
    info5 = info5.replace("</td>","")   #  Nombre DNS

    #  conseguir label adecuado
    td = 0
    for i in tr8.find_all("td"):
        td += 1
        if td == 2:
            tr8 = i

    info6 = tr8.find("a").get_text()    #  Numero sistema autónomo

    nombreASN = []
    tr8 = str(tr8)
    contador = 0
    for i in tr8:
        if i == " ":
            contador += 1
        print(contador)
        if contador >= 6:
            nombreASN.append(i)
            print(nombreASN)

    info6_1 = "".join(nombreASN)
    info6_1 = info6_1.replace("</td>","")     #  nombre sistema autónomo

    await ctx.send("Web: "+info1+"\n"
    "Encontrado en listas negras: "+info2+"\n"
    "Registro de dominio: "+info3+"\n"
    "Ip dns: "+info4+"\n"
    "Dns inverso: "+info5+"\n"
    "Numero sistema autónomo: "+info6+"\n"
    "Nombre sistema autónomo: "+info6_1)

    print(info1,info2,info3,info4,info5,info6,info6_1)

#  Traductor
@bot.command()
async def traduce(ctx,*args):

    headers = {
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
        }

    resultado_html = requests.get(f"https://www.google.com/search?q=traducir+{args}+a+ingles",headers=headers)
    resultado = resultado_html.text
    soup = BeautifulSoup(resultado,"lxml")
    
    cuadro_de_traduccion = soup.find( "pre",id="tw-target-text")
    print(cuadro_de_traduccion)
    texto_traducido = cuadro_de_traduccion.find("span",class_="Y2IQFc").get_text()
    print(texto_traducido)
    await ctx.send(f"```{texto_traducido}```")


#  API Clima
@bot.command()
async def clima(ctx,consulta):
    consulta = consulta.lower()
    await ctx.send("Lo sentimos esta opcion esta fuera de servicio :(")
"""
    access_key = ""
    params = {'access_key':"" ,"query": "Santiago",}

    for key, value in params.items():
        if key == "query":
            params[key] = consulta

    await ctx.send("Retraso aprox 10 segundos")
    api_result = requests.get("http://api.weatherstack.com/current", params=params)
    api_response = api_result.json()

    pais = api_response["location"]["country"]
    region = api_response["location"]["region"]
    hora = api_response["location"]["localtime"]
    grados = str(api_response["current"]["temperature"])
    humedad = str(api_response["current"]["humidity"])
    wind = str(api_response["current"]["wind_speed"])
    await ctx.send("Pais: "+pais+"\nRegion: "+region+"\nHora: "+hora+"\nTemperatura: "+grados+"°C\nHumedad: "+humedad+"%"+"\nViento: "+wind+"Km/h")
"""

#  COMANDO AYUDA

@bot.command()
async def ayuda(ctx):
    await ctx.send("""```
    Todos los comandos con ejemplos

    c!suma "1 1"
    c!resta "5 2"
    c!multiplica "3 5"
    c!divide "10 2"
    c!eleva "2 3"
    c!calcula "10/3" (este comando detecta el simbolo)
    c!cachipun "piedra"  (el legendario juego de piedra papel o tijera)
    c!hash "hola que tal 123" (genera un hash sha256 en base a lo que ingresaste)
    c!scanurl "netflix.com" (informacion sobre el enlace)
    c!traduce "hola buenas mañanas" (traduce tu texto a ingles, proximamente mas idiomas)
    c!busca "palabra o frase"  (proximamente)
    c!clima "santiago" (funcionalidad suspendida)```""")

bot.run(TOKEN)
