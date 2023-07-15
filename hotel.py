from MyExceptions import HotelDataTypeError, HotelDataValueError
from Passanger import Passenger
from Date import Date


class Hotel:
    def __init__(self, rooms):
        try:
            if type(rooms) != dict:
                raise HotelDataTypeError("rooms", rooms)
        except HotelDataTypeError as err:
            print(err)
        else:
            self.rooms = rooms
            self.passengers = []

    def __repr__(self):
        try:
            rooms_str = ""
            for room_type, count in self.rooms.items():
                rooms_str += "{}: {}\n".format(room_type, count)
            return rooms_str
        except AttributeError:
            return "Empty object. No rooms added"

    def reserve_rooms(self, room_type, room_count, firstname, lastname, birthday):
        try:
            if type(room_type) != str:
                raise HotelDataTypeError("room type", room_type)
            elif type(room_count) != int:
                raise HotelDataTypeError("room count", room_count)

            if room_type not in ("Standard Suite", "Presidential Suite", "Family Room"):
                raise HotelDataValueError("Wrong value for room type", room_type)
            elif room_count > self.rooms[room_type]:
                raise HotelDataValueError("No enough available", room_count)

        except (HotelDataValueError, HotelDataTypeError) as err:
            return err
        except AttributeError:
            return "Object does not have attribute 'rooms'"
        else:
            self.rooms[room_type] -= room_count
            self.passengers.append(Passenger(firstname, lastname, birthday, room_type, room_count))
            return "Room reserved successfully"

    def add_room(self, room_type, room_count):
        try:
            if type(room_type) != str:
                raise HotelDataTypeError("room type", room_type)
            elif type(room_count) != int:
                raise HotelDataTypeError("room count", room_count)
        except (HotelDataValueError, HotelDataTypeError) as err:
            return err
        except AttributeError:
            return "Object does not have attribute 'rooms'"
        else:
            self.rooms.update({room_type: room_count})

    def remove_room(self, room_type):
        try:
            if type(room_type) != str:
                raise HotelDataTypeError("room type", room_type)
        except (HotelDataValueError, HotelDataTypeError) as err:
            return err
        except AttributeError:
            return "Object does not have attribute 'rooms'"
        else:
            self.rooms.pop(room_type)

    def change_room_count(self, room_type, room_count):
        try:
            if type(room_type) != str:
                raise HotelDataTypeError("room type", room_type)
            elif type(room_count) != int:
                raise HotelDataTypeError("room count", room_count)
        except (HotelDataValueError, HotelDataTypeError) as err:
            return err
        except AttributeError:
            return "Object does not have attribute 'rooms'"
        else:
            self.rooms[room_type] = room_count

    def get_reservations(self):
        try:
            passengers_str = ""
            for passenger in self.passengers:
                passengers_str += "{}\n".format(passenger)
            return passengers_str
        except AttributeError:
            return "Object does not have attribute 'passengers'"

#
# h = Hotel({"Standard Suite": 5, "Presidential Suite": 3, "Family Room": 2})
# print(h)
# print(h.reserve_rooms("Standard Suite", 2, "Ani", "Dilanyan", Date(20, 3, 2005)))
# print(h)
# print(h.passengers)
# print(h.get_reservations())
# h.add_room("Double", 7)
# print(h)
#
# h.remove_room("Double")
# print(h)
#
# h.change_room_count("Double", 5)
# print(h)
