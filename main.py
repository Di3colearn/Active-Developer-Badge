import disnake
from disnake.ext import commands


TOKEN = input("Enter Your Token Here : ")

bot = commands.Bot()


@bot.event
async def on_ready():
  print(
    f"OK.\n I login into {bot.user.name} \n Add bot in your server and use /hello command \n\n Invite Link : https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands"
  )


@bot.slash_command()
async def hello(inter):
  await inter.response.send_message("Hi !")


bot.run(TOKEN)
