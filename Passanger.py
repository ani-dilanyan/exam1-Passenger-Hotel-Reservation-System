from Person import Person
from Date import Date
from MyExceptions import PersonalDataTypeError, PersonalDataValueError
from datetime import date


class Passenger(Person):
    def __init__(self, firstname, lastname, birthday: Date, room_type, room_count):
        try:
            if type(room_type) != str:
                raise PersonalDataTypeError("room type", room_type)
            elif type(room_count) != int:
                raise PersonalDataTypeError("room count", room_count)

            if date.today().year - birthday.year < 18:
                raise PersonalDataValueError("You must be at least 18 years old")
            elif room_type not in ("Standard Suite", "Presidential Suite", "Family Room"):
                raise PersonalDataValueError("Wrong value for room type")
            elif room_count < 0:
                raise PersonalDataValueError("Wrong value for room count")
        except (PersonalDataValueError, PersonalDataValueError) as err:
            print(err)
        else:
            super().__init__(firstname, lastname, birthday)
            self.room_type = room_type
            self.room_count = room_count

    def __repr__(self):
        return super().__repr__() + " " + self.get_room()

    def get_room(self):
        try:
            return "{} {}".format(self.room_type, self.room_count)
        except AttributeError:
            return "Couldn't find essential attributes"
