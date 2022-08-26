class VkUser:
    user_dict = {}

    def __init__(self, user_id, gender, city, age):
        """
        :param user_id: user id
        :param gender: gender
        :param city: city
        """
        self.user_id = user_id
        self.gender = gender
        self.city = city
        self.age = age
        self.option_list = []
        self.offset = 0

    def searching_parameters(self) -> list:
        """
        Determines parameters for searching
        :return: list of parameters [gender, city, age_from, age_to]
        """
        if self.gender == 'мужской':                        
            gender = 'женский'                               
        elif self.gender == 'женский':
            gender = 'мужской'
        else:
            gender = 'любой'
        city = self.city
        age_from = self.age - 5
        age_to = self.age + 5
        
        return [city, gender, age_from, age_to]

    def extend_option_list(self, options: list):
        """
        Adds more options to self.option_list
        :param options: list of new options
        :return:
        """      
          
        new_options = options.split(',')
        for option in new_options:
            self.option_list.append(option.strip())     

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

# user = VkUser(user_id = input('Введите ваш ID: '), 
#               gender = input("Введите ваш пол 'мужской' или 'женский': ").lower(), 
#               city = input('Введите ваш город: ').capitalize(), 
#               age = int(input("Введите ваш возраст от '14' до '100': ")))

# user.extend_option_list(input('Введите дополнительные параметры для поиска: '))


user_vk = VkUser(97600258, 'женский' ,'Смоленск', 30)
user_vk.extend_option_list('')