from faker import Faker


def fill_mock_data(quantity):
    user_list = []
    fake = Faker(["en_US", "lt_LT", "ja_JP"])
    for x in range(quantity):
        single_user = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": fake.color_name(),
        }
        user_list.append(single_user)
    return user_list


USER_MOCK_DATA = fill_mock_data(3)

print(USER_MOCK_DATA)
