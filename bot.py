import discord
import discord.client
import responses

async def print_response(message, user_message, is_private):
    try:
        response = responses.make_response(user_message)

        if (is_private):
            await message.author.send(response)
        else:
            await message.channel.send(response)
    
    except Exception as e:
        print(e)