from vkbottle import API
from vk_user import VkUser, user_vk
import configparser
# import asyncio


config = configparser.ConfigParser()
config.read('settings.ini')
user_token = config['VK']['user_token']

api = API(token=user_token)


async def top_3_photos(option_id: int) -> list:
    """
    Returns 3 photos with most amount of likes
    :param: option_id: vk user id.
    :return: top profile photos
    """
    photos = await api.photos.get_all(owner_id=option_id)
    photos_count = photos.count 

    offset = 0 
    while offset < photos_count:
        photos = await api.photos.get_all(owner_id=option_id, count=10, offset=offset, extended=1)
        offset += 10 
        photos = photos.items    
    
        like_list = []
        max_count_like_list = []

        for photo in photos:         
            like_list.append(photo.likes.count) 
        like_list.sort()
        max_count_like_list += like_list[-3:]

        top_photos_list= []
        for photo in photos:              
            if photo.likes.count in max_count_like_list:
                top_photos_list.append(f'photo{photo.owner_id}_{photo.id}')
    
        return top_photos_list    


async def search_options(vk_user: VkUser) -> list:
    """
    Searches options.
    :param: vk_user: VkUser
    :return: list of options
    """  
    list_of_options = []

    options = await api.users.search(hometown=vk_user.city, sex=vk_user.gender, age_from = vk_user.age_from, age_to = vk_user.age_to, status = 6, offset=vk_user.offset)
    options_count = options.count    

    if vk_user.gender == 2:                        
        gender = 1                               
    elif vk_user.gender == 1:
        gender = 2
    else:
        gender = 0

    while vk_user.offset < options_count:
        options = await api.users.search(hometown=vk_user.city, sex=gender, age_from = vk_user.age_from, age_to = vk_user.age_to, status = 6, count = 2, offset=vk_user.offset)
        vk_user.offset += 2
        options = options.items 

        list_of_options += [option for option in options if not option.is_closed]
    return list_of_options   


async def show_option(vk_user: VkUser) -> list:
    """
    Gives next option from vk_user option_list
    :param vk_user: VkUser
    :return: option [first_name, last_name, link_to_profile, [photos]]
    """

    if not vk_user.option_list:
        search_result = await search_options(vk_user)
        option_list = search_result
        vk_user.extend_option_list(option_list)
    option = vk_user.next_option()
    photos = await top_3_photos(option.id)
    message = [option.first_name, option.last_name, f'vk.com/id{option.id}', photos]
    return message




# print(asyncio.run(show_option(user_vk)))