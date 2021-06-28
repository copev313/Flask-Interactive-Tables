from fun_tables import db
from random import randint
from faker import Faker


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(250))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))


    def to_dict(self):
        '''Returns a User object as a dictionary.'''
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }


def create_fake_users(num_users):
    '''Creates N fake users to fill out our table with data.'''
    if (num_users <= 0) :
        print("The method: 'create_fake_users' requires a positive integer argument.")
        return

    faker = Faker()
    for i in range(num_users):
        user = User(name=faker.name(),
                    age=randint(18, 90),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email())
        db.session.add(user)

    db.session.commit()
    print(f"{num_users} FAKE USERS ADDED TO THE DATABASE.")
    return
