import os
import tempfile

class File:
    file_name=''

    def __init__(self, file_name):
        self.file_name=file_name

    def __add__(self, other):
        with open(os.path.join(tempfile.gettempdir(), 'storage.data'),"w") as resfile:
            with open(self.file_name,'r') as f1:
                resfile.write(f1.read())
            with open(other.file_name) as f2:
                resfile.write(f2.read())
        return File(os.path.join(tempfile.gettempdir(), 'storage.data'))
    # tempfile.gettempdir

    def __str__(self):
        return self.file_name

    def write(self, text):
        with open(self.file_name,'a+') as f:
            f.write(text)

    lines=[]
    cur_ind=-1;
    def __iter__(self):
        self.cur_ind=-1
        with open(self.file_name,'r') as f:
            self.lines = f.readlines()
        return self

    def __next__(self):
        self.cur_ind+=1
        if self.cur_ind <len(self.lines):
            return self.lines[self.cur_ind]
        raise StopIteration


# obj = File('/home/masha/dive_into_python/dive_into_python/week3/coursera_week3_cars.csv')
#
# obj.write('line')
#
# first = File('/home/masha/dive_into_python/dive_into_python/week3/coursera_week3_cars.csv')
# second = File('/home/masha/dive_into_python/dive_into_python/week3/week03_02.py')
#
# new_obj = first + second
#
#
# for line in File('/home/masha/dive_into_python/dive_into_python/week3/coursera_week3_cars.csv'):
#     print(line)
#
#
# print(obj)