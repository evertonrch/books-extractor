import json


class Book():

    def __init__(self, title, link, in_stock, category):
        self.title = title
        self.link = link
        self.in_stock = in_stock
        self.category = category

    def get_title(self):
        return self.title

    def get_link(self):
        return self.link

    def get_in_stock(self):
        return self.in_stock

    def get_category(self):
        return self.category

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)
