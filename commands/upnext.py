from twitchbot import Command
import os

@Command('upnext')
async def cmd_function(msg, *args):
    #print(getNameOfTopEntryInList.getIdForList("UP NEXT"))
    next = os.popen("cd  commands/redeem_bot && python getNameOfTopEntryInList.py").read()
    await msg.reply("upnext: " + next)