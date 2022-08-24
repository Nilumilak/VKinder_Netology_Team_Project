from vkbottle.bot import Bot, Message
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')
group_token = config['VK']['group_token']

group_bot = Bot(token=group_token)


@group_bot.on.message(text='/start')
async def create_user(message: Message):
    """
    Creates VkUser and shows an option.
    :param: message: incoming message from user
    :return:
    """
    ...


@group_bot.on.message(text='/next')
async def next_option(message: Message):
    """
    Shows next option.
    :param: message: incoming message
    :return:
    """
    ...


@group_bot.on.message(text='/add')
def add_favorite(message: Message):
    """
    Saves option to favorites.
    :param: message: incoming message
    :return:
    """
    ...


@group_bot.on.message(text='/show_favorites')
async def show_favorites(message: Message):
    """
    Shows favorites.
    :param message: incoming message
    :return:
    """
    ...


group_bot.run_forever()
