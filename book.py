import json

class Book():

    def __init__(self, title, link, in_stock):
        self.__title = title
        self.__link = link
        self.__in_stock = in_stock

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def get_in_stock(self):
        return self.__in_stock

    def set_in_stock(self, in_stock):
        self.__in_stock = in_stock

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)
