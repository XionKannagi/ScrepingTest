# _*_ coding: utf-8 _*_


import requests
import sys
import json
import os
from selenium import webdriver
from bs4 import BeautifulSoup


def scraping(url, output_name):

    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)

    #driver.get(url)
    #html = driver.page_source.encode('utf-8')

    response = requests.get(url)
    html = response.text.encode(response.encoding)

    soup = BeautifulSoup(html, "lxml")

    header = soup.find("head")
    title = header.find("title").text

    description = header.find("meta", attrs={"name": "description"})
    description_content = description.attrs['content'].text

    output = {"title": title, "descripition": description_content}

    with open(output_name, "w") as fout:
        json = json.dump(output, fout, indent = 4, sort_keys=true)


if __name__ == '__main__':

    argvs = sys.argv

    if len(argvs) != 2:
        print("Usage:python scraping.py [url] [output]")
        exit()

    url = argvs[1]
    output_name = argvs[2]

    scraping(url, output_name)
