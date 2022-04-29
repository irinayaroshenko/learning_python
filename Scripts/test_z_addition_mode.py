import asyncio
import typing

from accord_test_utils.helpers import random_email

from vbr_protocol.deserializers import deserialize_data
from vbr_protocol.objects.common import Hero, VehicleType
from vbr_protocol.objects.matchmaker import LayoutInfo
from vbr_game_client.game_client import ClientError, Metrics, VBRGameClient

from system_tests.constants import (
    BR_EASY_AI_PRESET_NAME,
    BR_HARD_AI_PRESET_NAME,
    DEATHMATCH_PRESET_NAME,
    SPIES_PRESET_NAME,
)
from system_tests.utils import get_arena_config, send_request_additional_players, \
    create_game_client
from vbr_game_client import ClientError, Metrics, VBRGameClient
from vbr_game_client import VBRGameClient as GameClient
from system_tests.utils import get_mm_config, set_mm_config


async def fetch_pushes(game_client: GameClient):
    while True:
        push = deserialize_data(await game_client.pushes.get())
        await game_client.on_push_received(push)
        print(f"Push received (client: {game_client.email}): {push}")


# Arena request and accept additional players on Training battle
async def main():
    async with create_game_client(email="testlogin1@test.iv") as game_client:
        print("************Player1 Login**************")
        await asyncio.sleep(0.1)
        print(await game_client.get_handshake_push())
        print(await game_client.inventory.get_update_push())
        print(await game_client.state.get_update_push())
        print(await game_client.stats.get_update_push())
        print(await game_client.matchmaker.get_config_push())
        print(await game_client.onlinelist.get_update_push())
        await asyncio.sleep(1)
        print("************Player1 Find Training**************")
        await game_client.matchmaker.start_training_battle(
            BR_HARD_AI_PRESET_NAME, BR_HARD_AI_PRESET_NAME
        )
        print(await game_client.state.get_update_push())
        await asyncio.sleep(0.1)
        print(await game_client.state.get_update_push())
        await asyncio.sleep(0.3)
        prerequisites = await game_client.arena.get_arena_prerequisites_push()
        await send_request_additional_players(
            address=prerequisites.prerequisites.address,
            preset_name="Convoy",
            main_preset_name=BR_HARD_AI_PRESET_NAME,
            request_timeout=30,
            accept_players=True,
            battle_id=prerequisites.prerequisites.battle_id,
            extend_session_duration_for=5,
        )
        await asyncio.sleep(1)
        async with create_game_client(email="testlogin2@test.iv") as game_client2:
            game_client2 = typing.cast(GameClient, game_client2)
            print("************Player2 Login**************")
            print(await game_client2.get_handshake_push())
            print(await game_client2.inventory.get_update_push())
            print(await game_client2.state.get_update_push())
            print(await game_client2.stats.get_update_push())
            print(await game_client2.matchmaker.get_config_push())
            print(await game_client2.onlinelist.get_update_push())
            await asyncio.sleep(1)
            print("************Player2 Find Convoy**************")
            await game_client2.matchmaker.find_single_player_battle("Convoy")
            print(await game_client2.matchmaker.get_queue_status_push())
            print(await game_client2.state.get_update_push())
            await asyncio.sleep(0.1)
            print(await game_client2.state.get_update_push())
            await asyncio.sleep(0.3)
            print("************Player2 Get Prereq**************")
            second_prerequisites = await game_client2.arena.get_arena_prerequisites_push()
            print(second_prerequisites)
            print("************Assert battle_id **************")
            assert (
                prerequisites.prerequisites.battle_id ==
                second_prerequisites.prerequisites.battle_id
            )
            await asyncio.sleep(0.1)
            print("************Get battle results **************")
            print(await game_client2.arena.get_results_push())
            await asyncio.sleep(0.5)
        print(await game_client.arena.get_results_push())
        await asyncio.sleep(1)
    await asyncio.sleep(1)

# Arena request and accept players on find_single_player battle
# async def main():
#     async with create_game_client(email="testlogin1@test.iv") as game_client:
#         print("************Player1 Login**************")
#         await asyncio.sleep(0.1)
#         print(await game_client.get_handshake_push())
#         print(await game_client.inventory.get_update_push())
#         print(await game_client.state.get_update_push())
#         print(await game_client.stats.get_update_push())
#         print(await game_client.matchmaker.get_config_push())
#         print(await game_client.onlinelist.get_update_push())
#         await asyncio.sleep(1)
#         print("************Player1 Create Group**************")
#         await game_client.groups.create(b"group:group")
#         await asyncio.sleep(1)
#         print(await game_client.onlinelist.get_update_push())
#         await asyncio.sleep(1)
#         print("************Update Preset Name**************")
#         await game_client.groups.update_preset_name("Deathmatch")
#         await asyncio.sleep(1)
#         print("***************SET READY status Player1 ***************")
#         await game_client.groups.set_ready()
#         await asyncio.sleep(1)
#         # print("************Player1 Find DEATHMATCH**************")
#         # await game_client.matchmaker.find_single_player_battle("Deathmatch")
#         # await asyncio.sleep(1)
#         # await game_client.matchmaker.start_training_battle(
#         #     BR_HARD_AI_PRESET_NAME, BR_HARD_AI_PRESET_NAME
#         # )
#         print("************Force Battle**************")
#         await game_client.groups.force_battle("Deathmatch")
#         await asyncio.sleep(1)
#         print(await game_client.state.get_update_push())
#         await asyncio.sleep(0.1)
#         print(await game_client.state.get_update_push())
#         await asyncio.sleep(0.3)
#         prerequisites = await game_client.arena.get_arena_prerequisites_push()
#         print(prerequisites)
#         await send_request_additional_players(
#             address=prerequisites.prerequisites.address,
#             preset_name="Convoy",
#             main_preset_name="Deathmatch",
#             request_timeout=30,
#             accept_players=True,
#             battle_id=prerequisites.prerequisites.battle_id,
#             extend_session_duration_for=10,
#         )
#         await asyncio.sleep(1)
#         async with create_game_client(email="testlogin2@test.iv") as game_client2:
#             game_client2 = typing.cast(GameClient, game_client2)
#             print("************Player2 Login**************")
#             print(await game_client2.get_handshake_push())
#             print(await game_client2.inventory.get_update_push())
#             print(await game_client2.state.get_update_push())
#             print(await game_client2.stats.get_update_push())
#             print(await game_client2.matchmaker.get_config_push())
#             print(await game_client2.onlinelist.get_update_push())
#             await asyncio.sleep(1)
#             print("************Player2 Create Group**************")
#             await game_client2.groups.create(b"group2:group2")
#             await asyncio.sleep(1)
#             print(await game_client2.onlinelist.get_update_push())
#             await asyncio.sleep(1)
#             async with create_game_client(email="testlogin3@test.iv") as game_client3:
#                 game_client3 = typing.cast(GameClient, game_client3)
#                 print("************Player3 Login**************")
#                 print(await game_client3.matchmaker.get_config_push())
#                 await asyncio.sleep(0.5)
#                 async with create_game_client(email="testlogin4@test.iv") as game_client4:
#                     game_client4 = typing.cast(GameClient, game_client4)
#                     print("************Player4 Login**************")
#                     print(await game_client4.matchmaker.get_config_push())
#                     await asyncio.sleep(0.5)
#                     print("************Send Invite to Player3**************")
#                     await game_client2.groups.send_invite(game_client3.account_key)
#                     await asyncio.sleep(1)
#                     print("************Player3 Accepts Invite **************")
#                     await game_client3.groups.accept_invite(game_client2.account_key)
#                     await asyncio.sleep(0.5)
#                     print("************Update Preset Name**************")
#                     await game_client2.groups.update_preset_name("Convoy")
#                     await asyncio.sleep(1)
#                     print("***************SET READY status Player2 ***************")
#                     await game_client2.groups.set_ready()
#                     await asyncio.sleep(1)
#                     print("***************SET READY status Player3 ***************")
#                     await game_client3.groups.set_ready()
#                     await asyncio.sleep(2)
#                     # print("************Player2 Find Convoy**************")
#                     # await game_client2.matchmaker.find_single_player_battle("Convoy")
#                     # await asyncio.sleep(1)
#                     # print(await game_client2.matchmaker.get_queue_status_push())
#                     # print(await game_client2.state.get_update_push())
#                     # await asyncio.sleep(0.1)
#                     # print(await game_client2.state.get_update_push())
#                     # await asyncio.sleep(0.3)
#                     # print("************Player2 Get Prereq**************")
#                     # second_prerequisites = await game_client2.arena.get_arena_prerequisites_push()
#                     # print(second_prerequisites)
#                     # print("************Assert battle_id **************")
#                     # assert (
#                     #     prerequisites.prerequisites.battle_id ==
#                     #     second_prerequisites.prerequisites.battle_id
#                     # )
#                     # await asyncio.sleep(0.1)
#                     # print("************Player3 Find Convoy**************")
#                     # await game_client3.matchmaker.find_single_player_battle("Convoy")
#                     # await asyncio.sleep(0.1)
#                     # print(await game_client3.matchmaker.get_queue_status_push())
#                     print(await game_client3.state.get_update_push())
#                     await asyncio.sleep(0.1)
#                     # print(await game_client3.state.get_update_push())
#                     # await asyncio.sleep(0.3)
#                     # print("************Player3 Get Prereq**************")
#                     # third_prerequisites = await game_client3.arena.get_arena_prerequisites_push()
#                     # print(third_prerequisites)
#                     # print("************Assert battle_id **************")
#                     # assert (
#                     #     prerequisites.prerequisites.battle_id ==
#                     #     third_prerequisites.prerequisites.battle_id
#                     # )
#                     # await asyncio.sleep(0.1)
#                     print("************Player4 Find Convoy**************")
#                     await game_client4.matchmaker.find_single_player_battle("Convoy")
#                     await asyncio.sleep(0.1)
#                     # print(await game_client2.state.get_update_push())
#                     # await asyncio.sleep(0.3)
#                     # print("************Player2 Get Prereq**************")
#                     # second_prerequisites = await game_client2.arena.get_arena_prerequisites_push()
#                     # print(second_prerequisites)
#                     # print("************Assert battle_id **************")
#                     # assert (
#                     #     prerequisites.prerequisites.battle_id ==
#                     #     second_prerequisites.prerequisites.battle_id
#                     # )
#                     # await asyncio.sleep(0.3)
#                     # print(await game_client4.matchmaker.get_queue_status_push())
#                     # print(await game_client4.state.get_update_push())
#                     # await asyncio.sleep(0.1)
#                     # print(await game_client4.state.get_update_push())
#                     # await asyncio.sleep(0.3)
#                     # print(await game_client3.state.get_update_push())
#                     # await asyncio.sleep(0.3)
#                     # print("************Player3 Get Prereq**************")
#                     # third_prerequisites = await game_client3.arena.get_arena_prerequisites_push()
#                     # print(third_prerequisites)
#                     # print("************Assert battle_id **************")
#                     # assert (
#                     #     prerequisites.prerequisites.battle_id ==
#                     #     third_prerequisites.prerequisites.battle_id
#                     # )
#                     # await asyncio.sleep(0.3)
#                     # print("************Player4 Get Prereq**************")
#                     # fourth_prerequisites = await game_client4.arena.get_arena_prerequisites_push()
#                     # print(fourth_prerequisites)
#                     # print("************Assert battle_id **************")
#                     # assert (
#                     #     prerequisites.prerequisites.battle_id ==
#                     #     fourth_prerequisites.prerequisites.battle_id
#                     # )
#                     # await asyncio.sleep(0.3)
#                     print("************Get battle results Player 2 **************")
#                     print(await game_client2.arena.get_results_push())
#                     await asyncio.sleep(0.3)
#                     print("************Get battle results Player 3 **************")
#                     print(await game_client3.arena.get_results_push())
#                     await asyncio.sleep(0.3)
#                     print("************Get battle results Player 4 **************")
#                     print(await game_client4.arena.get_results_push())
#                     await asyncio.sleep(0.5)
#         print("************Get battle results Player 1 **************")
#         print(await game_client.arena.get_results_push())
#         await asyncio.sleep(1)
#     await asyncio.sleep(1)

# Arena request and decline additional players
# async def main():
#     async with create_game_client(email="testlogin1@test.iv") as game_client:
#         print("************Player1 Login**************")
#         await asyncio.sleep(0.1)
#         print(await game_client.get_handshake_push())
#         print(await game_client.inventory.get_update_push())
#         print(await game_client.state.get_update_push())
#         print(await game_client.stats.get_update_push())
#         print(await game_client.matchmaker.get_config_push())
#         print(await game_client.onlinelist.get_update_push())
#         await asyncio.sleep(1)
#         print("************Player1 Find Training**************")
#         await game_client.matchmaker.start_training_battle(
#             BR_HARD_AI_PRESET_NAME, BR_HARD_AI_PRESET_NAME
#         )
#         print(await game_client.state.get_update_push())
#         await asyncio.sleep(0.1)
#         print(await game_client.state.get_update_push())
#         await asyncio.sleep(0.3)
#         prerequisites = await game_client.arena.get_arena_prerequisites_push()
#         await send_request_additional_players(
#             address=prerequisites.prerequisites.address,
#             preset_name="Convoy",
#             main_preset_name=BR_HARD_AI_PRESET_NAME,
#             request_timeout=30,
#             accept_players=False,
#             battle_id=prerequisites.prerequisites.battle_id,
#             extend_session_duration_for=5,
#         )
#         await asyncio.sleep(1)
#         async with create_game_client(email="testlogin2@test.iv") as game_client2:
#             game_client2 = typing.cast(GameClient, game_client2)
#             print("************Player2 Login**************")
#             print(await game_client2.get_handshake_push())
#             print(await game_client2.inventory.get_update_push())
#             print(await game_client2.state.get_update_push())
#             print(await game_client2.stats.get_update_push())
#             print(await game_client2.matchmaker.get_config_push())
#             print(await game_client2.onlinelist.get_update_push())
#             await asyncio.sleep(1)
#             print("************Player2 Find Convoy**************")
#             await game_client2.matchmaker.find_single_player_battle("Convoy")
#             print(await game_client2.matchmaker.get_queue_status_push())
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.1)
#             print(await game_client2.matchmaker.get_queue_status_push())
#             await asyncio.sleep(0.3)
#             await game_client2.matchmaker.stop()
#             print("************Player2 Find Deathmatch Single**************")
#             await game_client2.matchmaker.find_single_player_battle(DEATHMATCH_SINGLE_PRESET_NAME)
#             await asyncio.sleep(0.3)
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.1)
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.1)
#             print(await game_client2.arena.get_results_push())
#             await asyncio.sleep(0.1)
#             print(await game_client.arena.get_results_push())
#             await asyncio.sleep(1)
#             print("************Player1 Find Training**************")
#             await game_client.matchmaker.start_training_battle(
#                 BR_HARD_AI_PRESET_NAME, BR_HARD_AI_PRESET_NAME
#             )
#             print(await game_client.state.get_update_push())
#             await asyncio.sleep(0.1)
#             print(await game_client.state.get_update_push())
#             await asyncio.sleep(0.3)
#             prerequisites1 = await game_client.arena.get_arena_prerequisites_push()
#             await send_request_additional_players(
#                 address=prerequisites1.prerequisites.address,
#                 preset_name="Convoy",
#                 main_preset_name=BR_HARD_AI_PRESET_NAME,
#                 request_timeout=30,
#                 accept_players=True,
#                 battle_id=prerequisites1.prerequisites.battle_id,
#                 extend_session_duration_for=5,
#             )
#             await asyncio.sleep(1)
#             print("************Player2 Find Convoy**************")
#             await game_client2.matchmaker.find_single_player_battle("Convoy")
#             print(await game_client2.matchmaker.get_queue_status_push())
#             await asyncio.sleep(0.1)
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.2)
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.1)
#             print(await game_client2.arena.get_results_push())
#             await asyncio.sleep(0.1)
#             print(await game_client.arena.get_results_push())
#             await asyncio.sleep(1)
#         await asyncio.sleep(1)
#     await asyncio.sleep(1)


# async def main():
#     async with create_game_client(email="testlogin1@test.iv") as game_client:
#         print("************Player1 Login**************")
#         await asyncio.sleep(0.1)
#         print(await game_client.get_handshake_push())
#         print(await game_client.inventory.get_update_push())
#         print(await game_client.state.get_update_push())
#         print(await game_client.stats.get_update_push())
#         print(await game_client.matchmaker.get_config_push())
#         print(await game_client.onlinelist.get_update_push())
#         await asyncio.sleep(1)
#         print("************ Player1 Find BR_HARD **************")
#         await game_client.matchmaker.find_single_player_battle(BR_HARD_AI_PRESET_NAME)
#         await asyncio.sleep(1)
#         print("************ Player1 Force Battle **************")
#         await game_client.matchmaker.force_battle(BR_HARD_AI_PRESET_NAME)
#         await asyncio.sleep(0.1)
#         print(await game_client.state.get_update_push())
#         await asyncio.sleep(0.1)
#         print(await game_client.state.get_update_push())
#         await asyncio.sleep(0.3)
#         prerequisites = await game_client.arena.get_arena_prerequisites_push()
#         print("Player 1 prerequisites", prerequisites)
#         await send_request_additional_players(
#             address=prerequisites.prerequisites.address,
#             preset_name="Convoy",
#             main_preset_name=BR_HARD_AI_PRESET_NAME,
#             request_timeout=30,
#             accept_players=False,
#             battle_id=prerequisites.prerequisites.battle_id,
#             extend_session_duration_for=5,
#         )
#         await asyncio.sleep(1)
#         async with create_game_client(email="testlogin2@test.iv") as game_client2:
#             game_client2 = typing.cast(GameClient, game_client2)
#             await asyncio.sleep(0.1)
#             print("************Player2 Login**************")
#             print(await game_client2.get_handshake_push())
#             print(await game_client2.inventory.get_update_push())
#             print(await game_client2.state.get_update_push())
#             print(await game_client2.stats.get_update_push())
#             print(await game_client2.matchmaker.get_config_push())
#             print(await game_client2.onlinelist.get_update_push())
#             await asyncio.sleep(1)
#             print("************Player2 Find Convoy**************")
#             await game_client2.matchmaker.find_single_player_battle("Convoy")
#             print(await game_client2.matchmaker.get_queue_status_push())
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.1)
#             print(await game_client2.matchmaker.get_queue_status_push())
#             await asyncio.sleep(1)
#             print("************ Player2 Stop MM **************")
#             await game_client2.matchmaker.stop()
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.3)
#             print("************ Player1 Battle Results **************")
#             print(await game_client.arena.get_results_push())
#             await asyncio.sleep(1)
#
#             print("************ Player2 Find BR_EASY **************")
#             await game_client2.matchmaker.find_single_player_battle(BR_EASY_AI_PRESET_NAME)
#             await asyncio.sleep(1)
#             print("************ Player2 Force Battle **************")
#             await game_client2.matchmaker.force_battle(BR_EASY_AI_PRESET_NAME)
#             await asyncio.sleep(0.1)
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.2)
#             print(await game_client2.state.get_update_push())
#             await asyncio.sleep(0.1)
#             prerequisites = await game_client2.arena.get_arena_prerequisites_push()
#             await send_request_additional_players(
#                 address=prerequisites.prerequisites.address,
#                 preset_name="Convoy",
#                 main_preset_name=BR_EASY_AI_PRESET_NAME,
#                 request_timeout=30,
#                 accept_players=True,
#                 battle_id=prerequisites.prerequisites.battle_id,
#                 extend_session_duration_for=10,
#             )
#             await asyncio.sleep(0.1)
#             async with create_game_client(email="testlogin3@test.iv") as game_client3:
#                 game_client3 = typing.cast(GameClient, game_client3)
#                 print("************ Player3 Login **************")
#                 print(await game_client3.matchmaker.get_config_push())
#                 await asyncio.sleep(0.5)
#                 async with create_game_client(email="testlogin4@test.iv") as game_client4:
#                     game_client4 = typing.cast(GameClient, game_client4)
#                     print("************ Player4 Login **************")
#                     print(await game_client4.matchmaker.get_config_push())
#                     await asyncio.sleep(0.5)
#                     print("************ Player3 Create Group **************")
#                     await game_client3.groups.create(b"group:group")
#                     await asyncio.sleep(0.5)
#                     print("************ Player3 Invite Player4 **************")
#                     await game_client3.groups.send_invite(game_client4.account_key)
#                     await asyncio.sleep(0.5)
#                     print("************ Player4 Accepts Invite **************")
#                     await game_client4.groups.accept_invite(game_client3.account_key)
#                     await asyncio.sleep(0.5)
#                     print("************ Update Preset Name **************")
#                     await game_client3.groups.update_preset_name("Convoy")
#                     await asyncio.sleep(0.1)
#                     print("*************** SET READY Player3 ***************")
#                     await game_client3.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY Player4 ***************")
#                     await game_client4.groups.set_ready()
#                     await asyncio.sleep(1)
#                     print(await game_client3.state.get_update_push())
#                     await asyncio.sleep(0.1)
#                     print(await game_client4.state.get_update_push())
#                     await asyncio.sleep(0.1)
#                     print("************ Player1 Find Convoy **************")
#                     await game_client.matchmaker.find_single_player_battle("Convoy")
#                     await asyncio.sleep(0.1)
#                     print("************Get battle results Player 2 **************")
#                     print(await game_client2.arena.get_results_push())
#                     await asyncio.sleep(0.3)
#                     print("************Get battle results Player 3 **************")
#                     print(await game_client3.arena.get_results_push())
#                     await asyncio.sleep(0.3)
#                     print("************Get battle results Player 4 **************")
#                     print(await game_client4.arena.get_results_push())
#                     await asyncio.sleep(0.5)
#                     print("************Get battle results Player 1 **************")
#                     print(await game_client.arena.get_results_push())
#                     await asyncio.sleep(1)
#     await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
