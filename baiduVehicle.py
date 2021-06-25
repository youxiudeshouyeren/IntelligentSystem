#http://api.map.baidu.com/traffic/v1/road?road_name=%E4%B8%9C%E4%BA%8C%E7%8E%AF&city=%E5%8C%97%E4%BA%AC%E5%B8%82&ak=ewX4YgbE15522PhUgN4sQ9pO7KUq7FEX
import json
import random
from time import sleep

import requests


class StartShow():
    def __init__(self):
        pass
    # 返回ns_num南北车的数量，we_num东西车的数量
    #ak=
    def get_status(self):
        url = "http://api.map.baidu.com/traffic/v1/road?road_name=顺城大街&city=成都市&ak=ewX4YgbE15522PhUgN4sQ9pO7KUq7FEX"
        data = {}
        res = requests.get(url=url, data=data,timeout=10)
        mes_to_dict = json.loads(res.text)
        print(mes_to_dict)
        print(mes_to_dict["description"])
        status = mes_to_dict["evaluation"]
        ns_num=0
        if status["status"]==0:
            ns_num=random.randint(0,10)
        if status["status"]==1:
            ns_num=random.randint(5,15)
        if status["status"]==2:
            ns_num=random.randint(10,20)
        if status["status"]==3:
            ns_num=random.randint(15,25)
        if status["status"]==4:
            ns_num=random.randint(20,30)
        print(status)
        res.close()

        url = "http://api.map.baidu.com/traffic/v1/road?road_name=蜀都大道人民东路&city=成都市&ak=ewX4YgbE15522PhUgN4sQ9pO7KUq7FEX"
        data = {}
        res = requests.get(url=url, data=data,timeout=10)
        mes_to_dict = json.loads(res.text)
        print(mes_to_dict["description"])
        status = mes_to_dict["evaluation"]
        we_num = 0
        if status["status"]==0:
            we_num=random.randint(0,10)
        if status["status"]==1:
            we_num=random.randint(5,15)
        if status["status"]==2:
            we_num=random.randint(10,20)
        if status["status"]==3:
            we_num=random.randint(15,25)
        if status["status"]==4:
            we_num=random.randint(20,30)
        print(status)
        res.close()
        return ns_num,we_num

if __name__ == '__main__':
    status=StartShow()
    while 1:
        ns,we=status.get_status()
        print(ns,we)
        sleep(1)
