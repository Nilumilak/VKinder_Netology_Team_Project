from vkbottle import API
from vk_user import VkUser
import configparser
import asyncio


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
    photos = await api.photos.get_all(owner_id=option_id, count=200, extended=1)
    
    like_list = []
    max_count_like_list = []
    photos_list= []  

    for photo in photos.items:
        like_list.append(photo.likes.count) 

    like_list.sort()
    max_count_like_list += like_list[-3:]

    for photo in photos.items:
        if photo.likes.count in max_count_like_list:
            photos_list.append(f'photo{option_id}_{photo.id}')                   
    return photos_list
    
asyncio.run(top_3_photos(1))