# from vkinder_db import add_favorite_to_db, add_photo_to_db, get_favorites

class VkUser:
    user_dict = {}

    def __init__(self, user_id, gender, city):
        """
        :param user_id: user id
        :param gender: gender
        :param city: city
        """
        self.user_id = user_id
        self.gender = gender
        self.city = city
        self.age_from = None
        self.age_to = None
        self.option_list = []
        self.offset = 0

    def extend_option_list(self, options: list):
        """
        Adds more options to self.option_list
        :param options: list of new options
        :return:
        """   
        self.option_list.extend(options) 

    def next_option(self) -> list:
        """
        Gives next option.
        :return: option
        """
        return self.option_list.pop()

    def add_favorite(self):
        """
        Adds option to favorites
        """
        # add_favorite_to_db()
        # add_photo_to_db() 

    def show_favorites(self) -> list:
        """
        Shows list of favorites options
        """
        # return get_favorites()
