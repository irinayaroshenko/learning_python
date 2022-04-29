import asyncio
from vbr_protocol.messages.client.push.matchmaker import Config

from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from system_tests.utils import get_mm_config, set_mm_config
from vbr_protocol.deserializers import deserialize_data
from vbr_protocol.objects.groups import MemberState

async def fetch_pushes(game_client: GameClient):
    while True:
        push = deserialize_data(await game_client.pushes.get())
        await game_client.on_push_received(push)
        print(f"Push received (client: {game_client.email}): {push}")

async def main():
    async with GameClient(email="testlogin8@test.iv", password="123456") as game_client:
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
        await asyncio.sleep(1)
        print("***********FIND BATTLE Deathmatch2****************")
        await game_client.matchmaker.find_single_player_battle("Deathmatch2")
        await asyncio.sleep(10)
        print("**********CREATE GROUP*************")
        await game_client.groups.create(b"group:group")
        await asyncio.sleep(3)
        print("******************Change MM_preset to Deathmatch2***************")
        await game_client.groups.update_preset_name("Deathmatch2")
        await asyncio.sleep(1)
        print("***************SET READY STATUS***************")
        await game_client.groups.set_ready()
        await asyncio.sleep(8)
        fetch_pushes_task.cancel()
        await asyncio.sleep(1)
        await asyncio.sleep(1)
    await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())
