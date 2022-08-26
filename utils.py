from vkbottle import API
from vk_user import VkUser, user_vk
import configparser
import asyncio


config = configparser.ConfigParser()
config.read('settings.ini')
user_token = config['VK']['user_token']

api = API(token=user_token)


async def search_options(vk_user: VkUser) -> list:
    """
    Searches options.
    :param: vk_user: VkUser
    :return: list of options
    """
    list_of_options = [] 
    vk_user = user_vk
    for options in vk_user.searching_parameters():
        list_of_options.append(options)
    return list_of_options  

standart_options_list = asyncio.run(search_options(VkUser))


async def top_3_photos(option_id: int) -> list:
    """
    Returns 3 photos with most amount of likes
    :param: option_id: vk user id.
    :return: top profile photos
    """

    photos = await api.photos.get_all(owner_id=option_id, count=30, extended=1)
    
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
    
# top_photos = asyncio.run(top_3_photos(1))


async def show_option(vk_user: VkUser) -> list:
    """
    Gives next option from vk_user option_list
    :param vk_user: VkUser
    :return: option [first_name, last_name, link_to_profile, [photos]]
    """
    full_options_search = []
    standart_options = standart_options_list
    add_options = []

    vk_user = user_vk
    for options in vk_user.option_list:
        if options:
            add_options.append(options)
        else:
            break

    full_options_search = [*standart_options, *add_options]

    if full_options_search[1] == 'мужской':
        full_options_search[1] = 2
    elif full_options_search[1] == 'женский':
        full_options_search[1] = 1
    else: 
        full_options_search[1] = 0 

    user_list = []
    
    users = await api.users.search(hometown=full_options_search[0], sex=full_options_search[1], age_from = full_options_search[2], age_to = full_options_search[3], count = 10)
    for user in users.items:
        user_list.append([f'{user.first_name}, {user.last_name}, vk.com/id{user.id}'])
    
    print (user_list) 

show_option_user = asyncio.run(show_option(VkUser))