import asyncio
from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from vbr_protocol.deserializers import deserialize_data

async def fetch_pushes(cl):
    while True:
        print(f"Push received: {deserialize_data(await cl.pushes.get())}")


async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as client:
#    async with GameClient() as client:
        fetch_pushes_task = asyncio.create_task(fetch_pushes(client))
        await asyncio.sleep(1)
        await client.matchmaker.wait_for_initial_config()
        await client.matchmaker.find_single_player_battle('Deathmatch1')
        fetch_pushes_task = asyncio.create_task(fetch_pushes(client))
        await asyncio.sleep(1)
        print(await game_client.state.get_update_push())
        print(await game_client.matchmaker.get_queue_status_push())
        await asyncio.sleep(60)
        client.close()
        async with GameClient(email="testlogin7@test.iv", password="123456") as game_client_reconnected:
            fetch_pushes_task.cancel()
    await asyncio.sleep(3)

# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#     #     await client.inventory.wait_for_initial_inventory() # ask inventory
#    #      await client.inventory.grant_currency("soft", 10) # add 10 currency
#         print(await game_client.state.get_update_push())
#         await game_client.matchmaker.wait_for_initial_config()
#         await game_client.matchmaker.find_single_player_battle('Deathmatch1')
#         print(await game_client.state.get_update_push())
#         print(await game_client.matchmaker.get_queue_status_push())
#         print(await game_client.state.get_update_push())
#     await asyncio.sleep(3)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()

