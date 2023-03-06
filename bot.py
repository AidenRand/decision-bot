import discord
import discord.client
import responses

async def print_response(message, user_message, is_private):
    try:
        response = responses.make_game_response(user_message)

        if (is_private):
            await message.author.send(response)
        else:
            await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA4MjMyMjIyOTQ2MDc0MjE1NA.GurKZA.xhYE9OYaJEoQ_mqUcdDhErndZ2QvvVxfc-v6D4'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        # respond to the use through pm if ? inputted
        if user_message[0] == '?':
            user_message = user_message[1:]
            await print_response(message, user_message, is_private=True)
        else:
            await print_response(message, user_message, is_private=False)

    client.run(TOKEN)