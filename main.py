from scraper import Scraper

URL = "https://books.toscrape.com/index.html"

def main():
    scraper = Scraper(URL)
    scraper.init()

if __name__ == "__main__":
    main()