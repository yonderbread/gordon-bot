import os
import discord
import youtube_dl


class Client(discord.Client):
    def __init__(self,
                 status_message: str = "killing headcrabs",
                 status_mode: discord.Status = discord.Status.dnd,
                 *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self._status_mode = status_mode
        self._status_message = status_message

    async def on_ready(self):
        print('Bot ready.')
        await self.change_presence(status=self._status_mode, activity=discord.Game(self._status_message))


if __name__ == '__main__':
    bot = Client()
    bot.run(os.environ.get('DISCORD_TOKEN'))
