from vkbottle import API
from vk_user import VkUser
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')
user_token = config['VK']['user_token']

api = API(token=user_token)


async def get_city_id(city_name: str) -> list:
    """
    Gets cities ids
    :param city_name: name of city
    :return: list of ids that matches to the city_name
    """
    city_id = await api.database.get_cities(country_id=1, q=city_name)
    return city_id.items


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
