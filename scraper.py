import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from book import Book

from logger import logger

class Scraper():

    def __init__(self, url):
        self.url = url
        self.books = []

    def run(self):
        options = Options()
        options.add_argument("--headless")
        with webdriver.Chrome(options=options, service=Service()) as driver:
            try:
                driver.get(self.url)
                logger.info("Initializing scraper")

                soup = BeautifulSoup(driver.page_source, "html.parser")

                categories = soup.find_all(class_="nav nav-list")

                for category in categories:
                    links = category.find_all("a")[1:]  # ignora primeiro link
                    for link in links:
                        logger.info(f"Starting processing of the category: {link.text.strip()}")
                        self.process_category(link, driver)
                        logger.info(f"Finalizing processing of the category: {link.text.strip()}")

            except Exception as e:
                logger.error(f"Algo deu errado ao fazer o scraper: {e}")

    def process_category(self, link, driver):
        driver.get(f"https://books.toscrape.com/{link.get('href')}")

        while True:
            soup = BeautifulSoup(driver.page_source, "html.parser")

            category_title = soup.find("div", class_="page-header").h1.text
            books_div = soup.find("section").find_all("div")[1]
            book_rows = books_div.ol.find_all("li")
            for book in book_rows:
                book = self.create_book_item(book, category_title)
                self.books.append(book)

            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
                next_button.click()
                logger.info(f"Jump to next page in {category_title}")
                time.sleep(1)
            except NoSuchElementException:
                logger.info("Moving to the next category")
                break

    def create_book_item(self, book, category_title):
        title = book.find("h3").a.text.strip()
        price = book.find("p", class_="price_color").text
        in_stock = self.has_stock(book)
        return Book(title, price, in_stock, category_title)

    def has_stock(self, book):
        return True if "ok" in book.find("p", class_="instock availability").i["class"][0] else False

    def get_books(self):
        return self.books
