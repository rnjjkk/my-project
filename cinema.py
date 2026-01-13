class CinemaSystem:
    def __init__(self):
        self.__cinema = []

    def add_cinema(self, cinema):
        if isinstance(cinema, Cinema):
            self.__cinema.append(cinema)

    def show_cinema(self):
        if self.__cinema is not None:
            for c in self.__cinema:
                print(c)

class Cinema:
    def __init__(self, name, location, total_cinema_hall=0):
        self.__name = name
        self.__location = location
        self.__total_cinema_hall = total_cinema_hall
        self.__halls = []

    def add_halls(self, halls):
        if isinstance(halls, list):
            self.__halls.extend(halls)
        else:
            self.__halls.append(halls)

    def __str__(self):
        return self.__name + " in location " + self.__location + " has total cinema hall " + str(self.__total_cinema_hall)
    
class CinemaHall:
    pass

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Admin(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

admin = Admin("Admin", "admin@abc.com", "081-234-5678")
print(admin)