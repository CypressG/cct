from faker import Faker
import random


def fill_mock_data(quantity, callback):
    user_list = []
    fake = Faker(["en_US", "lt_LT", "ja_JP"])
    for x in range(quantity):
        single = callback(fake)
        user_list.append(single)
    return user_list


def fill_group_mock_data(fake):
    word_list = [
        " managing",
        " supervision",
        " artificial",
        " business",
        " marketing",
        " sales",
        " Oriental",
        " Remote",
        " Startup",
        " Session",
    ]
    return {"name": fake.sentence(nb_words=3, ext_word_list=word_list)}


def fill_meeting_mock_data(fake):
    word_list = [
        " statistics",
        " 2021",
        " 2022",
        " 2012",
        " financial",
        " crypto",
        " web3",
        " new product",
        " healtcare",
        " sprint",
        " agile",
        " scrum",
    ]
    return {
        "subject": fake.sentence(nb_words=2, ext_word_list=word_list),
        "room": random.randint(1, QUANTITY),
        "start_time": "2022-02-01T14:54:02.953Z",
        "end_time": "2022-02-01T14:54:02.953Z",
        "group": random.randint(1, QUANTITY),
    }


def fill_room_mock_data(fake):
    return {
        "name": fake.bothify(text="###-?", letters="ABC"),
    }


def fill_user_mock_data(fake):
    return {
        "email": fake.ascii_company_email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "password": fake.color_name(),
    }


def fill_registry_mock_data(fake):
    return {
        "group": random.randint(1, QUANTITY),
        "user": random.randint(1, QUANTITY),
    }


QUANTITY = 3

GROUP_MOCK_DATA = fill_mock_data(QUANTITY, fill_group_mock_data)

MEETING_MOCK_DATA = fill_mock_data(QUANTITY, fill_meeting_mock_data)

REGISTRY_MOCK_DATA = fill_mock_data(QUANTITY, fill_group_mock_data)

USER_MOCK_DATA = fill_mock_data(QUANTITY, fill_user_mock_data)

ROOM_MOCK_DATA = fill_mock_data(QUANTITY, fill_room_mock_data)
