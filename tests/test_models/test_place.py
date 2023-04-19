#!/usr/bin/python3
""" Unittests for place module """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test class for place file """

    def __init__(self, *args, **kwargs):
        """ test_Place class constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Tests the city id"""
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Tests the user id"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ Tests the name id"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ Tests the description"""
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test the number of rooms"""
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Tests for number of bathrooms"""
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Tests for max guests"""
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Tests price by night"""
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Tests for latitude of location"""
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Tests for longitude of location"""
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Tets for amenity id"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
