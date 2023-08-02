class PageIterator:
    def __init__(self, address_book, page_size):
        self.address_book = address_book
        self.page_size = page_size
        self.iterator = iter(address_book)
        self.current_page = 0

    def next_page(self):
        self.current_page += 1
        result = []
        try:
            for _ in range(self.page_size):
                result.append(next(self.iterator))
        except StopIteration:
            pass
        return result

page_iterator = PageIterator(a_book, 5)  

def command_next_page(*args) -> str:
    records = page_iterator.next_page()
    if not records:
        return "No more records"
    return "\n".join(map(str, records))


def days_to_birthday(self) -> int or None:
        if self.birthday is not None:
            now = datetime.now()
            birth_date = datetime.strptime(self.birthday.value, '%d-%m-%Y')
            next_birthday = birth_date.replace(year=now.year)
            if now > next_birthday:
                next_birthday = birth_date.replace(year=now.year + 1)
            days_left = (next_birthday - now).days
            return days_left