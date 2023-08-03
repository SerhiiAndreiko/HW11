from collections import UserDict
from record import Record
from fields import Name, Phone
import pickle
import os


class AddressBook(UserDict):
    def iterator(self, rec_per_page=2):
        records = 0
        while records < len(self):
            yield "; ".join(str(rec) for rec in list(self.values())[records: records + rec_per_page])
            records += rec_per_page
        

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
        return "Done"
   
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        result = map(str, self.data.values())
        return "\n".join(result)
    
    
    def load_data(self, file_name):
        if os.path.exists(file_name):
            with open (file_name, "rb") as f:
                self.data = pickle.load(f)

    
    def save_data(self, file_name):
        with open (file_name, "wb") as f:
            pickle.dump(self.data, f)


if __name__ == "__main__":
    ab = AddressBook()
    rec1 = Record(Name("Vasy1"), Phone("380980634829"))
    rec2 = Record(Name("Vasya21"), Phone("380980634829"))
    rec3 = Record(Name("Jhon"), Phone("380980634829"))
    ab.add_record(rec1)
    ab.add_record(rec2)
    ab.add_record(rec3)
    for rec in ab.iterator(1):
        print(rec)