#!/usr/bin/python3

# Import packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform

"""
Script is searching for selected categories one by one on pornhub, scraping using selenium provided amount of pages of each 
pornhub category and writing video titles as well as links to files.
Successful on minimum Python 3.8 and Chrome version 85 (https://chromedriver.chromium.org/downloads).
"""

# Example list of search categories to scrap pornhub with selenium
search_categories = ["teen", "amateur", "milf", "lesbian"]


def main():
    try:
        # Checking what is the running system type
        if platform.system() == "Windows":
            # Initiate Chrome driver for Windows
            driver = webdriver.Chrome('chromedriver.exe')
        else:
            # Initiate other Chrome driver if available
            driver = webdriver.Chrome('chromedriver')

        # Open pornhub.com in Chrome browser
        driver.get('https://pornhub.com')

        # For each category from the list make scrap
        for category in search_categories:
            # Find search bar input object in html code by ID
            search_bar = driver.find_element_by_id('searchInput')
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
            # Max web pages to scrap
            max_webpages = 10
            # List to append titles and video links to write into file or any DB
            video_link_list = []

            # Scrap "max_webpages" from provided category name
            while webpage <= max_webpages:
                # Print information about category and page currently scraped
                print(f"Scraping \"{category}\" page {webpage}.")
                # Open the appropriate url in the browser
                driver.get(f"{main_url}&page={str(webpage)}")

                # Find all html blocks in code which starts with "<a>" tag and includes "href" attribute
                html_object_list = driver.find_elements_by_xpath("//a[@href]")

                # For each "<a>" tag object from the list get video title and link value
                for html_object in html_object_list:
                    video_title = html_object.get_attribute("data-title")
                    video_link = html_object.get_attribute("href")
                    # Verify if the object for sure is valid video link with title
                    if "view_video.php" in video_link and video_title is not None:
                        # If video link is not yet in the link list append it with title
                        if video_link not in video_link_list:
                            video_link_list.append(video_title)
                            video_link_list.append(video_link)
                # Go to next web page
                webpage += 1
            # Print information about writing all data to category file
            print(f"Writing \"{category}\" data to file.")
            # Create or override file with new titles and video links for certain category
            with open(f"video-list-{category}.txt", "w", encoding='utf-8') as file:
                # Write data to file line by line
                file.write('\n'.join([_ for _ in video_link_list]))
        # Close Chrome browser
        driver.close()

    # Print other errors that can occur
    except Exception as e:
        print(f"ERROR: {e}")


# Run the script
if __name__ == '__main__':
    main()
