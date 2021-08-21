import discord

class VyktranianMenu(discord.ui.View):

    def __init__(self, user_id, main, medal=None, audit=None):
        super().__init__(timeout=None)
        self.id = user_id
        self.main = main
        self.medal = medal
        self.audit = audit

    @discord.ui.button(label="Profile", emoji="📊")
    async def main(self, button : discord.ui.Button, interaction : discord.Interaction):
        if interaction.user.id == self.id:
            await interaction.message.edit(content='`Viewing cladistic profile.`', embed=self.main)

    @discord.ui.button(label="Medals", emoji="🎖️")
    async def medals(self, button : discord.ui.Button, interaction : discord.Interaction):
        if interaction.user.id == self.id:
            await interaction.message.edit(content='`Viewing cladistic medals.`', embed=self.medal)

    @discord.ui.button(label="Audit", emoji="🔖")
    async def audit(self, button : discord.ui.Button, interaction : discord.Interaction):
        if interaction.user.id == self.id:
            await interaction.message.edit(content='`Viewing cladistic audit.`', embed=self.audit)