import asyncio

from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.constants import TEAMS_PRESET_NAME, GROUP_TRAINING_PRESET_NAME
from system_tests.utils import get_mm_config, set_mm_config

async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        await game_client.matchmaker.wait_for_initial_config()
        # currently we can check 2 presets: 'Deathmatch1' and 'Deathmatch2'
        preset = await game_client.matchmaker.get_preset('Deathmatch1')
        print(preset)
    await asyncio.sleep(3)

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
