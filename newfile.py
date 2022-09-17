from rubpy import Rubika
from re import findall
from time import sleep
import asyncio
import sys,time
from time import sleep as S
import  datetime
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
yellow = '\033[93m'
magenta = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
bold = '\033[1m'
underline = '\033[4m'
black='\033[30m'
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./90)
bot = Rubika("cfttoihkuzudgddhzadwqbawyeipmjtk")
channel_guid : str = "c0Ee9X09008b057804dadf8f941e305a"
post_link: str = "https://rubika.ir/ApLoD_0/CHJEFGAAHHEJAGG"
get_infos: list = [] # get post info
links = []

async def main():
	t: bool = False
	while(t != True):
		try:
			message_info: str = await bot.getLinkFromAppUrl(post_link)
			global get_infos
			get_infos.append(message_info['message_id'])
			get_infos.append(message_info['object_guid'])
			t: bool = True
		except:
			t: bool = False

	t: bool = False
	while(t!=True):
		try:
			messages : list = await bot.getMessagesInterval(channel_guid, await bot.getChannelLastMessageId(channel_guid))
			t:bool=True
		except:
			t:bool=False
	for msg in messages:
		try:
			msg = msg['text']
			group_link = findall(r"https://rubika.ir/joing/\w{32}", msg)
			for link in group_link:
				links.append(link)
		except: pass
	
	while(1):
		for link in links:
			sleep(0.0)
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					group_guid:str= await bot.joinGroup(link)
					group_guid: str = group_guid.get('data').get('group').get('group_guid')
					t:bool=True
					
					
					count += 5
				except:
					t:bool=False
					count += 1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
				#	await bot.sendMessage(group_guid, "تبلیغ")
					await bot.forwardMessages(get_infos[1], [get_infos[0]], group_guid)
					print("sended!")
				
					print(green,time.localtime().tm_hour,f'{yellow}',":",white,time.localtime().tm_min,f'{yellow}',":",magenta,time.localtime().tm_sec)
					
					print(cyan+"___________________")
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					await bot.leaveGroup(group_guid)
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1

asyncio.run(main())