import json

from logger import logger
from scraper import Scraper

URL = "https://books.toscrape.com"


def to_json(books):
    books_data = [book.to_dict() for book in books]
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books_data, f, indent=4)


def main():
    scraper = Scraper(URL)
    scraper.run()

    try:
        logger.info("Starting to write JSON")
        to_json(scraper.get_books())
        logger.info("JSON file completed")
    except Exception as e:
        logger.info(f"Error while saving json: {e}")


if __name__ == "__main__":
    main()
