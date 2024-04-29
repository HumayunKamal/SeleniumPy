# os for exploring directory
import os
# selenium for scraping
from selenium import webdriver
# time for sleeping the execution (code)
import time
# datetime to get latest time
from datetime import datetime
# Selenium_wire for username and password proxy configuration
from seleniumwire import webdriver

WEBSITE_LINK = 'https://myip.ms/'


def check_website():
    # # Config Driver
    # # For Ip Auth Configuration
    # # Chrome Options
    # chrome_options = webdriver.ChromeOptions()
    # # chrome_options.add_argument("--headless") # To run scraper without in background (without open the chrome)
    # ipconfig = f"http://proxy_domain:proxy_port"
    # chrome_options.add_argument('--proxy-server=%s' % ipconfig)
    # driver = webdriver.Chrome(options=chrome_options)

    # UserName and Password Authentication
    proxy_options = {
        'proxy': {
            "http": "http://proxy_username:proxy_password@proxy_domain:proxy_port/",
            "https": "http://proxy_username:proxy_password@proxy_domain:proxy_port/",
            'verify_ssl': False,
        }
    }
    # Config Driver
    driver = webdriver.Chrome(seleniumwire_options=proxy_options)

    # Run driver
    driver.maximize_window()

    # Get website
    driver.get(WEBSITE_LINK)

    # Selenium Code for Scrapping
    # Xpath Selection

    # Wait for specific time
    time.sleep(10)  # in seconds

    # Specify the parent directory path where you want to save screenshots
    parent_directory = "screenshots"

    # Ensure the parent directory exists
    os.makedirs(parent_directory, exist_ok=True)

    # Get the current date and time
    current_time = datetime.now()

    # Format the current date and time as a string to use in the filename
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")  # String format time

    # Combine the directory path and the formatted time to create the full path for the screenshot
    screenshot_path = os.path.join(parent_directory, f"screenshot_{formatted_time}.png")

    # Take a screenshot and save it to the specified directory with the current date in the filename
    driver.save_screenshot(screenshot_path)
    print("ScreenShot Taken")

    # Wait for specific time
    time.sleep(10)  # in seconds

    # Close the browser
    # driver.quit()


if __name__ == '__main__':
    check_website()
