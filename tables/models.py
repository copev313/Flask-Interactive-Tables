from tables import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(250))
    phone = db.Column(db.String(20))

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }
