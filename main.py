from email.mime import base
from gc import callbacks
import discord
from discord.ext import commands
#from discord.commands import Option
from discord.ui import *
from token_reader import read_token
import requests
from info import base_url
import json

# SETUP BÁSICO
#--------------------------------------------------------------------------------------------------------------------

intents = discord.Intents.all() # recebe todas as permissão, por enquanto DESATIVADA
client = commands.Bot(command_prefix="!", intents=intents) # cria a instância do bot, é através desse objeto que se controla tudo
token = read_token() # le o token do arquivo token.txt e guarda na variável

# SUB-CLASSES UI COMPONENTS
#--------------------------------------------------------------------------------------------------------------------

class SetupView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Criar canais",style=discord.ButtonStyle.green, custom_id="confirm channel")
    async def button_callback(self, button, interaction):
        dids = []
        for member in interaction.guild.members:
            if member.id != interaction.user.id and member.id != client.user.id:
                dids.append([member.name,member.id])        
        print(dids)
        class_req = requests.post(base_url+"/create_class",params={"guild": interaction.guild_id, "name":interaction.guild.name})
        if class_req.status_code == 200:
            setup_req = requests.post(base_url+"/setup_class",params={"dids":dids, "guild":interaction.guild_id,"prof":interaction.user.id,"prof_name":interaction.user.name})
            if setup_req.status_code == 200:
                print("setup completed")
                await interaction.response.edit_message(content="Setup completado com sucesso!", view=None)
            else:
                print(class_req.content)
                await interaction.response.edit_message(content="Error setting up class",view=None)
        else:
            print(class_req.content)
            await interaction.response.edit_message(content="Error creating class",view=None)
    #@discord.ui.button(label="Não criar",style=discord.ButtonStyle.red, custom_id="cancel channel",callback=button_callback)
# COMANDOS
#--------------------------------------------------------------------------------------------------------------------

@client.command(name='luffy') # esse comando manda uma mensagem no mesmo canal em que o comando foi utilizado
async def luffy(ctx):
    await ctx.send("Luffy no Baka!") # a palavra-chave "await" é necessária pois o processo de enviar uma mensagem é assíncrono, ou seja, ele n tem um tempo de execução determinado, varia de acordo com conexão com a api do discord, rede e etc... por isso temos que indicar ao programa que continue o bot rodando mesmo enquanto a ação está em processo

@client.slash_command(name="setup", description="Setup your class!", guild_ids=[1010241678445137920])
async def setup(ctx):
    setView = SetupView()
    await ctx.respond("Deseja criar automaticamente os canais de textos necessários?",view=setView, ephemeral=True)

@client.event
async def on_ready(): # essa função é acionada quando o bot fica online
    print(client.guilds)
    print("Online")
    print("------------------------------------------------")

client.run(token) # inicia o bot com o token estipulado no início