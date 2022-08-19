import discord
from discord.ext import commands
#from discord.commands import Option
from discord.ui import *
from token_reader import read_token

# SETUP BÁSICO
#--------------------------------------------------------------------------------------------------------------------

#intents = discord.Intents.all() # recebe todas as permissão, por enquanto DESATIVADA
client = commands.Bot(command_prefix="!") # cria a instância do bot, é através desse objeto que se controla tudo
token = read_token() # le o token do arquivo token.txt e guarda na variável

# COMANDOS
#--------------------------------------------------------------------------------------------------------------------

@client.command(name='luffy') # esse comando manda uma mensagem no mesmo canal em que o comando foi utilizado
async def luffy(ctx):
    await ctx.send("Luffy no Baka!") # a palavra-chave "await" é necessária pois o processo de enviar uma mensagem é assíncrono, ou seja, ele n tem um tempo de execução determinado, varia de acordo com conexão com a api do discord, rede e etc... por isso temos que indicar ao programa que continue o bot rodando mesmo enquanto a ação está em processo

@client.event
async def on_ready(): # essa função é acionada quando o bot fica online
    print(client.guilds)
    print("Online")
    print("------------------------------------------------")

client.run(token) # inicia o bot com o token estipulado no início