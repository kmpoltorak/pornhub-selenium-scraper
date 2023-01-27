# Overview
This script is created for gathering video titles and links from pornhub website. It is using selenium Python package and Chrome browser to make website scraping "like a human"

# Prerequirements
* Chrome browser installed
* Downloaded and name properly chrome driver file for Windows OSX, and Linux, which will be available in the same directory as script file (you have to check Chrome version and download chromedriver from https://chromedriver.chromium.org/downloads)
* Install all needed packages with: ```pip3 install -r requirements.txt```
* Install Python3
* Change list and variable to yours in **main.py** file if needed: ```SEARCH_CATEGORIES``` and ```MAX_WEBPAGES```

# Script output
By default script will scrap each time 10 (```MAX_WEBPAGES``` variable) web pages of pornhub website for provided category (```SEARCH_CATEGORIES``` list). The result will be video title and video link saved to csv like file.

# Comments
* The more categories and web pages you will have, the longer you will have to wait for output
