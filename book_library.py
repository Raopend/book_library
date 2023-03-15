import requests
import json
import datetime

# 获取 token
def get_token(student_number: str, password:str):
    url = "https://leosys.cn/cczukaoyan/rest/auth"
    querystring = {"username": student_number, "password": password}
    headers = {
        "Host": "leosys.cn",
        "Accept": "*/*",
        "actCode": "true",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://servicewechat.com/wx8adafd853fc21fd6/58/page-frame.html",
        "user_ip": "1.1.1.1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
        "Connection": "keep-alive",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
        "content-type": "multipart/form-data"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()['data']
    return data['token']

# 获得可选座位
def get_seat_available(token: str):
    url = "https://leosys.cn/cczukaoyan/rest/v2/searchSeats/2023-03-16/900/1020"
    querystring = {"roomId": "2", "batch": "999", "page": "1"}

    headers = { 
        "Host": "leosys.cn",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "token": token,
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
        "Referer": "https://servicewechat.com/wx8adafd853fc21fd6/58/page-frame.html",
        "user_ip": "1.1.1.1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
        "Connection": "keep-alive",
        "content-type": "multipart/form-data"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()['data']
    return data['seats']

# 选座位
def book_seat(seat_id: str, token: str, book_time: str):
    url = "https://leosys.cn/cczukaoyan/rest/v2/freeBook"
    payload = {
        "seat": seat_id,
        "date": book_time,
        "startTime": "1260",
        "endTime": "1320",
        "authid": None
    }
    data = json.dumps(payload)
    headers = {
        "Host": "leosys.cn",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "token": token,
        "Content-Length": "60",
        "Referer": "https://servicewechat.com/wx8adafd853fc21fd6/58/page-frame.html",
        "user_ip": "1.1.1.1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
        "Connection": "keep-alive",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
        "content-type": "multipart/form-data"
    }
    response = requests.request("POST", url, data=data, headers=headers)

if __name__ == "__main__":
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")

    token = get_token(student_number="", password="")
    seat_available = get_seat_available(token=token)
    for key, value in seat_available.items():
        if value['name'] > '020':
            book_seat(seat_id=value['id'], token=token, book_time=current_time)
            break

