from vkbottle import API
from vk_user import VkUser
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')
user_token = config['VK']['user_token']

api = API(token=user_token)


async def show_option(vk_user: VkUser) -> list:
    """
    Gives next option from vk_user option_list
    :param vk_user: VkUser
    :return: option [first_name, last_name, link_to_profile, [photos]]
    """
    ...


async def search_options(vk_user: VkUser) -> list:
    """
    Searches options.
    :param: vk_user: VkUser
    :return: list of options
    """
    ...


async def top_3_photos(option_id: int) -> list:
    """
    Returns 3 photos with most amount of likes
    :param: option_id: vk user id.
    :return: top profile photos
    """
    ...
