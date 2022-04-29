import asyncio
from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from vbr_protocol.deserializers import deserialize_data

async def fetch_pushes(game_client):
    print(f"Push received: {deserialize_data(await game_client.pushes.get())}")
    await asyncio.sleep(0.1)
    asyncio.create_task(fetch_pushes(game_client))

async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        print(await game_client.matchmaker.get_config_push())
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
        await asyncio.sleep(1)
        await game_client.matchmaker.find_single_player_battle('Deathmatch2')
        await asyncio.sleep(10)
    await asyncio.sleep(3)

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
