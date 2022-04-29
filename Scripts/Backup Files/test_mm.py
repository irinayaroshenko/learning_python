import asyncio
from vbr_protocol.messages.client.push.matchmaker import Config

from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from system_tests.utils import get_mm_config, set_mm_config
from vbr_protocol.deserializers import deserialize_data

async def fetch_pushes(game_client: GameClient):
    while True:
        push = deserialize_data(await game_client.pushes.get())
        if isinstance(push, Config):
            game_client.matchmaker._config = push
        print(f"Push received (client: {game_client.email}): {push}")


# messages.client.push.matchmaker.Config
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         print(await game_client.matchmaker.get_config_push())
#     await asyncio.sleep(3)

# wait_for_initial_config
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         await game_client.matchmaker.wait_for_initial_config()
#         config = game_client.matchmaker.config
#         print(config)
#     await asyncio.sleep(3)

# messages.client.request.matchmaker.FindSinglePlayerBattle  (messages.arena.request.Start is processed inside this request)
# mm_type TEAMS
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         print(await game_client.state.get_update_push())
#         await game_client.matchmaker.wait_for_initial_config()
#         await game_client.matchmaker.find_single_player_battle('Deathmatch1')
#         print(await game_client.state.get_update_push())
#         print(await game_client.matchmaker.get_queue_status_push())
#     await asyncio.sleep(3)

# mm_type GROUP_TRAINING
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(1)
#         await game_client.matchmaker.find_single_player_battle('Deathmatch2')
#         await asyncio.sleep(10)
#         fetch_pushes_task.cancel()
#     await asyncio.sleep(3)


# messages.client.request.dev.matchmaker.GetPreset
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(1)
#         preset = await game_client.matchmaker.get_preset('Deathmatch2')
#         print(preset)
#         fetch_pushes_task.cancel()
#     await asyncio.sleep(3)

# messages.client.request.dev.matchmaker.UpdatePreset
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
#        print(await game_client.matchmaker.get_config_push())
#        updated_preset = await game_client.matchmaker.get_preset('Deathmatch1')
#        print(updated_preset)
#        print("***** Client Reconnect *****")
        await asyncio.sleep(5)
        fetch_pushes_task.cancel()
#        game_client.close()
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client_reconnected:
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client_reconnected))
#         await asyncio.sleep(1)
#         preset = await game_client_reconnected.matchmaker.get_preset('Deathmatch1')
#         print("------GetPreset request check------")
#         print(preset)
#         print("------Config Check------")
#         config = game_client_reconnected.matchmaker.config
#         print(config)
#         fetch_pushes_task.cancel()
    await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())
