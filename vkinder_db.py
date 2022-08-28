import sqlalchemy
from sqlalchemy.orm import sessionmaker

from db_models import create_tables, User, Favorite, Photo, BlackList


def add_user_to_db(session, user_id: int, name: str, surname: str, gender: str, age: int, city: str) -> bool:
    try:
        user = User(user_id=user_id, name=name, surname=surname, gender=gender, age=age, city=city)
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def add_favorite_to_db(session, user_id: int, favorite_for_id: int) -> bool:
    try:
        user = Favorite(user_id=user_id, favorite_for_id=favorite_for_id)
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def add_photo_to_db(session, photo_list: list, favorite_id: int) -> bool:
    try:
        photos = [Photo(photo_id=x, favorite_id=favorite_id) for x in photo_list]
        session.add_all(photos)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_favorites(session, user_id):
    try:
        users = [user.user_id for user in session.query(Favorite).all() if user.favorite_for_id == user_id]
        return users
    except Exception as e:
        print(e)
        return False


def add_user_to_blacklist(session, user_id, blocked_for_id):
    try:
        user = BlackList(user_id=user_id, blocked_for_id=blocked_for_id)
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_blacklist(session, user_id):
    try:
        users = [user.user_id for user in session.query(BlackList).all() if user.favorite_for_id == user_id]
        return users
    except Exception as e:
        print(e)
        return False

user = input('Логин БД: ')
password = input('Пароль: ')
DSN = f'postgresql://{user}:{password}@localhost:5432/vkinder_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# add_user_to_db(session, user_id=112, name='Egor', surname='Sm', gender='male', age=33, city='Nov')
# add_user_to_db(session, user_id=228, name='Камила', surname='Го', gender='male', age=23, city='Nov')
# add_favorite_to_db(session, user_id=228, favorite_for_id=112)
#
# for user in session.query(User).all():
#     print(user)
#
# for user in session.query(Favorite).all():
#     print(user)
#
# print(get_favorites(session, 112))


session.close()
