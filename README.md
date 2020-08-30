# Overview
This script is created for gathering video titles and links from pornhub website. It is using selenium Python package and Chrome browser to make website scraping "like a human".

# Prerequirements
* Chrome browser installed
* Downloaded proper "chromedriver.exe" for Windows or "chromedriver" for Linux or OSX file, which will be available in the same directory as script file (you have to check Chrome version and download chromedriver from https://chromedriver.chromium.org/downloads)
* Install all needed packages with: ```pip3 install -r requirements.txt```
* Installed Python3 (my version was 3.8 and all was working fine)
* Change list and variable to yours in **main.py** file if needed: ```search_categories``` and ```max_webpages```

# Script output
By default script will scrap each time 10 (```max_webpages``` variable) web pages of pornhub website for provided category (```search_categories``` list). The result will be video title and video link saved to text file.

# Comments
* The more categories and web pages you will have, the longer you will have to wait for output
