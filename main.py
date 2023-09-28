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
    
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")






