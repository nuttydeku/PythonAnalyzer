import os
from urllib.request import urlopen

"""
====================
= URLReader Object =
====================


"""

class URLReader(object):

    def __init__(self, path: str, urlname: str, name: str):
        self.path = path
        self.urlname = urlname
        self.name = name


    def extract_data(self, urlname, path):
        try:
            f = urlopen(urlname)
        except:
            print(urlname + " is invalid")
        writetofile = open(os.path.join(path, "urldata"), "wb")
        for line in f:
            writetofile.write(f.read())
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
    def urlname(self):
        return self.__urlname

    @urlname.setter
    def urlname(self, value):
        self.__urlname = value

    @urlname.deleter
    def urlname(self):
        del self.__urlname