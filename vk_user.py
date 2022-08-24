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
        self.option_list = []
        self.offset = 0

    def searching_parameters(self) -> list:
        """
        Determines parameters for searching
        :return: list of parameters [city, gender, age_from, age_to]
        """
        ...

    def extend_option_list(self, options: list):
        """
        Adds more options to self.option_list
        :param options: list of new options
        :return:
        """
        ...

    def next_option(self):
        """
        Gives next option.
        :return: option
        """
        ...

    def add_favorite(self):
        """
        Adds option to favorites
        """
        ...

    def show_favorites(self):
        """
        Shows list of favorites options
        """
        ...

