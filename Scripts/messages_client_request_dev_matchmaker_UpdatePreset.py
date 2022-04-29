import asyncio
from vbr_protocol.messages.client.push.matchmaker import Config

from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from system_tests.utils import get_mm_config, set_mm_config
from vbr_protocol.deserializers import deserialize_data


# For script correct run you need to change any preset parameter value EACH TIME !!!
async def fetch_pushes(game_client: GameClient):
    while True:
        push = deserialize_data(await game_client.pushes.get())
        if isinstance(push, Config):
            game_client.matchmaker._config = push
        print(f"Push received (client: {game_client.email}): {push}")


async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
        await asyncio.sleep(1)
        preset = await game_client.matchmaker.get_preset('Deathmatch1')
        preset.game_mode = 1
        preset.num_teams = 8
        preset.team_size = 4
        preset.map_name = '/Game/Maps/Arenas/03_DeathMatchArena_P'
        preset.matchmaking_type = 1

        await game_client.matchmaker.update_preset('Deathmatch1', preset)
        print("----GetPreset request on Updated Preset---")
        await asyncio.sleep(5)
        fetch_pushes_task.cancel()
    await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())



# async def main():
    # async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        # await game_client.matchmaker.wait_for_initial_config()
        # # currently we can update 2 presets: 'Deathmatch1' and 'Deathmatch2'
        # preset = await game_client.matchmaker.get_preset('Deathmatch1')
# #        print(preset.game_mode)   # we can check each preset component separatly, e.g. print(preset.num_teams))
        # preset.game_mode = 1       # parameters value you can check in meta-server\meta-server\init\arenas.yaml
        # preset.num_teams = 5
        # preset.team_size = 10
        # preset.map_name = '/Game/Maps/Arenas/04_DeathMatchArena_P'
        # preset.matchmaking_type = 1
# #        print(preset.num_teams, preset.team_size)

        # await game_client.matchmaker.update_preset('Deathmatch1', preset)
        # print("----Config Push on Updated Preset----")
        # print(await game_client.matchmaker.get_config_push())
        # print("----GetPreset request on Updated Preset----")
        # new_preset = await game_client.matchmaker.get_preset('Deathmatch1')
        # print(new_preset)
        # print("***** Reconnect *****")
        # game_client.close()
        # async with GameClient(email="testlogin8@test.iv", password="123456") as game_client_reconnected:
            # await game_client_reconnected.matchmaker.wait_for_initial_config()
            # preset = await game_client_reconnected.matchmaker.get_preset('Deathmatch1')
            # print("------GetPreset request check------")
            # print(preset)
            # print("------Config Check------")
            # config = game_client.matchmaker.config
            # print(config)
    # await asyncio.sleep(3)

# UpdatePreset for Deathmatch2
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         await game_client.matchmaker.wait_for_initial_config()
#         preset = await game_client.matchmaker.get_preset('Deathmatch2')
#         preset.game_mode = 1
#         preset.num_teams = 1
#         preset.team_size = 4
#         preset.map_name = '/Game/Maps/Arenas/03_DeathMatchArena_P'
#         preset.matchmaking_type = 2
#
#         await game_client.matchmaker.update_preset('Deathmatch2', preset)
#         print("----Config Push on Updated Preset----")
#         print(await game_client.matchmaker.get_config_push())
#         print("----GetPreset request on Updated Preset---")
#         updated_preset = await game_client.matchmaker.get_preset('Deathmatch2')
#         print(updated_preset)
#         print("***** Client Reconnect *****")
#         game_client.close()
#         async with GameClient(email="testlogin7@test.iv", password="123456") as game_client_reconnected:
#             await game_client_reconnected.matchmaker.wait_for_initial_config()
#             preset = await game_client_reconnected.matchmaker.get_preset('Deathmatch2')
#             print("------GetPreset request check------")
#             print(preset)
#             print("------Config Check------")
#             config = game_client.matchmaker.config
#             print(config)
#     await asyncio.sleep(3)

# if __name__ == "__main__":
    # event_loop = asyncio.get_event_loop()
    # try:
        # event_loop.run_until_complete(main())
    # finally:
        # event_loop.close()
