from datetime import datetime
import re

class PhoneError(Exception):
    pass



class Field:
    def __init__(self, value=any)-> None:
        self.__value = value
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        if __new_value and __new_value.isprintable():
            self.__value = __new_value
        else:
            raise ValueError("used non printable chars") 

    def __eq__(self, __other):
        if isinstance(__other, Field):
            return self.value == __other.value
        else:
            raise TypeError
    
    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self):
        return self.__value
    

    @value.setter
    def value(self, new_value):
        if not re.match(r'\+?\d{9,15}', new_value):
            raise PhoneError("Invalid phone number format")
        self.__value = new_value


class Birthday(Field):

    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, __new_value):
        try:
            d = datetime.strptime(__new_value, "%d-%m-%Y")
            self.__value = d
        except ValueError:
            raise ValueError("Wrong date format, dd-mm-YYYY")
        

    def __str__(self):
        return self.value.strftime("%d-%m-%Y")
