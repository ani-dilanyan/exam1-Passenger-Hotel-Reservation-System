from MyExceptions import HotelDataTypeError, HotelDataValueError
from Passanger import Passenger
from Date import Date


class Hotel:
    # ROOMS = {"Standard Suite": 5, "Presidential Suite": 3, "Family Room": 2}
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
            for room_type in self.rooms.keys():
                rooms_str += "{}: {}\n".format(room_type, self.rooms[room_type])
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
        else:
            self.rooms[room_type] -= room_count
            self.passengers.append(Passenger(firstname, lastname, birthday, room_type, room_count))
            return "Room reserved successfully"


h = Hotel({"Standard Suite": 5, "Presidential Suite": 3, "Family Room": 2})
print(h.reserve_rooms("Standard Suite", 2, "Ani", "Dilan", Date(20, 3, 2005)))
print(h.passengers)
