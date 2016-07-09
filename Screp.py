#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import urllib2
from BeautifulSoupTests import BeautifulSoup


def scraping(url):

    htmlrp = urllib2.urlopen(url)
    html = htmlrp.read().decode("utf-8", "replace")
    htmlrp.close()

    soup = BeautifulSoup(html)
    for link in soup.findAll("script"):
        print(link)

if __name__ == '__main__':

    scraping("http://www.yahoo.co.jp")

