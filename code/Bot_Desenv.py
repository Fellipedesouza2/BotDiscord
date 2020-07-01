from Token_secreto import seu_token
from discord.ext import commands
from discord.utils import get
import discord, base64
from time import sleep
from datetime import datetime
from random import randint, choice
from Valores import ValorDolar

#DATA

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('-------GaussBot-Online--------')
    print(f'ID: {client.user.id}')
    print(f'NAME: {client.user.name}')
    print(f'Guildas conectado: {client.guilds}')
    print(10*'---')

@client.command()
async def PlayCassino(messege):
        channel = messege.channel
        sort1 = randint(0, 3)
        sort2 = randint(0, 3)
        sort3 = randint(0, 3)
        if sort1 == sort2 == sort3:
            await channel.send('🎰PROCESSANDO🎰')
            sleep(2)
            await channel.send('🤑Vc ganhou sortudo!!🤑')
        elif sort1 != sort2 == sort3 or sort2 != sort1 == sort3 or sort3 != sort1 == sort2:
            await channel.send('🎰PROCESSANDO🎰')
            sleep(2)
            await channel.send('🥺Chegou muito perto!🥺')
        elif sort1 != sort2 != sort3:
            await channel.send('🎰PROCESSANDO🎰')
            sleep(2)
            await channel.send('💩Vc perdeu💩')

@client.command(pass_context=True)
async def Creator(messege):
    channel = messege.channel
    await channel.send(f'‍💻Criador: Felipedesouza2‍\n🎉MELHOR GRUPO: Candy group <3🎉')

@client.command(pass_context=True)
async def connect(ctx):
    channel_messege = ctx.channel
    try:
        channel_voice = ctx.message.author.voice.channel
        await channel_voice.connect()
    except AttributeError:
        await channel_messege.send('🚨!VC PRECISA ESTAR CONNECTADO A UM CANAL!🚨')

@client.command(pass_context=True)
async def disconnect(ctx):
    pass

@client.command()
async def somar(ctx, num1:str, num2:str):
    if str(num1).isnumeric() and str(num2).isnumeric() == True:
        await ctx.send(f'{num1} + {num2} = {int(num1) + int(num2)}')
    else:
        await ctx.send('🚨!Apenas numeros!🚨')

@client.command()
async def dolar(ctx):
    await ctx.send(f'O dolar vale extamente:{ValorDolar()}')

@client.command()
async def info_modulo_dolar(ctx):
    await ctx.send('Font: https://br.advfn.com/cambio')
    await ctx.send('💻Codado em 30/06/2020 por Fellipe de souza!💻')

@client.command()
async def soma_PA(ctx, num1:int, num2:int, num3:int):
    formula = int(num1 * (num2 + num3) / 2)
    await ctx.send(f'A soma da PA é: {formula}')

@client.command()
async def Encode(ctx, valor:str):
    valor = valor.strip()
    cript = base64.b64encode(valor.encode('ascii'))
    cript = str(cript.decode('UTF-8'))
    await ctx.send(cript)

@client.command()
async def Decode(ctx, valor:str):
    try:
        valor = valor.strip()
        decode = base64.b64decode(valor, None, False)
        decode = str(decode.decode('UTF-8'))
        await ctx.send(decode)
    except:
        await ctx.send('🚨!Apenas B64 para decode!🚨')

@client.command()
async def Dado(ctx):
    dado1 = [1, 2, 3, 4, 5, 6]
    dado2 = [1, 2, 3, 4, 5, 6]
    escolha1 = choice(list(dado1))
    escolha2 = choice(list(dado2))
    await ctx.send('!🎲JOGANDO O DADO🎲!')
    sleep(2)
    await ctx.send(f'OS DADOS FORAM: [{escolha1}, {escolha2}, = {escolha1 + escolha2}]')



client.run(seu_token())
#💰 👑 💩 🎰 🎉 🚨

