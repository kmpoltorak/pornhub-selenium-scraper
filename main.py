#!/usr/bin/python

# Import packages
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Example list of search categories to scrap pornhub with selenium
SEARCH_CATEGORIES = ["teen", "amateur", "milf", "lesbian"]

# Max web pages to scrap
MAX_WEBPGES = 10


def main():
    """
    Script is searching for selected categories one by one on pornhub using Chrome browser,
    scraping using selenium provided amount of pages of each pornhub category and writing video titles
    as well as links to file. Download chromedriver from https://chromedriver.chromium.org/downloads.
    The browser must be open, if it will be hidden down there will be driver error.
    """

    try:
        # Checking what is the running system type
        if platform.system() == "Windows":
            # Initiate Chrome driver for Windows
            service = Service("chromedriver.exe")
        elif platform.system() == "Darwin":
            # Initiate Chrome driver for OSX
            service = Service("chromedriver-osx")
        elif platform.system() == "Linux":
            # Initiate Chrome driver for Linux
            service = Service("chromedriver")
        driver = webdriver.Chrome(service=service)

        # Open pornhub.com website in Chrome browser
        driver.get("https://pornhub.com")

        # For each category from the list make scrap
        for category in SEARCH_CATEGORIES:
            # Find search bar input object in html code by ID
            search_bar = driver.find_element(By.ID, "searchInput")
            # Clean search bar
            search_bar.clear()
            # Write category name in the search bar
            search_bar.send_keys(category)
            # "Click" enter to start search on website
            search_bar.send_keys(Keys.RETURN)

            # Get the existing URL from browser
            main_url = driver.current_url
            # Start web page number
            webpage = 1
            # List to append titles and video links to write into csv like file
            video_link_list = []

            # Scrap "max_webpages" from provided category name
            while webpage <= MAX_WEBPGES:
                # Print information about category and page currently scraped
                print(f"Scraping \"{category}\" page {webpage}.")
                # Open the appropriate url in the browser
                driver.get(f"{main_url}&page={str(webpage)}")

                # Find all html blocks in code which starts with "<a>" tag and includes "href" attribute
                html_object_list = driver.find_elements(By.XPATH, "//a[@href]")

                # For each "<a>" tag object from the list get video title and link value
                for html_object in html_object_list:
                    video_title = html_object.get_attribute("data-title")
                    video_link = html_object.get_attribute("href")
                    # Verify if the object for sure is valid video link with title
                    if "view_video.php" in video_link and video_title is not None and video_link not in video_link_list:
                        video_link_list.append(f"{video_title},{video_link}")
                # Go to next web page
                webpage += 1

            # Print information about writing all data to category file
            print(f"Writing \"{category}\" data to file.")
            # Create or override file with new titles and video links for certain category
            with open(f"video-list-{category}.csv", "w", encoding='utf-8') as file:
                # Write data to file line by line
                file.write('\n'.join(_ for _ in video_link_list))
            file.close()

        # Close Chrome browser
        driver.close()

    # Print other errors that can occur
    except Exception as exception:
        print(f"ERROR: {exception}")


# Run the script
if __name__ == '__main__':
    main()
