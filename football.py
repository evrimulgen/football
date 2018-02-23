import urllib
class Code(object):
    def __init__(self, code):
        self.dict = {}
        self.code = str(code)
        self.url = "http://istatistik.nesine.com/HeadToHead/Index.aspx?matchCode=" + self.code
        self.stand = 'deltaStand.png'
        socket = urllib.urlopen(self.url)
        self.source = socket.readlines()
        #for e, test in enumerate(self.source, 1):
        #    search = "<div class='posNormal'>"
        #    if test.find(search) is not -1:
        #        print self.getstr(test, ">","<")
        #        print self.source[e+1]
        #        print self.source[e+3]
        #        print self.source[e+17]
        #print self.source
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
print get.Teams()["Ev"], get.Count(), get.weather()
        
        
        
        
        
