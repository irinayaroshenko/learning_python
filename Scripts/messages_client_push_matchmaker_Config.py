import asyncio

from system_tests.vbr_game_client import VBRGameClient as GameClient


async def main():
    async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
        print(await game_client.matchmaker.get_config_push())
    await asyncio.sleep(3)

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
