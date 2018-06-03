import game_framework
import urllib.request
from tkinter import *
import json
import  smtplib
from tkinter import font
from email.mime.text import  MIMEText
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse   import quote_plus
from urllib.parse import urlencode
import  xml.etree.ElementTree as ET

name = "Main"

def enter():
    global city
    pass

def exit():
    pass

def ShowCityInfo(text):
    url='http://api.openweathermap.org/data/2.5/weather?q='+text+'&mode=json&APPID=f2a4cd151d30cad7c8721aa75cf0d078'
    data = urllib.request.urlopen(url).read()
    j = json.loads(data)
    print(text+" is "+j['weather'][0]['main'])
    print("최고기온 : "+str(j['main']['temp_max']-273.15)+".c")
    print("최저기온 : "+str(j['main']['temp_min']-273.15)+".c")
    print("경도 : "+str(j['coord']['lat']))
    print("위도 : " + str(j['coord']['lon']))
    print("풍속 : " + str(j['wind']['speed'])+"m/s")
    print("습도 : "+str(j['main']['humidity']))
    window = Tk()
    window.title(text)
    window.geometry('400x400+10+10')  # width x height + 세로격자+가로격자
    l1 = Label(window,text="최고기온 : "+str(j['main']['temp_max']-273.15)+".c")
    l2 = Label(window,text="최저기온 : "+str(j['main']['temp_min']-273.15)+".c")
    l3 = Label(window,text="경   도 : "+str(j['coord']['lat']))
    l4 = Label(window,text="위   도 : "+ str(j['coord']['lon']))
    l5 = Label(window,text="풍   속 : "+ str(j['wind']['speed'])+"m/s")
    l6 = Label(window,text="습   도 : "+str(j['main']['humidity']))
    e1 = Entry(window)
    l1.grid(row = 0,column = 0)
    l2.grid(row = 1,column = 0)
    l3.grid(row = 2,column = 0)
    l4.grid(row = 3,column = 0)
    l5.grid(row = 4,column = 0)
    l6.grid(row = 5,column = 0)
    e1.grid(row=6,column =0)

    button1 = Button(window, text="메일 보내기",command=lambda t=text: sendMail('nth0310@gmail.com', e1.get() ,text+"\n최고기온 : "+str(j['main']['temp_max']-273.15)+".c\n"+"최저기온 : "+str(j['main']['temp_min']-273.15)+".c\n"+"경   도 : "+str(j['coord']['lat'])+"\n위   도 : "+ str(j['coord']['lon'])+"\n풍   속 : "+ str(j['wind']['speed'])+"m/s"+"\n습   도 : "+str(j['main']['humidity'])))
    button1.place(x=130, y=120)

    window.mainloop()


def sendMail(me, you, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, 'supoudodmwburakq')
    msg = MIMEText(msg)
    msg['Subject'] = '날씨정보'
    smtp.sendmail(me, you, msg.as_string())
    smtp.quit()

def run():
    global window
    window = Tk()
    window.title('기상정보')
    window.geometry('690x900')  # width x height + 가로격자+세로격자

    map = 'map.png'
    img = PhotoImage(file=map)

    map_label = Label(window, image=img)
    map_label.pack()

    button1 = Button(window, text="서울",command=lambda t="Seoul": ShowCityInfo(t))
    button1.place(x=326, y=442)

    button2 = Button(window, text='인천',command=lambda t="Incheon": ShowCityInfo(t))
    button2.place(x=280, y=471)

    button3 = Button(window, text='대전',command=lambda t="Daejeon": ShowCityInfo(t))
    button3.place(x=358, y=571)

    button4 = Button(window, text='대구',command=lambda t="Daegu": ShowCityInfo(t))
    button4.place(x=460, y=619)

    button5 = Button(window, text='광주',command=lambda t="Kwangju": ShowCityInfo(t))
    button5.place(x=314, y=694)

    button6 = Button(window, text='울산',command=lambda t="Ulsan": ShowCityInfo(t))
    button6.place(x=520, y=652)

    button7 = Button(window, text='부산',command=lambda t="Busan": ShowCityInfo(t))
    button7.place(x=503, y=692)

    button8 = Button(window, text='제주',command=lambda t="Jeju": ShowCityInfo(t))
    button8.place(x=246, y=872)

    button9 = Button(window, text='평양',command=lambda t="Pyongyang": ShowCityInfo(t))
    button9.place(x=224, y=281)

    button10 = Button(window, text='강릉',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=446, y=399)

    button10 = Button(window, text='경기',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=336, y=485)

    button10 = Button(window, text='강원',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=432, y=432)

    button10 = Button(window, text='충북',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=304, y=565)

    button10 = Button(window, text='충남',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=370, y=540)

    button10 = Button(window, text='전북',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=308, y=646)

    button10 = Button(window, text='전남',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=290, y=751)

    button10 = Button(window, text='경북',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=463, y=572)

    button10 = Button(window, text='경남',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=412, y=685)

    button10 = Button(window, text='세종',command=lambda t="Kang-neung": ShowCityInfo(t))
    button10.place(x=333, y=546)




    window.mainloop()


def pause():
    pass


def resume():
    pass







