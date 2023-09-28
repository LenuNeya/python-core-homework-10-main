from collections import UserDict
from re import search

class Field:
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    
    def __init__(self, value: str):
        nodigit = search('\D+', value)
        if nodigit is None and len(value) == 10:
            self.value = value
        else:
            raise ValueError("Phone number is not valid")
    
    def __str__(self) -> str:
        return self.value
  

class Record:
    
    def __init__(self, name, phone=''):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.phones.append(Phone(phone))
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone: str):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                break    
    
    def edit_phone(self, old_phone, new_phone):
        phone = None
        for i in self.phones:
            if i.value == old_phone:
                phone = i
                break
        if phone is None:
            raise ValueError("Phone number is not fided")
        else:
            phone.value = new_phone


    def find_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                return i
        return None

      

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        Key = record.name.value
        self.data.update({Key:record})
    
    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]



if __name__ == '__main__':
    
    record1 = Record("Test1")
    record1.add_phone("1234567890")
    record1.add_phone("5555555555")

    record2 = Record("Test2")
    record2.add_phone("1234567890")
    record2.add_phone("5555555555")
    
    address_list = AddressBook()
    address_list.add_record(record1)
    address_list.add_record(record2)

    print(address_list.data)






