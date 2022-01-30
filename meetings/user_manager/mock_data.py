from faker import Faker


def fill_mock_data(quantity, callback):
    user_list = []
    fake = Faker(["en_US", "lt_LT", "ja_JP"])

    for x in range(quantity):
        single = callback(fake)
        user_list.append(single)
    return user_list


# Fills in user mock data
def fill_user_mock_data(fake):
    user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": fake.color_name(),
    }
    return user


USER_MOCK_DATA = fill_mock_data(5, fill_user_mock_data)
