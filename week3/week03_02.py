import os.path


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
        os.path.splitext(self.photo_file_name)
        pass


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = "car"
        pass


class Truck(CarBase):
    body_length = float(0)
    body_width = float(0)
    body_height = float(0)

    def get_body_volume(self):
        return self.body_length*self.body_height*self.body_width

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = 'truck'
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = 'spec_machine'
        pass



def get_car_list(csv_filename):
    car_list = []
    return car_list
