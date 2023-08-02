from fields import Field, Name, Phone, Birthday
from datetime import datetime


class Record:
    def __init__(self, name: Name, phone: Phone = None,birthday: Birthday=None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def add_birthday(self, birthday):
        self.birthday = birthday
        return True

    def add(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.add_phone(field)
        if isinstance(field, Birthday):
            return self.add_birthday(field)
        return False


    def remove_birthday(self, birthday: Birthday) -> None:
     if self.birthday == birthday:
        self.birthday = None
        return True
     return False
    

    def remove(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.remove_phone(field)
        if isinstance(field, Birthday):
            return self.remove_birthday(field)
        return False
    

    def add_phone(self, phone: Phone) -> None:
        if phone not in self.phones:
                self.phones.append(phone)
                return F"{phone} add successfull"
        return F"{phone} already inside"
            
    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
            return "Done"
        return "not find phone"

    def remove_phone(self, phone: Phone) -> None:
        if phone in self.phones:
            del self.phones[self.phones.index(phone)]
            return True
        return False
    

    def days_to_birthday(self) -> int or None:
            if self.birthday:
                now = datetime.now()
                birth_date = self.birthday.value
                next_birthday = birth_date.replace(year=now.year)
                if now > next_birthday:
                    next_birthday = birth_date.replace(year=now.year + 1)
                days_left = (next_birthday - now).days
                return days_left
    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phone == other.phone and self.birthday == other.birthday
        return False
    

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        phones = ", ".join(str(p) for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"name: {self.name}, phone: {phones}{birthday}"
        

    
    
    
    
    
    


# if __name__ == "__main__":
#     rec = Record(Name("Bill"), birthday=Birthday("12.09-1999"))
#     print(rec.days_to_birthday())