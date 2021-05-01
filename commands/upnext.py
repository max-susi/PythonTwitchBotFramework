from twitchbot import Command
import os

@Command('upnext')
async def cmd_function(msg, *args):
    #print(getNameOfTopEntryInList.getIdForList("UP NEXT"))
    next = os.popen("cd  commands/redeem-bot && python3 getNameOfTopEntryInList.py").read()
    await msg.reply("upnext: " + next)