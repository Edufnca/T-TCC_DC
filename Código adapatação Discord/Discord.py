import discord
import random
import os
class MyClient(discord.Client):
    async def on_ready(self):
        activity = discord.Activity(type=discord.ActivityType.watching, name='12 Homens e Uma Sentença')
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print('A {0} conseguiu logar!'.format(self.user))
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        messa = message.content = message.content.lower()
        if message.content == 'bom dia, <@numerodoBot>':
            await message.channel.send(f'{message.author.name}, bom dia!')
        a = random.randint(1, 3)
        if a == 1:
            await message.channel.send(f'{message.author.name}, bem e tu?')
        elif a == 2:
            await message.channel.send(f'{message.author.name}, mal e tu?')
        elif a == 3:
            await message.channel.send(f'{message.author.name}, normal e tu?')
        elif message.content == 'tudo bem?, <@numerodoBot>':
            a = random.randint(1, 3)
        if a == 1:
            await message.channel.send(f'{message.author.name}, tudo e tu?')
        elif a == 2:
            await message.channel.send(f'{message.author.name}, não muito e tu?')
        elif a == 3:
            await message.channel.send(f'{message.author.name}, acho que sim e tu?')

        elif message.content == 'amém' or message.content == "amem":
            await message.add_reaction(emoji='🛐')
        elif message.content == 'doim':
            await message.add_reaction(emoji='🥜')
        elif message.content == 'dio':
            await message.channel.send('Meu personagem favorito de JoJo :place_of_worship:')
        elif message.content == 'sus':
            await message.add_reaction(emoji='<:sus:940435663541637180>')

        elif message.content == 'como foi o dia de vocês ontem?' or message.content == 'como foi o dia de vcs onti?' or message.content == 'como foi o dia de vcs ontem?' or message.content == 'como foi o dia de cês ontem?':
            await message.add_reaction(emoji='✅')
            await message.add_reaction(emoji='❌')
            await message.add_reaction(emoji='🔀')
            await message.add_reaction(emoji='♾️')
            await message.add_reaction(emoji='<:sus:940435663541637180>')

        elif message.content == 's dado' or message.content == 's dice' or message.content == 's d':
            a = random.randint(1, 6)
            await message.channel.send(f'{message.author.name}, eu rolei os dados e deu {a} 🎲')
        elif message.content == 's anular':
            await message.channel.send('<:anulado:1002323343799750798>')

client = MyClient()
client.run('token')