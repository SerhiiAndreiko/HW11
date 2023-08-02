from datetime import datetime

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
    def value(self, __new_value):
        try:
            self.__value = str(int(__new_value))
        except ValueError:
            raise ValueError("wrong phone format")


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