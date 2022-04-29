# import asyncio
#
# from vbr_protocol.deserializers import deserialize_data
#
# from system_tests.vbr_game_client import VBRGameClient as GameClient
#
#
# async def fetch_pushes(game_client: GameClient):
#     while True:
#         push = deserialize_data(await game_client.pushes.get())
#         await game_client.on_push_received(push)
#         print(f"Push received (client: {game_client.email}): {push}")
#
#
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client1:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client1))
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
#             print("************Player2 Login**************")
#             fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client2))
#             await asyncio.sleep(1)
#             print("************Player1 Create Group**************")
#             await game_client1.groups.create(b"group:group")
#             await asyncio.sleep(2)
#             print("************Send Invite to Player2**************")
#             await game_client1.groups.send_invite(game_client2.account_key)
#             await asyncio.sleep(3)
#             print("************Player2 Accepts Invite**************")
#             await game_client2.groups.accept_invite(game_client1.account_key)
#             await asyncio.sleep(3)
#             fetch_pushes_task.cancel()
#     await asyncio.sleep(1)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

# VBRM-147
import asyncio

from vbr_protocol.objects.groups import MemberState
from vbr_protocol.deserializers import deserialize_data

from system_tests.constants import GROUP_TRAINING_PRESET_NAME
from system_tests.test_groups import check_member_state_update
from system_tests.utils import send_arena_battle_results
from system_tests.vbr_game_client import VBRGameClient as GameClient
from system_tests.test_groups import get_group_key_from_onlinelist

from jazz_common import Message


# async def fetch_pushes(game_client: GameClient):
#     while True:
#         push = deserialize_data(await game_client.pushes.get())
#         await game_client.on_push_received(push)
#         print(f"Push received (client: {game_client.email}): {push}")
#
#
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client1:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client1))
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
#             print("************Player2 Login**************")
#             fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client2))
#             await asyncio.sleep(1)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as game_client3:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client3))
#                 await asyncio.sleep(1)
#                 async with GameClient(email="testlogin4@test.iv", password="123456") as game_client4:
#                     print("************Player4 Login**************")
#                     fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client4))
#                     await asyncio.sleep(1)
#                     print("************Player1 Create Group**************")
#                     await game_client1.groups.create(b"group:group")
#                     await asyncio.sleep(2)
#                     print("************Send Invite to Player2**************")
#                     await game_client1.groups.send_invite(game_client2.account_key)
#                     await asyncio.sleep(3)
#                     print("************Player2 Accepts Invite**************")
#                     await game_client2.groups.accept_invite(game_client1.account_key)
#                     await asyncio.sleep(3)
#                     print("************Send Invite to Player3**************")
#                     await game_client1.groups.send_invite(game_client3.account_key)
#                     await asyncio.sleep(3)
#                     print("************Player3 Accepts Invite**************")
#                     await game_client3.groups.accept_invite(game_client1.account_key)
#                     await asyncio.sleep(3)
#                     print("************Send Invite to Player4**************")
#                     await game_client1.groups.send_invite(game_client4.account_key)
#                     await asyncio.sleep(3)
#                     print("************Player4 Accepts Invite**************")
#                     await game_client4.groups.accept_invite(game_client1.account_key)
#                     await asyncio.sleep(3)
#                     fetch_pushes_task.cancel()
#     await asyncio.sleep(1)
#
# if __name__ == "__main__":
#     asyncio.run(main())

# VBRM-148
async def fetch_pushes(game_client: GameClient):
    while True:
        push = deserialize_data(await game_client.pushes.get())
        await game_client.on_push_received(push)
        print(f"Push received (client: {game_client.email}): {push}")


async def main():
    async with GameClient(email="testlogin1@test.iv", password="123456") as game_client1:
        print("************Player1 Login**************")
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client1))
        await asyncio.sleep(1)
        async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
            print("************Player2 Login**************")
            fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client2))
            await asyncio.sleep(1)
            async with GameClient(email="testlogin3@test.iv", password="123456") as game_client3:
                print("************Player3 Login**************")
                fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client3))
                await asyncio.sleep(1)
                async with GameClient(email="testlogin4@test.iv", password="123456") as game_client4:
                    print("************Player4 Login**************")
                    fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client4))
                    await asyncio.sleep(1)
                    async with GameClient(email="testlogin5@test.iv",
                                          password="123456") as game_client5:
                        print("************Player5 Login**************")
                        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client5))
                        await asyncio.sleep(1)
                        print("************Player1 Create Group**************")
                        await game_client1.groups.create(b"group:group")
                        await asyncio.sleep(2)
                        print("************Send Invite to Player2**************")
                        await game_client1.groups.send_invite(game_client2.account_key)
                        await asyncio.sleep(3)
                        print("************Player2 Accepts Invite**************")
                        await game_client2.groups.accept_invite(game_client1.account_key)
                        await asyncio.sleep(3)
                        print("************Send Invite to Player3**************")
                        await game_client1.groups.send_invite(game_client3.account_key)
                        await asyncio.sleep(3)
                        print("************Player3 Accepts Invite**************")
                        await game_client3.groups.accept_invite(game_client1.account_key)
                        await asyncio.sleep(3)
                        print("************Send Invite to Player4**************")
                        await game_client1.groups.send_invite(game_client4.account_key)
                        await asyncio.sleep(3)
                        print("************Player4 Accepts Invite**************")
                        await game_client4.groups.accept_invite(game_client1.account_key)
                        await asyncio.sleep(3)
                        print("************Send Invite to Player5**************")
                        await game_client1.groups.send_invite(game_client5.account_key)
                        await asyncio.sleep(5)
                        print("************Player5 Accepts Invite**************")
                        await game_client5.groups.accept_invite(game_client1.account_key)
                        await asyncio.sleep(3)
                        fetch_pushes_task.cancel()
    await asyncio.sleep(1)


# VBRM-150   !!! After execution run same script with preset["preserve_group"] = False to set default value
async def main():
    async with GameClient(email="testlogin1@test.iv", password="123456") as game_client1:
        print("************Player1 Login**************")
        fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client1))
        await asyncio.sleep(1)
        async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
            print("************Player2 Login**************")
            fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client2))
            await asyncio.sleep(1)

            print("***********Get mm_config****************")
            mm_config = await get_mm_config()
            await asyncio.sleep(2)
            for preset in mm_config["presets"].values():
                preset["preserve_group"] = True
            print("***********Set mm_config****************")
            await set_mm_config(mm_config)
            await asyncio.sleep(2)
            print("************Player1 Create Group **************")
            await game_client1.groups.create(b"group:group")
            await asyncio.sleep(2)
            print("************Send Invite to Player2**************")
            await game_client1.groups.send_invite(game_client2.account_key)
            await asyncio.sleep(3)
            print("************Player2 Accepts Invite**************")
            await game_client2.groups.accept_invite(game_client1.account_key)
            await asyncio.sleep(3)
            print("***************SET READY STATUS Player1***************")
            await game_client1.groups.set_ready()
            await asyncio.sleep(2)
            print("***************SET READY STATUS Player2***************")
            await game_client2.groups.set_ready()
            await asyncio.sleep(2)
            print("************Player2 Leave Group **************")
            await game_client2.groups.leave()
            await asyncio.sleep(5)
            fetch_pushes_task.cancel()
    await asyncio.sleep(1)



if __name__ == "__main__":
    asyncio.run(main())
