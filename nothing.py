from twitchbot import Command

from twitchbot import BaseBot

if __name__ == '__main__':
    BaseBot().run()

@Command('COMMAND_NAME')
async def cmd_function(msg, *args):
    await msg.reply('i was called!')