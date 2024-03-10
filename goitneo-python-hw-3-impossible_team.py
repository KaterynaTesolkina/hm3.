import json
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            return str(e)

    def add_birthday(self, birthday):
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            return str(e)

class AddressBook:
    def __init__(self):
        self.data = {}

    def get_birthdays_per_week(self):
        pass

if __name__ == "__main__":
    book = AddressBook()


    book.serialize('addressbook.json')
    book.deserialize('addressbook.json')
    
  import json
if __name__ == "__main__":
    book = AddressBook()
    book.deserialize('addressbook.json')
    while True:
        command = input("Введіть команду: ").strip().lower()
        if command == 'add-birthday':
            name = input("Ім'я контакту: ")
            birthday = input("Дата народження (у форматі DD.MM.YYYY): ")
            contact = book.find(name)
            if contact:
                result = contact.add_birthday(birthday)
                print(result)
            else:
                print(f"Контакт {name} не знайдений.")
        elif command == 'show-birthday':
            name = input("Ім'я контакту: ")
            contact = book.find(name)
            if contact and contact.birthday:
                print(f"Дата народження для {name}: {contact.birthday}")
            else:
                print(f"Дата народження для {name} не вказана.")
        elif command == 'birthdays':
            birthdays = book.get_birthdays_per_week()
            if birthdays:
                print("Користувачі, яких потрібно привітати на наступному тижні:")
                for contact in birthdays:
                    print(f"{contact.name}: {contact.birthday}")
            else:
                print("Немає користувачів з днями народження на наступному тижні.")
        elif command == 'exit':
            book.serialize('addressbook.json')
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")  