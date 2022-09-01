from vkbottle import API
from vk_user import VkUser, user_vk
import configparser
# import asyncio


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


async def top_3_photos(option_id: int) -> list:
    """
    Returns 3 photos with most amount of likes
    :param: option_id: vk user id.
    :return: top profile photos
    """
 
    photos = await api.photos.get(owner_id=option_id, album_id='profile', extended=1)  
    photos_list = photos.items      
    photos_list.sort(key=lambda x: x.likes.count) 
    photos_list = photos_list[-3:]

    top_photos_list = []  
    for photo in photos_list:      
        top_photos_list.append(f'photo{photo.owner_id}_{photo.id}')    
   
    return top_photos_list 


async def search_options(vk_user: VkUser) -> list:
    """
    Searches options.
    :param: vk_user: VkUser
    :return: list of options
    """  
   
    if vk_user.gender == 2:                        
        gender = 1                               
    elif vk_user.gender == 1:
        gender = 2
    else:
        gender = 0 
   
    options = await api.users.search(city=vk_user.city, sex=gender, age_from = vk_user.age_from, age_to = vk_user.age_to, status = 6, count = 100, offset=vk_user.offset)
    vk_user.offset += 100
    options = options.items   
    
    return [option for option in options if not option.is_closed]  


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