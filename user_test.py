#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new Instance--")
my_state = State()
my_state.name = "New York"
my_city = City()
my_city.name = "NYC"
my_amenity = Amenity()
my_amenity.name = "Kitchen"
my_place = Place()
my_place.name = "My Place"
my_place.description = "This is my place"
my_place.price = "$10,56789"
my_place.number_rooms = 4
my_place.max_guests = 20
my_place.latitude = -1.23456789
my_place.longitude = 1.23456789
my_review = Review()
my_review.text = "I love this place!"


my_user.save()
my_user2.save()
my_state.save()
my_city.save()
my_amenity.save()
my_place.save()
my_review.save()
print(my_user)
print(my_user2)
print(my_state)
print(my_city)
print(my_amenity)
print(my_place)
print(my_review)
