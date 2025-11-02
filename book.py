import json


class Book():

    def __init__(self, title, link, in_stock, category):
        self.__title = title
        self.__link = link
        self.__in_stock = in_stock
        self.__category = category

    def get_title(self):
        return self.__title

    def get_link(self):
        return self.__link

    def get_in_stock(self):
        return self.__in_stock

    def get_category(self):
        return self.__category

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)
