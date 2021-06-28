from random import randint
import sys
from faker import Faker
from models import User


def create_fake_users(n):
    '''Creates N fake users to fill out our table with data.'''
    faker = Faker()

    for i in range(n):
        name = faker.name()
        age = randint(18, 90)
        address = faker.address().replace('\n', ', '),
        phone_number = faker.phone_number()
        email = faker.email()

        user = User(name=name,
                    age=age,
                    address=address,
                    phone=phone_number,
                    email=email)
        db.session.add(user)

    db.session.commit()
    print(f"{n} FAKE USERS ADDED TO THE DATABASE.")


if __name__ == '__main__':

    args = sys.argv

    # [CHECK] Argument validation:
    if (len(args) <= 1):
        print("Please pass in the number of users you'd like ot create")
        sys.exit(1)

    create_fake_users(int(args[1]))
