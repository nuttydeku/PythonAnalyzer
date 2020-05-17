import os

"""
=====================
= FileReader Object =
=====================

Reads all txt files from path
Writes all data to new txt file in same path  

"""


class FileReader(object):

    def __init__(self, path: str, filename: str, name: str):
        self.path = path
        self.filename = filename
        self.name = name

    def extract_data(self, path):
        try:
            writetofile = open(os.path.join(path, "wigglefile"), "a")
        except:
            print("Write to file failed")
            return
        else:
            for filename in os.listdir(path):
                try:
                    with open(os.path.join(path, filename), 'r') as f:
                        writetofile.write(f.read())
                except:
                    print("File " + filename + " failed to open")
                    print("Check " + os.path.join(path, filename) + " for errors")

            f.close()
            writetofile.close()


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, pathvalue):
        self.__path = pathvalue

    @path.deleter
    def path(self):
        del self.__path

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @filename.deleter
    def filename(self):
        del self.__filename



