from collections import UserDict
from record import Record
from fields import Name, Phone


class AddressBook(UserDict):
    def iterator(self, rec_per_page=2):
        records = 0
        while records < len(self):
            yield list(self.values())[records: records + rec_per_page]
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
    


    def __next__(self) -> list[Record]:
        if self._page_pos < len(self.data.keys()):
            result = []
            keys = list(self.data)[self._page_pos:self._page_pos+self.max_records_per_page]
            for key in keys:
                result.append(self.data[key])
            self._page_pos += self.max_records_per_page
            return result
        self._page_pos = 0
        raise StopIteration


# if __name__ == "__main__":
#     ab = AddressBook()
#     rec1 = Record(Name("Vasy1"), Phone("380980634829"))
#     rec2 = Record(Name("Vasya21"), Phone("380980634829"))
#     rec3 = Record(Name("Jhon"), Phone("380980634829"))
#     ab.add_record(rec1)
#     ab.add_record(rec2)
#     ab.add_record(rec3)
#     for rec in ab.iterator():
#         print(rec)