

class FileReader:
    filePath = ""


    def __init__(self, filePath):
        self.filePath=filePath

    def read(self):
        result = ""
        try:
            f = open(self.filePath, 'r')
            result = f.read()

        except IOError as err:
            result=""
        finally:
            f.close()

        return result





#
#
# reader = FileReader("/home/masha/dive_into_python/dive_into_python/week3/masha.txt")
# print(reader.read())