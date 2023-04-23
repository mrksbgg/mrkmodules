# 🔒 The GPL-3.0 license
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# ⠄⠄⠄⠄⡠⣿⢷⣻⣿⣾⣳⡇⢺⠟⠒⠒⠶⢤⣈⠃⢠⡀
# ⠄⠄⠄⢀⣼⡿⠋⢉⣉⣙⠿⠁⢁⣤⣤⣄⡀⠄⠈⠳⢾⣿⣄
# ⠄⠄⠄⢞⡞⠄⣴⣿⡿⠛⠓⠄⠉⠉⠉⠉⠹⣷⣄⠄⠄⠙⢿⣦
# ⠄⢀⣾⡟⠄⣸⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⡀⠄⠰⣿⣆
# ⠄⢸⣿⠁⢸⣿⠄⠄⢸⢸⠄⠄⠄⢸⣆⢠⣀⡀⣧⣨⣻⡀⠄⢻⣿⣦⣀
# ⠄⢸⡇⡀⠘⣿⢰⣐⢾⢿⡀⠄⡀⢨⣎⣻⣷⣶⣿⣿⣿⣇⢀⢸⣿⣿⣿⣷
# ⠄⢸⣣⡇⣧⣿⣿⣿⣿⡎⢳⣟⠿⣿⣿⣏⣉⣿⣿⣿⢻⣿⣿⣾⣿⣿⣿⣿⣦
# ⠄⠄⢼⡇⢹⣿⡏⢠⣿⣿⠄⠉⠄⠄⠈⠄⢹⣿⠟⠼⢻⣿⣿⣿⣿⣿⣿⣿⣿
# ⠄⠄⠈⢿⢈⣿⡛⠘⣿⡇⠄⠄⡀⠄⠄⠄⠈⠉⠁⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿
# ⠄⠄⢀⣿⣼⡿⣿⣀⠄⠄⠄⠄⠃⠄⠄⠄⠄⠄⠄⠘⣻⡏⣿⣿⢻⣿⣿⣿⣿
# ⠄⠄⠾⢻⡇⣿⣸⣦⣀⠄⠄⠐⢟⠙⢻⠃⠄⠄⠄⣾⡏⣷⢻⡹⡟⣿⣿⡟⢿
# ⠄⢀⡴⢻⣇⢿⣷⢻⡟⠻⣶⣤⣀⠉⠄⣀⣴⡿⢣⡟⠄⣿⢸⡇⣰⡟⠻⠃⢸
# ⢠⡏⠄⠄⠈⠻⣿⣏⣷⠄⠈⠻⠉⠛⠛⠉⠄⠄⢛⠄⠄⠻⢠⠁⢛⠁⠄⠄⢸
# ⣼⠄⠄⠄⠄⠄⠈⢿⡘⠃⠄⠄⠄⠄⠄⠄⠠⠈⠄⠄⠄⢠⣸⣠⡞⠄⠄⠄⣿
# ⣤⠄⠄⠄⠄⠄⠄⢸⣇⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⠟⠄⠄⠄⣸⣿
#
# 👾 Module for Telethon User Bot (Netfoll, Hikka, FTG)
# 🔒 The GPL-3.0 license
# ⚠️ Owner @mrkmods
# All rights reserved > @mrkmods
# ---------------------------------------------------------------------------------
# meta developer: @mrkmods
# meta description: Dupes ruble after every use


from telethon.tl.types import Message
from .. import loader, utils
from time import sleep

__version__ = (0, 0, 1)

@loader.tds
class AuroraDuper(loader.Module):
    """Duping rubles in @aurorasms_bot"""
    
    strings = {
        "name": "AuroraDuper",
        "duped": "😏 Succesfully duped a ruble!",
        "started": "😏 Started duping",
        "toomany": "🤨 Hey! You trying to dupe more than a 50 rubles! I think this is a bad idea, please, enter lesser number..."
    }
    
    strings_ru = {
        "name": "AuroraDuper",
        "duped": "😏 Успешно дюпнул рубль!",
        "started": "😏 Начал дюп",
        "toomany": "🤨 Хей! Ты пытаешься дюпнуть больше 50 рублей! Я думаю это плохая идея, пожалуйста, введи число поменьше..."
    }
    
    async def dupecmd(self, message: Message):
        """- dupe"""
        async with self._client.conversation("@aurorasms_bot") as conv:
            n = utils.get_args_raw(message)
            if str(n).isdigit():
                while n > str(0):
                    if n > str(50):
                        await utils.answer(message, self.strings("toomany"))
                    else:
                        await conv.send_message("/start")
                        await utils.answer(message, self.strings("started"))
                        sleep(0.3)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(0)
                        sleep(0.5)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(0)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(2)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(5)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(2)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(0)
                        sleep(30)
                        messages = await self._client.get_messages("aurorasms_bot")
                        await messages[0].click(0)
                        await self.inline.bot.send_message(self._client.tg_id, self.strings("duped"))
                        n -= str(1)
            else:
                await utils.answer(message, f'😒 Enter number, moron...')
