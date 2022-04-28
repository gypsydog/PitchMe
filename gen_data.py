from faker import Faker

fake = Faker()


def signup_data():
    data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'password': fake.password()
    }
    return data
