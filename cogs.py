import discord
from discord.ext import commands
import sqlite3

# Connection to db file
con = sqlite3.connect("test.db")
cur = con.cursor()

class Information(commands.Cog, name="Information"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="**Tyndale**", description="A Theological Dictionary Bot \n\n**Author:** [DeeDeeAich](https://github.com/DeeDeeAich) \n**Repository:** [Link](https://github.com/DeeDeeAich/tyndale-bot) \n**Bot Created:** September 5, 2021 \n\n*Therefore, since we are surrounded by so great a cloud of witnesses, let us also lay aside every weight, and sin which clings so closely, and let us run with endurance the race that is set before us, looking to Jesus, the founder and perfecter of our faith, who for the joy that was set before him endured the cross, despising the shame, and is seated at the right hand of the throne of God.* (Hebrews 12:1-2)")
        embed.set_footer(text="Tyndale Bot | v0.1", icon_url="https://cdn.discordapp.com/avatars/883461136098406400/1635532c169bd66012115ccb19d7aef8.png?size=256")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! ``{latency}ms``")
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", inline=False)

        embed.add_field(name=":question: **Bot Information**", value="``info`` \nShows information about the bot's creation, creator, links, and other basic info. \n``ping`` \nShows the bot's latency.")
        embed.add_field(name=":book: **Main Commands**", value="``define`` \nShows the definition for a user-specified term. (Aliases: def, definition)")
        embed.set_author(name="Tyndale Bot", icon_url="https://cdn.discordapp.com/avatars/883461136098406400/1635532c169bd66012115ccb19d7aef8.png?size=256")
        embed.set_footer(text="Soli Deo Gloria ❤️")

        await ctx.send(embed=embed)

class MainCommands(commands.Cog, name="Main"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["def", "define"])
    async def definition(self, ctx, *, term):
        # Searches for user-specified term in database
        title = cur.execute(f"SELECT * FROM Definitions WHERE Term LIKE \'{term}\'").fetchall()[0][0]
        definition = cur.execute(f"SELECT * FROM Definitions WHERE Term LIKE \'{term}\'").fetchall()[0][1]

        # These replace the term variable's spaces with the appropriate chars for the url; might need to be cleaned up later
        monergism = term.replace(" ", "+")
        wikipedia = term.replace(" ", "_")
        theopedia = term.replace(" ", "-")

        embed = discord.Embed(title=f"**{title}**", description=f"{definition} \n\n__Links:__ \n[Monergism](https://www.monergism.com/search?keywords={monergism}&format=All) \n[Theopedia](https://www.theopedia.com/{theopedia}) \n[Wikipedia](https://en.wikipedia.org/wiki/{wikipedia})")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Information(bot))
    bot.add_cog(MainCommands(bot))