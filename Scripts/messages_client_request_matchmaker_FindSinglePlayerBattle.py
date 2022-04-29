import asyncio
from vbr_protocol.messages.client.push.matchmaker import Config

from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from vbr_protocol.messages.client.push.matchmaker import Config
from vbr_protocol.deserializers import deserialize_data


# Fetch all pushes client should receive by default and print to console
async def fetch_pushes(game_client: GameClient):    # this fetch_pushes is customized for current check on meta-server 0.28.2. For later versions other code is implemented  
    while True:
        push = deserialize_data(await game_client.pushes.get())
        if isinstance(push, Config):
            game_client.matchmaker._config = push
        print(f"Push received (client: {game_client.email}): {push}")


async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:  # start GC with credentials
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))                # run fetch_pushes task
        await asyncio.sleep(1)
        await game_client.matchmaker.find_single_player_battle("Deathmatch2")             # search for battle with mm_type GROUP_TRAINING (arena is found, arena presets come)
        await asyncio.sleep(10)
        await game_client.matchmaker.find_single_player_battle("Deathmatch1")             # search for battle with mm_type TEAMS after previous battle finished
        await asyncio.sleep(5)
        fetch_pushes_task.cancel()                                                        # cancel fetch_pushes task
    await asyncio.sleep(0.1)
    
if __name__ == "__main__":
    asyncio.run(main())

# messages.arena.request.Start is processed inside this request with info in Server Logs
# mm_type TEAMS
# async def main():
    # async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        # print(await game_client.state.get_update_push())
        # await game_client.matchmaker.wait_for_initial_config()
        # await game_client.matchmaker.find_single_player_battle('Deathmatch1')
        # print(await game_client.state.get_update_push())
        # print(await game_client.matchmaker.get_queue_status_push())
    # await asyncio.sleep(3)


# # mm_type GROUP_TRAINING
# async def main():
    # async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        # print(await game_client.state.get_update_push())
        # await game_client.matchmaker.wait_for_initial_config()
        # await game_client.matchmaker.find_single_player_battle('Deathmatch2')
        # print(await game_client.state.get_update_push())
        # print(await game_client.state.get_update_push())
    # await asyncio.sleep(3)


# if __name__ == "__main__":
    # event_loop = asyncio.get_event_loop()
    # try:
        # event_loop.run_until_complete(main())
    # finally:
        # event_loop.close()
