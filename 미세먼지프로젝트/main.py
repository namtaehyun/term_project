import urllib.request
from tkinter import *
import json

print("1.Seoul 2.Incheon 3.Wonju 4.Busan 5.Daegu 6.Daejeon 7.Jeonju 8.Gwangju 9.Ulsan 10.Yeosu 11.Kang-neung 12.Jeju")

while True:
    city=['Seoul','Incheon','Wonju','Busan','Daegu','Daejeon','Jeonju','Gwangju','Ulsan','Yeosu','Kang-neung','Jeju']

    n= input("도시 선택 :")
    n=int(n)
    if(n==0 or n>12):
        print("wrong number")
    elif n==13:
        print("Exit Program")
        break
    else:
        city=city[n-1]
        url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&APPID=f2a4cd151d30cad7c8721aa75cf0d078'
        data = urllib.request.urlopen(url).read()
        j = json.loads(data)
        print(city+" is "+j['weather'][0]['main'])
        print("최고기온 : "+str(j['main']['temp_max']-273.15)+".c")
        print("최저기온 : "+str(j['main']['temp_min']-273.15)+".c")
        print("경도 : "+str(j['coord']['lat']))
        print("위도 : " + str(j['coord']['lon']))
        print("풍속 : " + str(j['wind']['speed'])+"m/s")
        print("습도 : "+str(j['main']['humidity']))