# os for exploring directory
import os
# selenium for scraping
from selenium import webdriver
# time for sleeping the execution (code)
import time
# datetime to get latest time
from datetime import datetime, timedelta
# Selenium_wire for username and password proxy configuration
# from seleniumwire import webdriver
# for importing consts from .env
from dotenv import load_dotenv

# For email sending with Google app password
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Load environment variables from .env file
load_dotenv()

# consts from .env
website_link = os.getenv("WEBSITE_LINK")
rerun_time = int(os.getenv("RERUN_TIME"))
running_duration = int(os.getenv("RUNNING_DURATION"))

# Proxy constants
proxy_ip_auth = os.getenv("PROXY_IP_AUTH")
proxy_username = os.getenv("PROXY_USERNAME")
proxy_password = os.getenv("PROXY_PASSWORD")
proxy_domain = os.getenv("PROXY_DOMAIN")
proxy_port = os.getenv("PROXY_PORT")

# Google App Password
gmail_app_username = os.getenv("GMAIL_APP_USERNAME")
gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
gmail_sender = os.getenv("GMAIL_SENDER")
gmail_receiver = os.getenv("GMAIL_RECEIVER")


def check_website(parent_dir):
    # # Config Driver for Ip Auth Configuration
    # # Chrome Options
    # chrome_options = webdriver.ChromeOptions()
    # # chrome_options.add_argument("--headless") # To run scraper without in background (without open the chrome)
    # chrome_options.add_argument('--proxy-server=%s' % proxy_ip_auth)
    # driver = webdriver.Chrome(options=chrome_options)

    # # UserName and Password Authentication
    # http = f"http://{proxy_username}:{proxy_password}@{proxy_domain}:{proxy_port}"
    # proxy_options = {
    #     'proxy': {
    #         "http": http,
    #         "https": http,
    #         'verify_ssl': False,
    #     }
    # }
    # # Config Driver
    # driver = webdriver.Chrome(seleniumwire_options=proxy_options)

    # Config Driver without proxies
    driver = webdriver.Chrome()

    # Run driver
    driver.maximize_window()

    # Get website
    driver.get(website_link)

    # Selenium Code for Scrapping
    # Xpath Selection

    # Wait for specific time
    time.sleep(10)  # in seconds

    # Get the current date and time
    current_time = datetime.now()

    # Format the current date and time as a string to use in the filename
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")  # String format time

    # Combine the directory path and the formatted time to create the full path for the screenshot
    screenshot_path = os.path.join(parent_dir, f"screenshot_{formatted_time}.png")

    # Take a screenshot and save it to the specified directory with the current date in the filename
    driver.save_screenshot(screenshot_path)
    print("ScreenShot Taken")

    try:
        # Get Image for sending in Email
        with open(screenshot_path, 'rb') as f:
            image_part = MIMEImage(f.read())

        # Email Content
        message = MIMEMultipart()
        subject = "From Scraper"
        body = f"Hello world!"
        message['Subject'] = "Scraper Testing"
        message["From"] = gmail_sender
        message["To"] = gmail_receiver
        html_part = MIMEText(body)
        message.attach(html_part)
        message.attach(image_part)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(gmail_app_username, password=gmail_app_password)
            smtp_server.sendmail(gmail_sender, gmail_receiver, message.as_string())
            print("Message sent!")
        print("Email Sent")
    except Exception as e:
        print("Issue Found", e)

    # Wait for specific time
    time.sleep(10)  # in seconds

    # Close the browser
    # driver.quit()


# Specify the parent directory path where you want to save screenshots
parent_directory = "screenshots"

# Ensure the parent directory exists
os.makedirs(parent_directory, exist_ok=True)

# Calculate the end time
end_time = datetime.now() + timedelta(seconds=running_duration)


def main():
    while datetime.now() < end_time:
        try:
            # Check website
            check_website(parent_directory)
            print("Main function executed successfully.")
            time.sleep(rerun_time)  # Wait for specific minutes before running again

        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(rerun_time)  # Wait for specific minutes before running again


if __name__ == '__main__':
    main()
