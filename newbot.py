# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
from random import randint
import asyncio
import re
import requests
import random
import time
import os
client = discord.Client()

@client.event
async def on_ready():
	botver = "Alpha 2.0.3 Build 29"
	game = discord.Game("%s" % botver)
	await client.change_presence(status=discord.Status.online, activity=game)
	print("bot is connecting...")

def timechange(create):
	if create.hour < 10:
		chour = '0'+str(create.hour)
	else:
		chour = str(create.hour)
	if create.minute < 10:
		cminute = '0'+str(create.minute)
	else:
		cminute = str(create.minute)
	if create.second < 10:
		csecond = '0'+str(create.second)
	else:
		csecond = str(create.second)
	return ('%s.%s.%s %s:%s:%s UTC' % (create.year, create.month, create.day, chour, cminute, csecond))

async def myinfo(user, mch):
	joinedtime = timechange(user.joined_at)
	createdtime = timechange(user.created_at)
	embed = discord.Embed(title="{} Info".format(user.name), description="slice of information of {}".format(user.name), color=0x25DFE4)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Joined at Server", value=joinedtime, inline=True)
	embed.add_field(name="Role", value=user.top_role, inline=True)
	embed.add_field(name="Status", value=user.status, inline=True)
	embed.add_field(name="Joined at Discord", value=createdtime, inline=True)
	embed.set_thumbnail(url=user.avatar_url)
	await mch.send(embed = embed)

async def serverinfo(server, mch):
	createdtime = timechange(server.created_at)
	embed = discord.Embed(title="{} Info".format(server.name), description="slice of information of {}".format(server.name), color=0x25DFE4)
	embed.add_field(name="Created at", value=createdtime, inline=True)
	embed.add_field(name="ID", value=server.id, inline=True)
	embed.add_field(name="Members", value=server.member_count, inline=True)
	embed.add_field(name="Server Owner", value=server.owner, inline=True)
	embed.add_field(name="Role Count", value=len(server.roles), inline=True)
	embed.add_field(name="Emoji Count", value=len(server.emojis), inline=True)
	embed.set_thumbnail(url=server.icon_url)
	await mch.send(embed = embed)

async def helpp(mch):
	embed = discord.Embed(title="봇 정보", description="더 자세한 사항은 개발자에게 문의하세요", color=0x25DFE4)
	embed.add_field(name="봇 커멘드 목록", value='hello\nmyinfo\nserverinfo\nbotinfo\nsource', inline=True)
	embed.set_thumbnail(url=mch.guild.me.avatar_url)
	await mch.send(embed = embed)

async def source(mch):
	embed = discord.Embed(title="봇 소스코드", description="더 자세한 사항은 개발자에게 문의하세요", color=0x25DFE4)
	embed.add_field(name='소스코드를 9', value='이 봇의 모든 소스코드는 오픈소스로 제공되고 있으며, 누구나 소스코드를 절차 없이 확인할 수 있습니다.\nhttps://github.com/SimSimi33/newbot', inline=True)
	embed.set_thumbnail(url=mch.guild.me.avatar_url)
	await mch.send(embed = embed)

@client.event
async def on_message(message):
	msg = message.content.split(" ")
	tomsg = message.content.upper()
	nomsg = message.content
	user = message.author
	mch = message.channel
	server = message.guild
	botver = "Alpha 2.0.3"
	print("%s#%s" % (user.name, str(user.discriminator)))
	print(nomsg)
	if server.id == 697960788945666139:
		vtxt = open("Specialinfo.txt", "r").readlines()
		botname = vtext[0]
	else:
		botname = 'NBot'
	if message.author == client.user:
		return
	elif message.guild == None:
		await mch.send(mch, "Sorry, please use Sbot in Discord server instead of DM or PM.")
		return
	elif re.compile("^s! *(hello|hi)", re.I).search(tomsg):
		if user.nick == None:
			await mch.send("Hello, %s!" % user.name)
		else:
			await mch.send("Hello, %s!" % user.nick)
	elif re.compile("^s! *myinfo", re.I).search(tomsg):
		await myinfo(user, mch)
	elif re.compile("^s! *serverinfo", re.I).search(tomsg):
		await serverinfo(server, mch)
	elif re.compile("^s! *help", re.I).search(tomsg):
		await helpp(mch)
	elif re.compile("^s! *source", re.I).search(tomsg):
		await source(mch)
	elif re.compile("^s! *(info|botinfo)", re.I).search(tomsg):
		verinfo = '%s %s' % (botname, botver)
		await mch.send('이 봇은 심늣이 (코딩 공부를 하기 위해) 개발하고 있는 봇입니다.\n여러분의 꾸준한 피드백과 기능 추가 요청 부탁드립니다!\n%s' % verinfo)
	elif re.compile("^s! *serverinfo", re.I).search(tomsg):
		await date(server, mch)

client.run("token")
