import asyncio
from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME

# We always can start from observing client structure to find needed component
print(dir(client))   # get everything what is present in client. Than we take piece from there and put further
print(dir(game_client))  # or game_client. It depends how you call
print(dir(client.matchmaker))  # get everything that is in matchmaker. Than we take piece from there and put further
print(dir(client.matchmaker.get_config_push))
print(dir(game_client.state))

current_client_status = await  game_client.state.get_update_push()   # get current client status
         print(current_client_status)

# Now we can use print function to get data which config_pus contains
print(await client.matchmaker.get_config_push())

# wait_for_initial_config    this is "obertka" for system_tests

# messages.client.push.matchmaker.Config
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         print(await game_client.matchmaker.get_config_push())
#     await asyncio.sleep(3)

# Get client status in Lobby, in mm, in arena
# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         current_client_status = await game_client.state.get_update_push()
#         print(current_client_status)
#         await game_client.matchmaker.wait_for_initial_config()
#         await game_client.matchmaker.find_single_player_battle(TEAMS_PRESET_NAME)
#         current_client_status = await game_client.state.get_update_push()
#         print(current_client_status)
#         current_client_status = await game_client.state.get_update_push()
#         print(current_client_status)
#     await asyncio.sleep(3)

# Get Queue Status
async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        print(await game_client.state.get_update_push())
        await game_client.matchmaker.wait_for_initial_config()
        await game_client.matchmaker.find_single_player_battle(TEAMS_PRESET_NAME)
        print(await game_client.state.get_update_push())
        print(await game_client.matchmaker.get_queue_status_push())
    await asyncio.sleep(3)

async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        config = await game_client.matchmaker.get_config_push()
        print(config)
    await asyncio.sleep(3)

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()