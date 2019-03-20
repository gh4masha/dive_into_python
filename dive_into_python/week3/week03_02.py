import os.path
import csv


class CarBase:
    car_type = ""
    photo_file_name = ''
    carrying = ''

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying


class Car(CarBase):
    passenger_seats_count = int(0)

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count
        super().__init__(brand, photo_file_name, carrying)


class Truck(CarBase):
    body_length = float(0)
    body_width = float(0)
    body_height = float(0)
    body_whl = float(0)

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl or None
        if self.body_whl is not None:
            sizes = self.body_whl.split('x');
            self.body_length=float(sizes[0])
            self.body_width = float(sizes[1])
            self.body_height = float(sizes[2])


class SpecMachine(CarBase):
    extra = ''

    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = 'spec_machine'
        self.extra = extra
        super().__init__(brand, photo_file_name, carrying)


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row[0])
            try:
                if row[0] == 'car':
                    if row[1] is not None and row[3] is not None and row[5] is not None and row[2] is not None:
                        car = Car(row[1], row[3], float(row[5]), int(row[2]))
                        car_list.append(car)
                elif row[0] == 'truck':
                    if row[1] is not None and row[3] is not None and row[5] is not None :
                        truck = Truck(row[1], row[3], float(row[5]), row[4] or None)
                        car_list.append(truck)
                elif row[0] == 'spec_machine':
                    if row[1] is not None and row[3] is not None and row[5] is not None and row[6] is not None:
                        spec_machine = SpecMachine(row[1], row[3],float( row[5]), row[6] or None)
                        car_list.append(spec_machine)
            except (LookupError, ArithmeticError):
                pass

    #     0       1             2                   3               4         5        6
    #  car_type; brand; passenger_seats_count; photo_file_name; body_whl;  carrying; extra

    return car_list


# get_car_list('/home/masha/dive_into_python/dive_into_python/week3/coursera_week3_cars.csv')
