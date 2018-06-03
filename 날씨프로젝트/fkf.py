from urllib.request import Request
from urllib.request import urlopen
from urllib.parse   import quote_plus
from urllib.parse import urlencode
import  xml.etree.ElementTree as ET

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
sidoName = input("시도이름")

queryParams = '?' + urlencode(
    {quote_plus(
        'ServiceKey'): '3VBoDPGPgJs5RX5aeKkM/aR9pe/zaMePqelfkZcIzEM9w+FHrMEAXR0cKMlMxK8YvBKGr1vbvaTwz3+dULIwvQ==',
     quote_plus('numOfRows'): '10', quote_plus('pageNo'): '1',
     quote_plus('sidoName'): sidoName, quote_plus('ver'): '1.3'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
filename="mise.xml"
f=open(filename,"wb")
f.write(response_body)
f.close()

tree=ET.parse(filename)
root=tree.getroot()

for a in root.findall('.//item'):
    print("측정일 :",a.findtext("dataTime"))
    print("도시 이름 :",a.findtext("stationName"))
    print("일산화탄소량 :",a.findtext("coValue"))
    print("미세먼지 농도 :",a.findtext("pm25Value") +"ug")
    print("아황산가스 지수 :",a.findtext("so2Grade"))
    print("이산화질소 지수 :",a.findtext("no2Grade"))

# 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종 을 클릭하면
# 바운딩박스에 동네 이름들이 뜨고, 특정 도시이름을 선택하면 그 도시의 대기오염정보띄워준다.
# 그리고, 대기오염정보를 이메일로 보낼 수 있도록 한다.