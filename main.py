# selenium for scraping
from selenium import webdriver
import time

WEBSITE_LINK = 'https://myip.ms/'


def check_website():
    # Config Driver
    driver = webdriver.Chrome()

    # Run driver
    driver.maximize_window()

    # Get website
    driver.get(WEBSITE_LINK)

    # Selenium Code for Scrapping
    # Xpath Selection

    # Wait for specific time
    time.sleep(1)  # in minute

    # Close the browser
    # driver.quit()


if __name__ == '__main__':
    check_website()
