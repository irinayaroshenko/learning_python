import asyncio

from accord_test_utils.helpers import random_email

from vbr_protocol.deserializers import deserialize_data
from vbr_protocol.objects.common import Hero, VehicleType
from vbr_protocol.objects.matchmaker import LayoutInfo

from constants import (
    BR_EASY_AI_PRESET_NAME,
    BR_HARD_AI_PRESET_NAME,
    DEATHMATCH_SINGLE_PRESET_NAME,
    SPIES_PRESET_NAME
)
# from system_tests.utils import get_arena_config
# from vbr_game_client import ClientError
from system_tests.utils import create_game_client
from vbr_game_client import VBRGameClient as GameClient
# from system_tests.utils import get_mm_config, set_mm_config


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
        preset_config = config.presets["BattleRoyaleHardAI"]
        preset_config.teams_layouts[0].weight = 1
        preset_config.teams_layouts[1].weight = 100
        await game_client.matchmaker.update_preset("BattleRoyaleHardAI", preset_config)
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

# multimode with update_preset configs + force battle
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         config = await game_client.matchmaker.get_config_push()
#         print(config)
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         preset_config = config.presets["BattleRoyaleEasyAI"]
#         preset_config.teams_layouts[0].weight = 1
#         preset_config.teams_layouts[1].weight = 100
#         # preset_config.teams_layouts[0].layout["DeathmatchSingle"] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         # preset_config.teams_layouts[0].layout[GROUP_TRAINING_PRESET_NAME] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         # preset_config.teams_layouts[1].layout["Spies"] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         preset_config.teams_layouts[0].layout = {
#             "BattleRoyaleEasyAI": TeamsLayoutLayoutItem(num_teams=3, team_size=1),
#             "Spies": TeamsLayoutLayoutItem(num_teams=2, team_size=3),
#             "DeathmatchSingle": TeamsLayoutLayoutItem(num_teams=2, team_size=1),
#             "Convoy": TeamsLayoutLayoutItem(num_teams=1, team_size=4)
#         }
#         preset_config.teams_layouts[1].layout = {
#             "BattleRoyaleHardAI": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "Convoy": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "DeathmatchSingle": TeamsLayoutLayoutItem(num_teams=1, team_size=1)
#         }
#         # preset_config.teams_layouts[1].layout[
#         #     "Deathmatch"] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         await game_client.matchmaker.update_preset("BattleRoyaleEasyAI", preset_config)
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as second_client:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as third_client:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(third_client))
#                 await asyncio.sleep(0.5)
#                 async with GameClient(email="testlogin4@test.iv",
#                                       password="123456") as fourth_client:
#                     print("************Player4 Login**************")
#                     fetch_pushes_task_4 = asyncio.create_task(fetch_pushes(fourth_client))
#                     await asyncio.sleep(0.5)
#                     print("************Player1 Find Game**************")
#                     await game_client.matchmaker.find_single_player_battle("DeathmatchSingle")
#                     await asyncio.sleep(0.1)
#                     print("************Player2 Find Game**************")
#                     await second_client.matchmaker.find_single_player_battle("Spies")
#                     await asyncio.sleep(0.5)
#                     print("************Player3 Find Game**************")
#                     await third_client.matchmaker.find_single_player_battle("DeathmatchSingle")
#                     await asyncio.sleep(0.1)
#                     print("************Player4 Find Game**************")
#                     await fourth_client.matchmaker.find_single_player_battle("Convoy")
#                     await asyncio.sleep(0.5)
#                     print("************Force Battle**************")
#                     await fourth_client.matchmaker.force_battle("BattleRoyaleEasyAI")
#                     await asyncio.sleep(6)
#                     fetch_pushes_task.cancel()
#                     fetch_pushes_task_2.cancel()
#                     fetch_pushes_task_3.cancel()
#                     fetch_pushes_task_4.cancel()
#     await asyncio.sleep(1)


# multimode for groups with update_preset configs and change configs in arenas.yaml
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         config = await game_client.matchmaker.get_config_push()
#         print(config)
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         preset_config = config.presets["BattleRoyaleHardAI"]
#         preset_config.teams_layouts[0].weight = 100
#         preset_config.teams_layouts[1].weight = 1
#         # preset_config.teams_layouts[0].layout["DeathmatchSingle"] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         # preset_config.teams_layouts[0].layout[GROUP_TRAINING_PRESET_NAME] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         # preset_config.teams_layouts[1].layout["Spies"] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         preset_config.teams_layouts[0].layout = {
#             "BattleRoyaleEasyAI": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "Spies": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "Deathmatch": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "Convoy": TeamsLayoutLayoutItem(num_teams=1, team_size=1)
#         }
#         preset_config.teams_layouts[1].layout = {
#             "BattleRoyaleHardAI": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "Convoy": TeamsLayoutLayoutItem(num_teams=1, team_size=1),
#             "DeathmatchSingle": TeamsLayoutLayoutItem(num_teams=1, team_size=1)
#         }
#         # preset_config.teams_layouts[1].layout[
#         #     "Deathmatch"] = TeamsLayoutLayoutItem(
#         #     num_teams=1, team_size=1
#         # )
#         await game_client.matchmaker.update_preset("BattleRoyaleHardAI", preset_config)
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as second_client:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as third_client:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(third_client))
#                 await asyncio.sleep(0.5)
#                 async with GameClient(email="testlogin4@test.iv",
#                                       password="123456") as fourth_client:
#                     print("************Player4 Login**************")
#                     fetch_pushes_task_4 = asyncio.create_task(fetch_pushes(fourth_client))
#                     await asyncio.sleep(0.5)
#                     print("************Player1 Create Group**************")
#                     await game_client.groups.create(b"group:group")
#                     await asyncio.sleep(1)
#                     print("************Update Preset Name**************")
#                     await game_client.groups.update_preset_name("BattleRoyaleEasyAI")
#                     await asyncio.sleep(1)
#                     print("************Player2 Create Group**************")
#                     await second_client.groups.create(b"group2:group2")
#                     await asyncio.sleep(1)
#                     print("************Update Preset Name**************")
#                     await second_client.groups.update_preset_name("Deathmatch")
#                     await asyncio.sleep(1)
#                     print("************Player3 Create Group**************")
#                     await third_client.groups.create(b"group3:group3")
#                     await asyncio.sleep(1)
#                     print("************Update Preset Name**************")
#                     await third_client.groups.update_preset_name("Spies")
#                     await asyncio.sleep(1)
#                     print("************Player4 Create Group**************")
#                     await fourth_client.groups.create(b"group4:group4")
#                     await asyncio.sleep(1)
#                     # print("************Send Invite to Player3**************")
#                     # await game_client.groups.send_invite(third_client.account_key)
#                     # await asyncio.sleep(1)
#                     # print("************Player3 Accepts Invite **************")
#                     # await third_client.groups.accept_invite(game_client.account_key)
#                     # await asyncio.sleep(0.5)
#                     # print("************Send Invite to Player2**************")
#                     # await game_client.groups.send_invite(second_client.account_key)
#                     # await asyncio.sleep(1)
#                     # print("************Send Invite to Player4**************")
#                     # await second_client.groups.send_invite(fourth_client.account_key)
#                     # await asyncio.sleep(1)
#                     # print("************Player4 Accepts Invite **************")
#                     # await fourth_client.groups.accept_invite(second_client.account_key)
#                     # await asyncio.sleep(0.5)
#                     # print("************Player2 Accepts Invite **************")
#                     # await second_client.groups.accept_invite(game_client.account_key)
#                     # await asyncio.sleep(0.5)
#                     print("***************SET READY status Player1 ***************")
#                     await game_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player3 ***************")
#                     await third_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     # print("************Update Preset Name**************")
#                     # await second_client.groups.update_preset_name("Spies")
#                     # await asyncio.sleep(0.5)
#                     print("***************SET READY status Player2***************")
#                     await second_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("************Update Preset Name**************")
#                     await fourth_client.groups.update_preset_name("Convoy")
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player4***************")
#                     await fourth_client.groups.set_ready()
#                     await asyncio.sleep(6)
#                     fetch_pushes_task.cancel()
#                     fetch_pushes_task_2.cancel()
#                     fetch_pushes_task_3.cancel()
#                     fetch_pushes_task_4.cancel()
#     await asyncio.sleep(1)


# FindSinglePlayerBattle without update_preset configs
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(game_client2))
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as game_client3:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(game_client3))
#                 await asyncio.sleep(0.5)
#                 async with GameClient(email="testlogin4@test.iv",
#                                       password="123456") as game_client4:
#                     print("************Player4 Login**************")
#                     fetch_pushes_task_4 = asyncio.create_task(fetch_pushes(game_client4))
#                     await asyncio.sleep(0.5)
#                     async with GameClient(email="testlogin5@test.iv",
#                                           password="123456") as game_client5:
#                         print("************Player5 Login**************")
#                         fetch_pushes_task_5 = asyncio.create_task(fetch_pushes(game_client5))
#                         await asyncio.sleep(0.5)
#                         print("************Player1 Find Game**************")
#                         await game_client.matchmaker.find_single_player_battle("Spies")
#                         await asyncio.sleep(0.1)
#                         print("************Player2 Find Game**************")
#                         await game_client2.matchmaker.find_single_player_battle("Spies")
#                         await asyncio.sleep(0.1)
#                         print("************Player3 Find Game**************")
#                         await game_client3.matchmaker.find_single_player_battle("Convoy")
#                         await asyncio.sleep(0.1)
#                         print("************Player4 Find Game**************")
#                         await game_client4.matchmaker.find_single_player_battle("Convoy")
#                         await asyncio.sleep(0.1)
#                         print("************Player5 Find Game**************")
#                         await game_client5.matchmaker.find_single_player_battle("Convoy")
#                         await asyncio.sleep(6)
#                         fetch_pushes_task.cancel()
#                         fetch_pushes_task_2.cancel()
#                         fetch_pushes_task_3.cancel()
#                         fetch_pushes_task_4.cancel()
#                         fetch_pushes_task_5.cancel()
#     await asyncio.sleep(1)

# start_training_battle for groups
# async def main():
#     default_config = await get_mm_config()
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         config = await game_client.matchmaker.get_config_push()
#         print(config)
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         preset_config = config.presets["BattleRoyaleHardAI"]
#         preset_config.teams_layouts[0].weight = 1
#         preset_config.teams_layouts[1].weight = 100
#         await game_client.matchmaker.update_preset("BattleRoyaleHardAI", preset_config)
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as second_client:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as third_client:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(third_client))
#                 await asyncio.sleep(0.5)
#                 async with GameClient(email="testlogin4@test.iv",
#                                       password="123456") as fourth_client:
#                     print("************Player4 Login**************")
#                     fetch_pushes_task_4 = asyncio.create_task(fetch_pushes(fourth_client))
#                     await asyncio.sleep(0.5)
#                     print("************Player1 Create Group**************")
#                     await game_client.groups.create(b"group:group")
#                     await asyncio.sleep(1)
#                     print("************Player2 Create Group**************")
#                     await second_client.groups.create(b"group2:group2")
#                     await asyncio.sleep(1)
#                     # print("************Update Preset Name**************")
#                     # await second_client.groups.update_preset_name("Deathmatch")
#                     # await asyncio.sleep(1)
#                     # print("************Player3 Create Group**************")
#                     # await third_client.groups.create(b"group3:group3")
#                     # await asyncio.sleep(1)
#                     # print("************Update Preset Name**************")
#                     # await third_client.groups.update_preset_name("Spies")
#                     # await asyncio.sleep(1)
#                     # print("************Player4 Create Group**************")
#                     # await fourth_client.groups.create(b"group4:group4")
#                     # await asyncio.sleep(1)
#                     print("************Send Invite to Player3**************")
#                     await game_client.groups.send_invite(third_client.account_key)
#                     await asyncio.sleep(1)
#                     print("************Player3 Accepts Invite **************")
#                     await third_client.groups.accept_invite(game_client.account_key)
#                     await asyncio.sleep(0.5)
#                     # print("************Update Preset Name**************")
#                     # await game_client.groups.update_preset_name("Convoy")
#                     # await asyncio.sleep(1)
#                     # print("************Send Invite to Player2**************")
#                     # await game_client.groups.send_invite(second_client.account_key)
#                     # await asyncio.sleep(1)
#                     # print("************Send Invite to Player4**************")
#                     # await second_client.groups.send_invite(fourth_client.account_key)
#                     # await asyncio.sleep(1)
#                     # print("************Player4 Accepts Invite **************")
#                     # await fourth_client.groups.accept_invite(second_client.account_key)
#                     # await asyncio.sleep(0.5)
#                     # print("************Update Preset Name**************")
#                     # await second_client.groups.update_preset_name("Deathmatch")
#                     # await asyncio.sleep(0.5)
#                     # print("************Player2 Accepts Invite **************")
#                     # await second_client.groups.accept_invite(game_client.account_key)
#                     # await asyncio.sleep(0.5)
#                     print("***************Player1 Update Training Preset Name***************")
#                     await game_client.groups.update_training_main_preset_name(BR_EASY_AI_PRESET_NAME)
#                     await asyncio.sleep(0.5)
#                     # print("***************Player2 Update Training Preset Name***************")
#                     # await second_client.groups.update_training_main_preset_name(
#                     #     BR_HARD_AI_PRESET_NAME)
#                     # await asyncio.sleep(0.5)
#                     print("***************SET READY status Player1 ***************")
#                     await game_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player3 ***************")
#                     await third_client.groups.set_ready()
#                     await asyncio.sleep(6)
#                     # print("***************SET READY status Player2***************")
#                     # await second_client.groups.set_ready()
#                     # await asyncio.sleep(0.5)
#                     # print("************Update Preset Name**************")
#                     # await fourth_client.groups.update_preset_name("Convoy")
#                     # await asyncio.sleep(0.5)
#                     # print("***************SET READY status Player4***************")
#                     # await fourth_client.groups.set_ready()
#                     print("************Update Preset Name**************")
#                     await game_client.groups.update_preset_name(BR_HARD_AI_PRESET_NAME)
#                     await asyncio.sleep(1)
#                     print("***************Player1 Update Training Preset Name***************")
#                     await game_client.groups.update_training_main_preset_name(
#                         BR_HARD_AI_PRESET_NAME)
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player1 ***************")
#                     await game_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player3 ***************")
#                     await third_client.groups.set_ready()
#                     await asyncio.sleep(6)
#                     print("***************SET to None ***************")
#                     await game_client.groups.update_training_main_preset_name(None)
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player1 ***************")
#                     await game_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player3 ***************")
#                     await third_client.groups.set_ready()
#                     await asyncio.sleep(1.5)
#                     print("************Player1 Force Battle**************")
#                     await game_client.groups.force_battle(BR_HARD_AI_PRESET_NAME)
#                     await asyncio.sleep(6)
#                     fetch_pushes_task.cancel()
#                     fetch_pushes_task_2.cancel()
#                     fetch_pushes_task_3.cancel()
#                     fetch_pushes_task_4.cancel()
#     await set_mm_config(default_config)
#     await asyncio.sleep(1)


# Bug 344890
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         await game_client.matchmaker.start_training_battle(
#             "Convoy", BR_EASY_AI_PRESET_NAME
#         )
#         await asyncio.sleep(6)
#         fetch_pushes_task.cancel()
#     await asyncio.sleep(1)

# Bug 345064
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         config = await game_client.matchmaker.get_config_push()
#         print(config)
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         preset_config = config.presets["BattleRoyaleHardAI"]
#         preset_config.teams_layouts[0].weight = 1
#         preset_config.teams_layouts[1].weight = 100
#         await game_client.matchmaker.update_preset("BattleRoyaleHardAI", preset_config)
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as second_client:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
#             await asyncio.sleep(0.5)
#             print("************Player1 Find Game**************")
#             await game_client.matchmaker.find_single_player_battle("Spies")
#             await asyncio.sleep(0.1)
#             print("************Player2 Find Game**************")
#             await second_client.matchmaker.find_single_player_battle("Spies")
#             await asyncio.sleep(3)
#             await game_client.matchmaker.force_battle(GROUP_TRAINING_PRESET_NAME)
#             await asyncio.sleep(6)
#             fetch_pushes_task.cancel()
#             fetch_pushes_task_2.cancel()
#     await asyncio.sleep(1)

# Force Battle for single players
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         print("************Player1 Find Game**************")
#         await game_client.matchmaker.find_single_player_battle(BR_EASY_AI_PRESET_NAME)
#         await asyncio.sleep(1)
#         print("************Player1 Force Battle**************")
#         await game_client.matchmaker.force_battle(BR_EASY_AI_PRESET_NAME)
#         await asyncio.sleep(6)
#         fetch_pushes_task.cancel()
#     await asyncio.sleep(1)

# Force battle for groups
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         config = await game_client.matchmaker.get_config_push()
#         print(config)
#         await asyncio.sleep(0.1)
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         preset_config = config.presets["BattleRoyaleEasyAI"]
#         preset_config.teams_layouts[0].weight = 1
#         preset_config.teams_layouts[1].weight = 100
#         await game_client.matchmaker.update_preset("BattleRoyaleEasyAI", preset_config)
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(game_client2))
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as game_client3:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(game_client3))
#                 await asyncio.sleep(0.5)
#                 async with GameClient(email="testlogin4@test.iv",
#                                       password="123456") as game_client4:
#                     print("************Player4 Login**************")
#                     fetch_pushes_task_4 = asyncio.create_task(fetch_pushes(game_client4))
#                     await asyncio.sleep(0.5)
#                     print("************Player1 Create Group**************")
#                     await game_client.groups.create(b"group:group")
#                     await asyncio.sleep(1)
#                     print("************Update Preset Name**************")
#                     await game_client.groups.update_preset_name("Spies")
#                     await asyncio.sleep(1)
#                     print("************Player2 Create Group**************")
#                     await game_client2.groups.create(b"group2:group2")
#                     await asyncio.sleep(1)
#                     # print("************Player3 Create Group**************")
#                     # await game_client3.groups.create(b"group3:group3")
#                     # await asyncio.sleep(1)
#                     print("************Send Invite to Player3**************")
#                     await game_client.groups.send_invite(game_client3.account_key)
#                     await asyncio.sleep(1)
#                     print("************Player3 Accepts Invite **************")
#                     await game_client3.groups.accept_invite(game_client.account_key)
#                     await asyncio.sleep(0.5)
#                     print("************Send Invite to Player4**************")
#                     await game_client2.groups.send_invite(game_client4.account_key)
#                     await asyncio.sleep(1)
#                     print("************Player4 Accepts Invite **************")
#                     await game_client4.groups.accept_invite(game_client2.account_key)
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player1 ***************")
#                     await game_client.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player3 ***************")
#                     await game_client3.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     # print("************Update Preset Name**************")
#                     # await game_client2.groups.update_preset_name("Spies")
#                     # await asyncio.sleep(0.5)
#                     print("***************SET READY status Player2***************")
#                     await game_client2.groups.set_ready()
#                     await asyncio.sleep(0.5)
#                     print("***************SET READY status Player4***************")
#                     await game_client4.groups.set_ready()
#                     await asyncio.sleep(2)
#                     print("************Player1 Force Battle**************")
#                     await game_client4.groups.force_battle("BattleRoyaleEasyAI")
#                     await asyncio.sleep(6)
#                     fetch_pushes_task.cancel()
#                     fetch_pushes_task_2.cancel()
#                     fetch_pushes_task_3.cancel()
#                     fetch_pushes_task_4.cancel()
#     await asyncio.sleep(1)

# Force Battle multimode
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         config = await game_client.matchmaker.get_config_push()
#         print(config)
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         preset_config = config.presets["BattleRoyaleEasyAI"]
#         preset_config.teams_layouts[0].weight = 1
#         preset_config.teams_layouts[1].weight = 100
#         await game_client.matchmaker.update_preset("BattleRoyaleEasyAI", preset_config)
#         await asyncio.sleep(1)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as second_client:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as third_client:
#                 print("************Player3 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(third_client))
#                 await asyncio.sleep(0.5)
#                 print("************Player1 Find Game**************")
#                 await game_client.matchmaker.find_single_player_battle("Spies")
#                 await asyncio.sleep(0.5)
#                 print("************Player2 Find Game**************")
#                 await second_client.matchmaker.find_single_player_battle("Deathmatch")
#                 await asyncio.sleep(0.5)
#                 print("************Player3 Find Game**************")
#                 await third_client.matchmaker.find_single_player_battle("BattleRoyaleEasyAI")
#                 await asyncio.sleep(0.1)
#                 print("************Force Battle**************")
#                 await third_client.matchmaker.force_battle("Deathmatch")
#                 await asyncio.sleep(0.5)
#                 print("************Force Battle**************")
#                 await second_client.matchmaker.force_battle("BattleRoyaleEasyAI")
#                 # print("************Player4 Find Game**************")
#                 # await fourth_client.matchmaker.find_single_player_battle("Convoy")
#                 await asyncio.sleep(6)
#                 fetch_pushes_task.cancel()
#                 fetch_pushes_task_2.cancel()
#                 fetch_pushes_task_3.cancel()
#     await asyncio.sleep(1)

# Disconnect, Reconnect
# async def main():
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         print("************Player1 Find Game**************")
#         await game_client.matchmaker.find_single_player_battle(BR_EASY_AI_PRESET_NAME)
#         await asyncio.sleep(1)
#         print("************Player1 Disconnect**************")
#         game_client.close()
#         fetch_pushes_task.cancel()
#         await asyncio.sleep(1)
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         print("************Player1 Find Game**************")
#         await game_client.matchmaker.find_single_player_battle(BR_EASY_AI_PRESET_NAME)
#         await asyncio.sleep(1)
#         print("************Player1 Force Battle**************")
#         await game_client.matchmaker.force_battle(BR_EASY_AI_PRESET_NAME)
#         await asyncio.sleep(6)
#         game_client.close()
#         fetch_pushes_task.cancel()
#         await asyncio.sleep(1)
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as second_client:
#             print("************Player2 Login**************")
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(second_client))
#             await asyncio.sleep(0.5)
#             print("************Player1 Create Group**************")
#             await game_client.groups.create(b"group:group")
#             await asyncio.sleep(1)
#             print("************Send Invite to Player3**************")
#             await game_client.groups.send_invite(second_client.account_key)
#             await asyncio.sleep(1)
#             print("************Player2 Accepts Invite **************")
#             await second_client.groups.accept_invite(game_client.account_key)
#             await asyncio.sleep(0.5)
#             print("***************SET READY status Player1 ***************")
#             await game_client.groups.set_ready()
#             await asyncio.sleep(0.5)
#             print("***************SET READY status Player2 ***************")
#             await second_client.groups.set_ready()
#             await asyncio.sleep(1)
#             print("Disconnect")
#             game_client.close()
#             await asyncio.sleep(1)
#             # print("************Player2 Find Game**************")
#             # await second_client.matchmaker.find_single_player_battle(BR_HARD_AI_PRESET_NAME)
#             # await asyncio.sleep(1)
#             print("***************SET READY status Player2 ***************")
#             await second_client.groups.set_ready()
#             await asyncio.sleep(1)
#             print("************Player1 Force Battle**************")
#             await second_client.groups.force_battle(BR_HARD_AI_PRESET_NAME)
#             await asyncio.sleep(6)
#             fetch_pushes_task.cancel()
#             fetch_pushes_task_2.cancel()
#     await asyncio.sleep(1)

# Scenario 1. Single players: find battle, force battle, start training
# async def main():
#     default_config = await get_mm_config()
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         print("************Player1 Find Game**************")
#         await game_client.matchmaker.find_single_player_battle(DEATHMATCH_SINGLE_PRESET_NAME)
#         await asyncio.sleep(6)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
#             print("************Player2 Login**************")
#             config = await game_client2.matchmaker.get_config_push()
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(game_client2))
#             await asyncio.sleep(0.5)
#             preset_config = config.presets[BR_HARD_AI_PRESET_NAME]
#             preset_config.teams_layouts[0].weight = 1
#             preset_config.teams_layouts[1].weight = 100
#             await game_client.matchmaker.update_preset(BR_HARD_AI_PRESET_NAME, preset_config)
#             await asyncio.sleep(1)
#             print("************Player1 Find BR_HARD**************")
#             await game_client.matchmaker.find_single_player_battle(BR_HARD_AI_PRESET_NAME)
#             await asyncio.sleep(0.1)
#             print("************Player2 Find Spies**************")
#             await game_client2.matchmaker.find_single_player_battle(SPIES_PRESET_NAME)
#             await asyncio.sleep(0.5)
#             print("************Force Battle**************")
#             await game_client2.matchmaker.force_battle(BR_HARD_AI_PRESET_NAME)
#             await asyncio.sleep(6)
#             print("************Start Training**************")
#             await game_client.matchmaker.start_training_battle(
#                 BR_EASY_AI_PRESET_NAME, BR_EASY_AI_PRESET_NAME
#             )
#             await asyncio.sleep(0.5)
#             print("************Start Training**************")
#             await game_client2.matchmaker.start_training_battle(
#                 SPIES_PRESET_NAME, BR_EASY_AI_PRESET_NAME
#             )
#             await asyncio.sleep(6)
#             fetch_pushes_task.cancel()
#             fetch_pushes_task_2.cancel()
#     await set_mm_config(default_config)
#     await asyncio.sleep(1)


# Scenario 2
# async def main():
#     default_config = await get_mm_config()
#     async with GameClient(email="testlogin1@test.iv", password="123456") as game_client:
#         print("************Player1 Login**************")
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         await asyncio.sleep(0.5)
#         async with GameClient(email="testlogin2@test.iv", password="123456") as game_client2:
#             print("************Player2 Login**************")
#             config = await game_client2.matchmaker.get_config_push()
#             fetch_pushes_task_2 = asyncio.create_task(fetch_pushes(game_client2))
#             await asyncio.sleep(0.5)
#             preset_config = config.presets[BR_HARD_AI_PRESET_NAME]
#             preset_config2 = config.presets[BR_EASY_AI_PRESET_NAME]  #
#             preset_config.teams_layouts[0].weight = 1
#             preset_config.teams_layouts[1].weight = 100
#             await game_client.matchmaker.update_preset(BR_HARD_AI_PRESET_NAME, preset_config)
#             await asyncio.sleep(1)
#             print("************Player1 Create Group**************")
#             await game_client.groups.create(b"group:group")
#             await asyncio.sleep(1)
#             print("************Send Invite to Player2**************")
#             await game_client.groups.send_invite(game_client2.account_key)
#             await asyncio.sleep(1)
#             print("************Player2 Accepts Invite **************")
#             await game_client2.groups.accept_invite(game_client.account_key)
#             await asyncio.sleep(0.5)
#             print("***************Player1 Update Training Preset Name***************")
#             await game_client.groups.update_training_main_preset_name(BR_EASY_AI_PRESET_NAME)
#             await asyncio.sleep(0.5)
#             print("***************SET READY status Player1 ***************")
#             await game_client.groups.set_ready()
#             await asyncio.sleep(0.5)
#             print("***************SET READY status Player2 ***************")
#             await game_client2.groups.set_ready()
#             await asyncio.sleep(6)
#             print("***************SET to None ***************")
#             await game_client.groups.update_training_main_preset_name(None)
#             await asyncio.sleep(0.5)
#             async with GameClient(email="testlogin3@test.iv", password="123456") as game_client3:
#                 print("************Player1 Login**************")
#                 fetch_pushes_task_3 = asyncio.create_task(fetch_pushes(game_client3))
#                 await asyncio.sleep(0.5)
#                 print("************Player3 Create Group**************")
#                 await game_client3.groups.create(b"group3:group3")
#                 await asyncio.sleep(1)
#                 print("************Update Preset Name**************")
#                 await game_client.groups.update_preset_name(SPIES_PRESET_NAME)
#                 await asyncio.sleep(1)
#                 print("***************SET READY status Player1 ***************")
#                 await game_client.groups.set_ready()
#                 await asyncio.sleep(0.1)
#                 print("***************SET READY status Player2 ***************")
#                 await game_client2.groups.set_ready()
#                 await asyncio.sleep(0.1)
#                 print("************Update Preset Name**************")
#                 await game_client3.groups.update_preset_name(BR_HARD_AI_PRESET_NAME)
#                 await asyncio.sleep(1)
#                 print("***************SET READY status Player3 ***************")
#                 await game_client3.groups.set_ready()
#                 await asyncio.sleep(0.1)
#                 print("************Player1 Force Battle**************")
#                 await game_client2.groups.force_battle(BR_HARD_AI_PRESET_NAME)
#                 await asyncio.sleep(6)
#                 print("Update config")                           #
#                 preset_config2.teams_layouts[1].layout = {                                       #
#                     BR_EASY_AI_PRESET_NAME: TeamsLayoutLayoutItem(num_teams=1, team_size=2),     #
#                     SPIES_PRESET_NAME: TeamsLayoutLayoutItem(num_teams=1, team_size=1)         #
#                 }
#                 await game_client.matchmaker.update_preset(BR_EASY_AI_PRESET_NAME, preset_config2)
#                 await asyncio.sleep(0.1)
#                 print("************Update Preset Name**************")
#                 await game_client.groups.update_preset_name(BR_EASY_AI_PRESET_NAME)
#                 await asyncio.sleep(1)
#                 print("***************SET READY status Player1 ***************")
#                 await game_client.groups.set_ready()
#                 await asyncio.sleep(0.1)
#                 print("***************SET READY status Player2 ***************")
#                 await game_client2.groups.set_ready()
#                 await asyncio.sleep(0.1)
#                 print("************Update Preset Name**************")
#                 await game_client3.groups.update_preset_name(SPIES_PRESET_NAME)
#                 await asyncio.sleep(1)
#                 print("***************SET READY status Player3 ***************")
#                 await game_client3.groups.set_ready()
#                 await asyncio.sleep(6)
#                 fetch_pushes_task.cancel()
#                 fetch_pushes_task_2.cancel()
#                 fetch_pushes_task_3.cancel()
#     await set_mm_config(default_config)
#     await asyncio.sleep(1)

# async def main():
#     async with GameClient(email="testlogin7@test.iv", password="123456") as game_client:
#         fetch_pushes_task = asyncio.create_task(fetch_pushes(game_client))
#         print("await game_client.matchmaker.get_config_push()")
#         await asyncio.sleep(1)
#         fetch_pushes_task.cancel()
#     await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
