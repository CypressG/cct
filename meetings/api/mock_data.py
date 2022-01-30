from faker import Faker


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
        "subjects": fake.sentence(nb_words=2, ext_word_list=word_list),
        "room": fake.bothify(text="###-?", letters="ABC"),
        "time": "TBA TIME FORMAT",
        "group": None,
    }


def fill_registry_mock_data(fake):
    return {"fk_group": None, "fk_user": None}


QUANTITY = 3

GROUP_MOCK_DATA = fill_mock_data(QUANTITY, fill_group_mock_data)


MEETING_MOCK_DATA = fill_mock_data(QUANTITY, fill_meeting_mock_data)

REGISTRY_MOCK_DATA = fill_mock_data(QUANTITY, fill_group_mock_data)
