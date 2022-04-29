import asyncio

from vbr_protocol.deserializers import deserialize_data

from system_tests.constants import GROUP_TRAINING_PRESET_NAME
from system_tests.vbr_game_client import VBRGameClient as GameClient


async def fetch_pushes(game_client: GameClient):
    while True:
        push = deserialize_data(await game_client.pushes.get())
        await game_client.on_push_received(push)
        print(f"Push received (client: {game_client.email}): {push}")


async def main():
    async with create_game_client(email="testlogin1@test.iv") as game_client:
        print("************Player1 Login**************")
        config = await game_client.matchmaker.get_config_push()
        print(config)
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
        await asyncio.sleep(0.5)
        preset_config = config.presets[BR_HARD_AI_PRESET_NAME]
        preset_config.teams_layouts[0].weight = 1
        preset_config.teams_layouts[1].weight = 100
        await game_client.matchmaker.update_preset(BR_HARD_AI_PRESET_NAME, preset_config)
        await asyncio.sleep(1)
        async with create_game_client(email="testlogin2@test.iv") as second_client:
            print("************Player2 Login**************")
            fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
            await asyncio.sleep(0.5)
            print("************Player1 Find Game**************")
            await game_client.matchmaker.find_single_player_battle("Spies")
            await asyncio.sleep(0.1)
            print("************Player2 Find Game**************")
            await second_client.matchmaker.find_single_player_battle("Spies")
            await asyncio.sleep(3)
            await game_client.matchmaker.force_battle(BR_HARD_AI_PRESET_NAME)
            await asyncio.sleep(6)
            fetch_pushes_task.cancel()
            fetch_pushes_task_2.cancel()
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
