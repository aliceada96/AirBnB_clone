#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class
    
    Args:
        city_id (str): it will be the City.id
        user_id (str): it will be the User.id
        name (str): name of place
        description (str): description of place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests 
        price_by_night (int): price per night
        latitude (float): Lattitude of place
        longitude (float): longitude of place
        amenity_ids (list): list of Amenity.ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
