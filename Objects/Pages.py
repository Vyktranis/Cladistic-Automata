from discord.ext import menus

async def remove_and_readd(ctx, payload):
    message = await ctx.channel.fetch_message(payload.message_id)
    await message.remove_reaction(payload.emoji, payload.member)

class VyktranianMenu(menus.Menu):

    def __init__(self):
        super().__init__(timeout=None)

    async def send_initial_message(self, ctx, channel):
        return await channel.send("Hi, This is a test")

    @menus.button('<:accolade:867969813337743370>')
    async def on_accolade(self, payload):
        await self.message.edit(content="You pressed on the accolade")
        await remove_and_readd(self.ctx, payload)

    @menus.button('<:nonaccolade:867969813220302888>')
    async def on_nonaccolade(self, payload):
        await self.message.edit(content="You pressed on the nonaccolade")
        await remove_and_readd(self.ctx, payload)

    @menus.button('⏹️')
    async def on_stop(self, payload):
        self.stop()