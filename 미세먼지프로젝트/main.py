import urllib.request
import json
import pytz
import datetime
#인증키 EnpWcha8fRqol4EYvjGbsX7bq2DrzonbZ8J1C2VVoaps5xWVV%2BPdPLJZwvuVUzCoWNfEAhB7HamhWFDT3bh3ew%3D%3D

def get_api_date():
    standard_time = [2, 5, 8, 11, 14, 17, 20, 23]
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')                     #국제시간(서울)
    check_time = int(time_now) - 1
    day_calibrate = 0
    while not check_time in standard_time:
        check_time -= 1
        if check_time < 2:
            day_calibrate = 1
            check_time = 23
    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')                 #국제시간
    check_date = int(date_now) - day_calibrate

    return (str(check_date), (str(check_time) + '00'))
# YYYYMMDD, tt+00 형태로 반환함. 2017년 6월30일 오후 17시라면, 20170630,1700이 반환됨.

def get_weather_data():
    api_date, api_time = get_api_date()
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    key = "serviceKey=" + "EnpWcha8fRqol4EYvjGbsX7bq2DrzonbZ8J1C2VVoaps5xWVV%2BPdPLJZwvuVUzCoWNfEAhB7HamhWFDT3bh3ew%3D%3D"
    date = "&base_date=" + api_date
    time = "&base_time=" + api_time
    nx = "&nx=97"                           # 경도
    ny = "&ny=76"                           # 위도
                                             # 내가 사용하고싶은 지역의 위도와 경도를 알아야한다.
    numOfRows = "&numOfRows=100"
    type = "&_type=json"
    api_url = url + key + date + time + nx + ny + numOfRows + type

    data = urllib.request.urlopen(api_url).read().decode('utf8')
    data_json = json.loads(data)

    parsed_json = data_json['response']['body']['items']['item']

    target_date = parsed_json[0]['fcstDate']  # get date and time
    target_time = parsed_json[0]['fcstTime']

    date_calibrate = target_date  # date of TMX, TMN
    if target_time > 1300:
        date_calibrate = str(int(target_date) + 1)

    passing_data = {}
    for one_parsed in parsed_json:
        if one_parsed['fcstDate'] == target_date and one_parsed['fcstTime'] == target_time:  # get today's data
            passing_data[one_parsed['category']] = one_parsed['fcstValue']

        if one_parsed['fcstDate'] == date_calibrate and (
                one_parsed['category'] == 'TMX' or one_parsed['category'] == 'TMN'):  # TMX, TMN at calibrated day
            passing_data[one_parsed['category']] = one_parsed['fcstValue']

    return passing_data


if __name__ == '__main__':
    print(get_weather_data())



