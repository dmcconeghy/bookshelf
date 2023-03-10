from models import db
import uuid

'''
    This file is currently deprecated. 
    It may be used in the future to create a device model for the database.
    See the following link for more information:
    https://blog.teclado.com/api-key-authentication-with-flask/

'''
# 

# class DeviceModel(db.Model):
#     __tablename__ = 'devices'

#     id = db.Column(db.Integer, primary_key=True)
#     device_name = db.Column(db.String(80))
#     device_key = db.Column(db.String(80))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship('UserModel', back_populates='devices')

#     def __init__(self, device_name, device_key, user_id):
#         self.device_name = device_name
#         self.device_key = device_key or uuid.uuid4().hex
#         self.user_id = user_id

#     def json(self):
#         return {'device_name': self.device_name, 'device_key': self.device_key, 'user_id': self.user_id}
    
#     @classmethod
#     def find_by_name(cls, device_name):
#         return cls.query.filter_by(device_name=device_name).first()
    
#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete_from_db(self):
#         db.session.delete(self)
#         db.session.commit()

# class UserModel(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80))
#     password = db.Column(db.String(80))
#     devices = db.relationship('DeviceModel', back_populates='user')

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def json(self):
#         return {'username': self.username, 'password': self.password, 'devices': [device.json() for device in self.devices]}
    
#     @classmethod
#     def find_by_username(cls, username):
#         return cls.query.filter_by(username=username).first()
    
#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete_from_db(self):
#         db.session.delete(self)
#         db.session.commit()