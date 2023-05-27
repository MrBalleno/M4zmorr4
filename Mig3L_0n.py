from twitchio.ext import commands
import time
from os import system
system("title KUKORO - MAZMORRA")

Canales = ['Tu_Canal'] # <-------- Canal o Canales donde se va a conectar ['canal1','canal2']
Administradores = ['Tu_Usuario'] # <----- Usuario y/o Usuarios quienes podran usar el bot ['usuario1','usuario2']
Comando = '#angel' # <---- Comando o Mensaje  al cual respondera el bot
TokenTwitch = 'oauth:abcdefghijklmnopqrstuvwxyz' # <----- Oauth (Bot) (https://twitchapps.com/tmi/)

class Bot(commands.Bot):
    def __init__(self):         
        super().__init__(token = TokenTwitch, prefix = '_', initial_channels = Canales)

    async def event_ready(self):   
        print(f'\x1b[3;35m --> {self.nick.capitalize()}\x1b[3;32m conectado a {Canales}\x1b[0;m')  
        print(f'\x1b[3;35m --> Administradores: \x1b[3;37m{Administradores}\x1b[0;m')  
        print(f'\x1b[3;33m --> {Comando}\x1b[3;34m para invocarlo') 

    async def event_message(self, ctx):
        if ctx.echo:
            return
        Canal = (f'{ctx.channel}').replace('<Channel name: ','').replace('>','')
        Mensaje = f'{ctx.content}'

        if(Administradores.__contains__(ctx.author.name)):
            if(Mensaje.lower() == Comando.lower()):  
                await ctx.channel.send('!kukoro_O')
                time.sleep(3)
                await ctx.channel.send('!getinfO_o')  
                print(f'\x1b[3;36m --> Invocado por {ctx.author.name} en {Canal}\x1b[0;m')    
                         
bot = Bot()
bot.run()

################################# MIG3L_0N ##########################################
#01 ---> Descargar e Instalar Python (https://www.python.org/downloads/).
#02 ---> Abrir CMD y ejecutar (pip install twitchio) para instalar las dependencias.

# ---> Ten en cuenta que algunos canales permiten seguir para poder escribir en el chat.
