import discord
import os
import random
from discord.ext import commands
import youtube_dl
import asyncio

# Ustawienia bota
prefix = "!"  # Możesz dostosować prefiks komendy według własnych preferencji
token = "MTE5NDAwNzEzOTYxNDczMjM3MA.GQCVL8.FeN8UvF_lTFm0I9RGZJDjcg1ySJ2w-AA1pRBzw"  # Zastąp "TUTAJ_TWÓJ_TOKEN" rzeczywistym tokenem bota

# Inicjalizacja bota
intents = discord.Intents.all()  # Lub możesz dostosować Intents według własnych potrzeb
bot = commands.Bot(command_prefix=prefix, intents=intents)
soundcloud_link = "https://soundcloud.com/sebastian-niezgoda-889984368/xddd?si=5f10dc03f39a435eb2b1f586e16a2736&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
soundcloud_link2 = "https://soundcloud.com/sebastian-niezgoda-889984368/a-moze-jestem-gejem?si=c0f75b44903c452fbd00eaf397657142&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
constant_user_id = 279627398587219968
image_urls = [
    
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/1.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/2.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/3.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/4.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/5.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/6.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/7.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/8.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/9.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/10.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/11.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/12.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/13.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/14.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/15.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/16.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/17.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/18.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/19.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/20.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/21.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/22.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/23.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/24.webp?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/25.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/26.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/27.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/28.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/29.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/30.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/31.jpg?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/32.png?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/33.png?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/34.png?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/35.png?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/36.png?raw=true",
    "https://github.com/SebastianNiezgoda/DiscordBotRafal/blob/main/foto/37.png?raw=true",
    
    


    
    
]
# Komenda do wysyłania losowego zdjęcia
@bot.command(name="rafal")
async def losowe_zdjecie(ctx):
    # Wybierz losowy URL obrazu
    losowy_url = random.choice(image_urls)
    await ctx.send("hej jestem Rafal cipka, ciesze sie ze wybrales moje uslugi. Oto moja mega sexi fota:")
    # Prześlij obraz na serwer Discord
    await ctx.send(losowy_url)
@bot.command(name="prostefakty") 
async def play_soundcloud(ctx):
    # Sprawdź, czy autor komendy jest na kanale głosowym
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        # Dołącz do kanału głosowego
        voice_channel = await channel.connect()

        # Konfiguracja youtubedl
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(soundcloud_link, download=False)
            url = info['formats'][0]['url']
            voice_channel.play(discord.FFmpegPCMAudio(url))

        # Poczekaj, aż dźwięk się zakończy
        while voice_channel.is_playing():
            await asyncio.sleep(1)

        # Opuść kanał głosowy
        await voice_channel.disconnect()
    else:
        await ctx.send("Musisz być na kanale głosowym, aby użyć tej komendy.")
@bot.command(name="gej") 
async def play_soundcloud(ctx):
    # Sprawdź, czy autor komendy jest na kanale głosowym
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        # Dołącz do kanału głosowego
        voice_channel = await channel.connect()

        # Konfiguracja youtubedl
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(soundcloud_link2, download=False)
            url = info['formats'][0]['url']
            voice_channel.play(discord.FFmpegPCMAudio(url))

        # Poczekaj, aż dźwięk się zakończy
        while voice_channel.is_playing():
            await asyncio.sleep(1)

        # Opuść kanał głosowy
        await voice_channel.disconnect()
    else:
        await ctx.send("Musisz być na kanale głosowym, aby użyć tej komendy.")
        
        
@bot.command(name="fakty2")       
async def mention_constant_user(ctx):
    # Pobierz obiekt użytkownika na podstawie ID
    constant_user = await bot.fetch_user(constant_user_id)

    # Wyślij wiadomość z oznaczeniem stałego użytkownika
    await ctx.send(f"{constant_user.mention} jest gejem")
      

# Uruchomienie bota
bot.run(token)