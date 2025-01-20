import discord 
import os 
from dotenv import load_dotenv
from geminiMetaData import CHAT_METADATA
import google.generativeai as genai
load_dotenv()



SERVER_GENERAL_CHANNEL =''
SERVER_GENERAL_CHANNEL_ID = 1178674808968446027
GEMINI_TOKEN = os.environ['GEMINI_AUTHENTICATION_TOKEN']
TOKEN = os.environ['TOKEN']

#HMM CLASS BABY 


class Gemini:
    model = None
    def __init__(self):
        genai.configure(api_key=GEMINI_TOKEN)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def chat(self,message):
        if(self.model):
            try:
                response = self.model.generate_content(CHAT_METADATA+message)
            except:
                response =None
            return response.text
        return None


async def which_command(message,author):
    command = message.split(" ")
    if(not len(command)>1):
        return
    message=""
    for i in range(len(command)):
        if(i>1):
            message+=command[i];
        
    if(command[1] == "/chat"):
        response = gemini.chat(message=message)
        if(response):
            await SERVER_GENERAL_CHANNEL.send(response)
        
client = discord.Client(intents=discord.Intents.default())
gemini = Gemini()




@client.event
async def on_ready():
    global SERVER_GENERAL_CHANNEL
    for server in client.guilds:
        for channel in server.channels:
            if(channel.name == 'general'):
                SERVER_GENERAL_CHANNEL=client.get_channel(SERVER_GENERAL_CHANNEL_ID)
        for member in server.members:
            print("members in the server",member);


# if anyone post the message in the server then this willl triggger......
@client.event 
async def on_message(message):
    if(message.content):
        await which_command(message.content,message.author.name);
        
async def sendMessage():
    if(not SERVER_GENERAL_CHANNEL):
        return
    try:
        await SERVER_GENERAL_CHANNEL.send("bhen ke bhai")
    except:
        print("something went wrong!");
        return;
                    

client.run(TOKEN)
