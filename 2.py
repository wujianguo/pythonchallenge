#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,string
URL='http://www.pythonchallenge.com/pc/def/ocr.html'
def getMesses(url):
    f=urllib.urlopen(url)
    mess=f.read()
    f.close()
    return mess[mess.rfind('!--')+4:]
def main():
    messes=getMesses(URL)
    print([x for x in messes if x in string.letters])
if __name__=='__main__':
    main()
