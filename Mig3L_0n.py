from twitchio.ext import commands
import time
from os import system
system("title KUKORO - MAZMORRA")

# REEMPLAZAR POR TUS DATOS
Canales = ['CANAL']
Administradores = ['ADMINISTRADOR'] 
Comando = 'COMANDO'
TokenTwitch = 'TOKEN'

class Bot(commands.Bot):
    def __init__(self):         
        super().__init__(token = oauth:0fkx7b61e09frmk1qs201ildy6fxzl, prefix = '_0n', initial_channels = tm_ballenocr,brasitos10,bro_paper)

    async def event_ready(self):   
        print(f'\x1b[3;35m --> {self.nick.capitalize()}\x1b[3;32m conectado a {tm_ballenocr,brasitos10,bro_paper}\x1b[0;m')  
        print(f'\x1b[3;35m --> Administradores: \x1b[3;37m{tm_ballenocr,brasitos10,bro_paper}\x1b[0;m')  
        print(f'\x1b[3;33m --> {#dino}\x1b[3;34m para invocarlo') 

    async def event_message(self, ctx):
        if ctx.echo:
            return
        Canal = (f'{ctx.channel}').replace('<Channel name: ','').replace('>','')
        Mensaje = f'{ctx.content}'
        if(Administradores.__contains__(ctx.author.name)):
            if(Mensaje.lower() == Comando.lower()):  
                await ctx.channel.send('!kukoro')
                time.sleep(2)
                await ctx.channel.send('!getinfo')  
                print(f'\x1b[3;36m --> Invocado por {ctx.author.name} en {Canal}\x1b[0;m')                            
bot = Bot()
bot.run()
