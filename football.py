#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from CodeList import dict
#print dict().test()
class Code(object):
    def __init__(self, code):
        self.code = str(code)
        self.delta, self.posHTTR, self.posATTR, self.points, self.ligText = [], "", "", [], ""
        self.averageList = []
        self.dict, self.posDict, self.deltaDict = {}, {}, {}
        url = "http://istatistik.nesine.com/HeadToHead/Index.aspx?matchCode=" + self.code
        socket = urllib.urlopen(url)
        self.source = socket.readlines()
        #print self.source
        self.zero = 0
    def generic(self):
        for e, test in enumerate(self.source, 1):
            search = "<div class='posNormal'>"
            if test.find(search) is not -1:
                pos = self.getstr(test, ">","<")
                if self.source[e+1].find("deltaStand") is not -1:
                    self.delta.append("Stand")
                elif self.source[e+1].find("deltaDown") is not -1:
                    self.delta.append("Down")
                elif self.source[e+1].find("deltaUp") is not -1:
                    self.delta.append("Up")
                points = self.getstr(self.source[e+17], ">", "<")
                self.averageList.append(int(self.getstr(self.source[e+15], ">", "<")))
                print self.getstr(self.source[e+15], ">", "<")
                self.points.append(points)
                string = self.source[e+3]
                if string.find(self.Teams()["HTTR"]) is not -1:
                    self.posHTTR = pos
                if string.find(self.Teams()["ATTR"]) is not -1:
                    self.posATTR = pos
        self.posDict["Pos"] = {"HTTR":self.posHTTR, "ATTR":self.posATTR}
        self.posHTTR = int(self.posHTTR)
        self.posATTR = int(self.posATTR)
        self.posDict["TEAMS"] = {"HTTR":get.Teams()["HTTR"],  "ATTR":get.Teams()["ATTR"]}
        self.posDict["Delta"] = {"HTTR":self.delta[self.posHTTR-1], "ATTR":self.delta[self.posATTR-1]}
        self.posDict["Point"] = {"HTTR":self.points[self.posHTTR-1], "ATTR":self.points[self.posATTR-1]}
        self.posDict["Weather"] = {"Stat":get.weather()["stat"].decode("utf-8"), "Temp":get.weather()["c"]}
        self.posDict["Kral"] = {"point":self.points[self.zero]}
        self.posDict["Ts"] = {"count":self.Count()}
        self.posDict["Lig"] = {"Lig":self.lig()}
        self.posDict["Averaj"] = {"HTTR":self.averageList[self.posHTTR-1], "ATTR":self.averageList[self.posATTR-1],
        "Fark":self.averageList[self.posHTTR-1]+self.averageList[self.posATTR-1]}
        return self.posDict
    def lig(self):
        for test in self.source:
            search = "leagueTableTeamHeader"
            if test.find(search) is not -1:
                self.ligText = self.getstr(test, ">", "<").split("/")[0]
        return self.ligText
    def weather(self):
        for enum, test in enumerate(self.source,1):
            search  = '<div class="desc">'
            if test.find(search) is not -1:
                stat = self.source[enum].strip()
                c = self.source[enum+1].replace(" ","").replace("(","").replace(")","")
        self.dict = {"stat":stat, "c":c}
        return self.dict
    def getstr(self, source, start, end):
        get = source.find(start) +1
        output = source.find(end, get)
        return source[get:output]
    def Count(self):
        for test in self.source:
            search = "<div class='posNormal'>"
            if test.find(search) is not -1:
                count = self.getstr(test, ">", "<")
        return int(count)
    def Teams(self):
        for test in self.source:
            search = 'Nesine - ' + self.code + ' Kodlu'
            if test.find(search) is not -1:
                Teams = test.strip()[len(search):].replace("Maçı","").replace(" - ","-").strip().split("-")
        self.dict = {"HTTR":Teams[0], "ATTR":Teams[1]}
        return self.dict
string = """Ligin {}. sırasında olan {}. sıradaki ev sahibi {} takımı
evinde {}.sıradaki {} takımını konuk ediyor. Ev sahibi ile aralarında {} puan
farkı olan {} takımı """
#string = string.format("test")

get = Code(623)
#print get.Teams()["HTTR"], get.Count(), get.weather()["Stat"], get.weather()["Temp"]
print get.generic()
