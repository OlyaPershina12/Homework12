# Пункт а)
# Описание класса: у квартиры есть её номер, номер улицы, на которой она находится, год её построения, количество
# человек, проживающих в ней. Квартира может показывать всю информацию о ней.
# Класс: Apartment
# Атрибуты объектов данного класса:
# - number
# - street
# - year
# - members
# Методы объектов данного класса:
# - show_information()

class Apartment:
    # пункт б) - конструктор
    def __init__(self, number, street, year, members):
        self.number = number
        self.street = street
        self.year = year
        self.members = members

    # пункт в) - show_information() является методом объекта класса Apartment
    def show_information(self):
        print(f"Квартира под номером {self.number} была построена на {self.street} улице в {self.year} году. Здесь"
              f" живёт {self.members} человек(а).")


# пункт г) - создаём объект person класса Apartment
apartment = Apartment(number=65, street=11, year=1984, members=5)

# пункт д) - обращаемся к атрибутам объекта
print("Number:", apartment.number)
print("Street:", apartment.street)
print("Year:", apartment.year)
print("Members:", apartment.members)
# пункт e) - обращаемся к методу объекта
apartment.show_information()
