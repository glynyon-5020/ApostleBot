import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member

class Experience(commands.Cog):
    def __init__(self, client):
        self.client = client

    test_server_id = 820053634598567984

    @nextcord.slash_command(name="hello", description="My first application Command", guild_ids=[test_server_id])
    async def test(self, interaction: Interaction):
        await interaction.response.send_message("Hello!")

    @nextcord.slash_command(name="addxp", description="Adds experience to your character.", guild_ids=[test_server_id])
    async def add_experience(self, interaction: Interaction, member: Member, experience: int):
        await interaction.response.send_message(f"Adds {experience}xp to {member}!")
        

    @nextcord.slash_command(name="removexp", description="Removes experience from your character.", guild_ids=[test_server_id])
    async def remove_experience(self, interaction: Interaction, member: Member, experience: int):
        await interaction.response.send_message(f"Removes {experience}xp from {member}!")


def setup(client):
    client.add_cog(Experience(client))

