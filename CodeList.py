# -*- coding: utf-8 -*-
#!/usr/bin/env python
import datetime, json
import urllib
date = str(datetime.datetime.now())[0:10].split('-')
datenow = date[0] +'-'+ date[1] +'-'+ date[2]
class dict(object):
    def __init__(self):
        url = 'https://www.nesine.com/iddaa/IddaaResultsData?BetType=1&OnlyLive=0&Date='+datenow+'&League=&FilterType=init'
        source = urllib.urlopen(url)
        self.data = json.load(source)
        self.liste = {}
    def test(self):
        for OnlineIddaa in range(0, len(self.data['result']), +1):
            Code = int(self.data['result'][OnlineIddaa]['C'])
            HTTR, ATTR = str(self.data['result'][OnlineIddaa]['HTTR'].encode('Utf-8')), str(self.data['result'][OnlineIddaa]['ATTR'].encode('Utf-8'))
            self.liste[Code] = {"HTTR":HTTR, "ATTR":ATTR}
        return self.liste
