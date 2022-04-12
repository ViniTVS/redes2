import re
from datetime import datetime
import requests

class Entrada:
    __temp = None
    __local = ""
    __link = ""
    __last_upd = 0
    # Construtor da Entrada
    def __init__(self, local, link = None):
        self.__local = local;
        if (link == None or link == ""):
            self.__link = "https://wttr.in/" + local
        else:
            self.__link = link

        res = requests.get(self.__link + "?format=\"%t\"")
        print(int(re.findall('[\+\-]?[0-9]+', res.text)[0]))
        self.__last_upd = datetime.now()

    def updateTemp(self):
        t_now = datetime.now()
        t_delta = t_now - self.__last_upd
        return
        if (t_delta.total_seconds() < 30):
            return

        res = requests.get(self.__link)
        print(res.text)
        s = '-5+2y'
        now = datetime.now()
        print(now)
        result = int(re.findall('[\+\-]?[0-9]+', s)[0])
        print(result)
        self.__temperatura = 0
        print(self.__temperatura)