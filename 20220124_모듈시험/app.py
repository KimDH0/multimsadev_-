# pip install flask 설치 진행
# API 요청 할 pip install requests

from flask import Flask
import json
import requests


# 변수 선언 - 프로그램의 이름 저장하는 변수(파일 이름 저장 변수)
# application server 개발 app 변수를 많이 사용
app = Flask(__name__) # flask 프로그램 시작 기본 값은 = app.py 파일을 생성

#함수 선언 
# 시작할 때 경로(route) 선언해야함
@app.route("/") # 웹 사이트 경로를 지정 - 앞에서 선언한 app 변수를 사용
def FlaskLab(): # 요청 - 메서드(함수) 이름 요청에서 사용하는 것
    return "Flask 데이터 응답" # 응답 -  return 에서 돌려주는 데이터가 응답

@app.route("/data1")
def FlaskData(startPage, pageCount, address): # 요청 받음
    keyValue = r"Vbg6Bf8TjEx6qxVQolGEzVlx4sKid9OEu%2FO1tlqazIwGNBm6C3lcKTanaP3KT8G6aNXUS3Qjs3%2Bj%2F3%2FwheM4pw%3D%3D"   

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond" + "%5BorgZipaddr%3A%3ALIKE%5D=%EA%B0%95%EB%82%A8%EA%B5%AC" #강남구
    dataURL += "&serviceKey=" + keyValue
    
    dataResult = requests.get(dataURL)
    #공공데이터 요청 후 데이터 받기 : flask - request / requests 기능 사용"

    return json.loads(dataResult) # 공공데이터 결과 값 응답