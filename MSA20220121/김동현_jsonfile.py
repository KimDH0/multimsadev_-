import json

try:
    jsonFile = open("datalab\\mydata.json", "rb")
    tempData = json.load(jsonFile)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
except Exception:
    error = str(ex)
finally:
    pass


jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

#2번 
try:
    writeFile = open("datalab\\mydata2.json", "w")
    json.dump(jsonData1, writeFile)
except Exception:
    error = str(ex)
finally:
    pass

#3번
try:
    writeFile = open("datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False)
except Exception:
    error = str(ex)
finally:
    pass

#4번
try:
    writeFile = open("datalab\\mydata4.json", "w")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except Exception:
    error = str(ex)
finally:
    pass

#5번
try:
    writeFile = open("datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except Exception:
    error = str(ex)
finally:
    pass

#디버깅 변수 선언함(임시)
temp = 0
