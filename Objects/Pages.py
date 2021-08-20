from discord.ext import menus

async def remove_and_readd(ctx, payload):
    message = await ctx.channel.fetch_message(payload.message_id)
    await message.remove_reaction(payload.emoji, payload.member)

class VyktranianMenu(menus.Menu):

    def __init__(self, main, medal=None, audit=None):
        super().__init__(timeout=None)
        self.main = main
        self.medal = medal
        self.audit = audit

    async def send_initial_message(self, ctx, channel):
        self.id = ctx.author.id
        return await channel.send(content='`Viewing cladistic profile.`',embed=self.main)

    @menus.button('📊')
    async def main(self, payload):
        if payload.user_id == self.id:
            await self.message.edit(content='`Viewing cladistic profile.`', embed=self.main)
        await remove_and_readd(self.ctx, payload)

    @menus.button('🎖️')
    async def medal(self, payload):
        if payload.user_id == self.id:
            await self.message.edit(content="`Viewing cladistic medals.`", embed=self.medal)
        await remove_and_readd(self.ctx, payload)

    @menus.button('🔖')
    async def log(self, payload):
        if payload.user_id == self.id:
            await self.message.edit(content="Bookmark Page", embed=self.audit)
        await remove_and_readd(self.ctx, payload)