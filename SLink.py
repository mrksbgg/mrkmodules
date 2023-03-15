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
# ⚠️ Owner @mrkmodules
# All rights reserved > @mrkmodules
# ---------------------------------------------------------------------------------
# meta developer: @mrkmodules
# meta description: Makes a search engines link


from telethon.tl.custom import Message


from .. import loader, utils

__version__ = (0, 0, 1)

@loader.tds
class SLinkMod(loader.Module):
    """Makes a search engines link"""

    strings = {
        "name": "SLink"
    }

    async def googlecmd(self, message: Message):
        """- Create a Google Search link"""

        args = utils.get_args_raw(message)
        google = args.replace(' ', '%20')
        await utils.answer(message, f'https://google.com/search?q={google}')
        
    async def yandexcmd(self, message: Message):
        """- Create a Yandex Search link"""

        args = utils.get_args_raw(message)
        yandex = args.replace(' ', '%20')
        await utils.answer(message, f'https://yandex.ru/search/?text={yandex}')

    async def bingcmd(self, message: Message):
        """- Create a Bing Search link"""

        args = utils.get_args_raw(message)
        bing = args.replace(' ', '%20')
        await utils.answer(message, f'https://www.bing.com/search?q={bing}')    
    
    async def youcmd(self, message: Message):
        """- Create a You Search link"""

        args = utils.get_args_raw(message)
        you = args.replace(' ', '%20')
        await utils.answer(message, f'https://you.com/search?q={you}')   
        
    async def ddgcmd(self, message: Message):
        """- Create a DuckDuckGo Search link"""

        args = utils.get_args_raw(message)
        ddg = args.replace(' ', '%20')
        await utils.answer(message, f'https://duckduckgo.com/?q={ddg}') 