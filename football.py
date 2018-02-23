import urllib
class Code(object):
    def __init__(self, code):
        self.code = str(code)
        self.delta, self.posHTTR, self.posATTR, self.points = [], "", "", []
        self.dict, self.posDict, self.deltaDict = {}, {}, {}
        self.url = "http://istatistik.nesine.com/HeadToHead/Index.aspx?matchCode=" + self.code
        socket = urllib.urlopen(self.url)
        self.source = socket.readlines()
        #print self.source
    def pos(self):
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
                self.points.append(points)
                string = self.source[e+3]
                if string.find(self.Teams()["Ev"]) is not -1:
                    self.posHTTR = pos
                if string.find(self.Teams()["Konuk"]) is not -1:
                    self.posATTR = pos
        self.posDict["pos"] = {"HTTR":self.posHTTR, "ATTR":self.posATTR}
        self.posHTTR = int(self.posHTTR)
        self.posATTR = int(self.posATTR)
        self.posDict["delta"] = {"HTTR":self.delta[self.posHTTR-1], "ATTR":self.delta[self.posATTR-1]}
        self.posDict["points"] = {"HTTR":self.points[self.posHTTR-1], "ATTR":self.points[self.posATTR-1]}
        return self.posDict
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
        self.dict = {"Ev":Teams[0], "Konuk":Teams[1]}
        return self.dict 

get = Code(225)
#print get.Teams()["Ev"], get.Count(), get.weather()["stat"]
print get.pos()
        
        
        
  
