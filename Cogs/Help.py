import discord
from discord.ext import commands


class HelpCommand(commands.HelpCommand):

    async def send_bot_help(self, mapping):
        e = discord.Embed(colour=0xFD8063)
        filtered = await self.filter_commands(self.context.bot.commands, sort=True)
        for command in filtered:
            e.add_field(name=f'{command.name} {command.signature}', value=command.short_doc, inline=False)

        await self.get_destination().send(embed=e)

    async def send_command_help(self, command):
        e = discord.Embed(title=f'{command.qualified_name} {command.signature}', colour=0xFD8063)
        e.description = command.help
        if isinstance(command, commands.Group):
            filtered = await self.filter_commands(command.commands, sort=True)
            for child in filtered:
                e.add_field(name=f'{child.qualified_name} {child.signature}', value=child.short_doc, inline=False)

        await self.get_destination().send(embed=e)

    send_group_help = send_command_help
    