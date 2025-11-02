import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from book import Book

class Scraper():

    def __init__(self, url):
        self.url = url
        self.books = []

    def init(self):
        options = Options()
        options.add_argument("--headless")
        with webdriver.Chrome(options=options, service=Service()) as driver:
            try:
                driver.get(self.url)

                soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

                categories = soup.find_all(class_="nav nav-list")

                for category in categories:
                    links = category.find_all("a")[1:]  # ignora primeiro link
                    for link in links:
                        self.process_category(link, driver)

            except Exception as e:
                pass

    def process_category(self, link, driver):
        driver.get(f"https://books.toscrape.com/{link.get('href')}")
        soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

        books_section = soup.find("section").find_all("div")[1]
        book_rows = books_section.ol.find_all("li")
        for book in book_rows:
            title = book.find("h3").a.text.strip()
            price = book.find("p", class_="price_color").text
            in_stock = True if "ok" in book.find("p", class_="instock availability").i["class"][0] else False
            book = Book(title, price, in_stock)
            self.books.append(book)

    def get_books(self):
        return self.books