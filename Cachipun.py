from hashlib import sha256
from logging import exception
from random import choice
from discord import client
import discord
from discord.client import Client
from discord.ext import commands
from discord.ext.commands.errors import PrivateMessageOnly
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot=commands.Bot(command_prefix = 'c!')

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



#  comprobacion tipo de resultado en operacion matematica
def comprobacion_numero(resultado):
    resultado = str(resultado)
    decimal = False
    for n in resultado:
        if n == "0":
            decimal = False
        else:
            decimal = True
    return decimal



#  OPERACIONES MATEMATICAS--------------------
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


#  calculo con deteccion de signo--------------
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

    #  borrar valores de variable primer_numero
    primer_numero = str(primer_numero)
    primer_numero = ""
    primer_numero = list(primer_numero)

    #  -----------------borrar valores de variable primer_numero
    var2 = "".join(segundo_numero)

    #  borrado de valores variable segundo_numero
    segundo_numero = str(segundo_numero)
    segundo_numero = ""
    segundo_numero = list(segundo_numero)

    #  --------------borrado de valores variable
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


#-CACHIPUN-----------------------------------------------------
@bot.command()
async def cachipun(ctx,tirada1):
    respuestas = ["piedra","piedra","papel","papel","tijera","tijeras"]
    tirbot = (choice(respuestas))
    tirada1 = tirada1.lower()

    if tirada1 in respuestas:
        
        await ctx.send(tirbot)
        if tirada1 == tirbot:
            await ctx.send("Empate")
    
        elif tirada1 == "piedra" and tirbot == "papel" or tirada1 == "papel"and tirbot == "tijera" or tirada1 == "papel" and tirbot == "tijeras" or tirada1 == "tijera" and tirbot == "piedra" or tirada1 == "tijeras" and tirbot == "piedra":
            await ctx.send("EZZ")
        else:
            await ctx.send("me falta practica :(")
    else:
        await ctx.send("parece que no sabes jugar XD")

#  FUNCION BUSQUEDA DE GOOGLE

@bot.command()
async def busca(ctx,):
    await ctx.send("funcionalidad en desarrollo")

"""@bot.command()
async def busca(ctx,*args):
    params = {"search?q" : ""}
    palabra_o_frase = []
    for n in args:
        palabra_o_frase.append(n)

    if bool(palabra_o_frase) == False:
        await ctx.send("escribe lo que quieres buscar, frase o palabra")
    else:
        try:
            texto_a_buscar = "+".join(palabra_o_frase)
        except exception:
            pass
    str(texto_a_buscar)
    print(type(texto_a_buscar))
    for key, value in params.items():
        if key == "search?q":
            params[key] = texto_a_buscar

    print(params)

    #website = "https://www.google.com"
    #resultado = requests.get("https://www.google.com/",params=params)
    #print(resultado)"""

#  Generador_de_hash

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


#-CONSULTA DEL CLIMA------------------------------------
@bot.command()
async def clima(ctx,consulta):
    consulta = consulta.lower()
    await ctx.send("Lo sentimos esta opcion esta fuera de servicio :(")

    #access_key = ""
    #params = {'access_key':"" ,"query": "Santiago",}

    #for key, value in params.items():
    #    if key == "query":
    #        params[key] = consulta

    #await ctx.send("Retraso aprox 10 segundos")
    #api_result = requests.get("http://api.weatherstack.com/current", params=params)
    #api_response = api_result.json()

    #pais = api_response["location"]["country"]
    #region = api_response["location"]["region"]
    #hora = api_response["location"]["localtime"]
    #grados = str(api_response["current"]["temperature"])
    #humedad = str(api_response["current"]["humidity"])
    #wind = str(api_response["current"]["wind_speed"])
    #await ctx.send("Pais: "+pais+"\nRegion: "+region+"\nHora: "+hora+"\nTemperatura: "+grados+"°C\nHumedad: "+humedad+"%"+"\nViento: "+wind+"Km/h")
#-----------------------------------------CONSULTA DEL CLIMA
#COMANDO DE AYUDA-------------------------------------------

@bot.command()
async def ayuda(ctx):
    await ctx.send("""```Todos los comandos con ejemplos
    \nc!suma "1 1"
    \nc!resta "5 2"
    \nc!multiplica "3 5"
    \nc!divide "10 2"
    \nc!eleva "2 3"
    \nc!calcula "10/3" (este comando detecta el simbolo)
    \nc!cachipun "piedra"  (el legendario juego de piedra papel o tijera)
    \nc!hash "hola que tal 123" (genera un hash con el algoritmo sha256 en base a lo que ingresaste)
    \nc!busca "palabra o frase"  (proximamente)
    \nc!clima "santiago" (funcionalidad suspendida)```""")

bot.run(TOKEN)
