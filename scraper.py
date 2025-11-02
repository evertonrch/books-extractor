import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from book import Book


class Scraper():

    def __init__(self, url):
        self.url = url

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
                        name = link.text.strip()
                        href = link.get("href")

                        book = Book(name, href)
                        print(book)


            except Exception as e:
                pass
