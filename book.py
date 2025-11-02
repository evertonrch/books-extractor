import json

class Book():

    def __init__(self, title, link):
        self.__title = title
        self.__link = link

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def __str__(self):
        # só serializa tipos primitivos
        return json.dumps(self.__dict__)
