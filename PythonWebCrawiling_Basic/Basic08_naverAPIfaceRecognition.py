# 8. 네이버 얼굴인식 API 사용하기 - 파이썬 레시피 웹 활용 입문편

import os
import sys
import requests
import json

# 기본
# 파이썬 예제가 제공된다.
# https://developers.naver.com/docs/clova/api/CFR/API_Guide.md#Python
# 주석이 // 로 되어있기 때문에 변경해준다.
# client_id와 client_secret에 네이버 개발자 애플리케이션 id와 secret을 입력한다.
client_id = 'hYU0kQ0W3w2VnRBgEUAo'
client_secret = 'wpPHo8fHDh'
#url = 'https://openapi.naver.com/v1/vision/face'#얼굴감지
#files = {'image': open('the-weekend.jpg', 'rb')}
url = "https://openapi.naver.com/v1/vision/celebrity" #유명인 얼굴인식
files = {'image': open('who-is-it.jpg', 'rb')}
headers = {'X-NAVER-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code


if(rescode==200):
    #응답받은 데이터 활용
    #-> 응답은 json 형식의 문자열로 온다.
    #-> import json 을 참조하여 json 모듈의 loads 함수를 통해 변환하여보자.
    #print(response.text)
    data = json.loads(response.text)
    faceCount = data['info']['faceCount']
    data1 = data['faces'][0]
    celebrity = data1['celebrity']['value']
    print('감지된 얼굴 수: ' + format(faceCount))
    print('사진속 인물: ',celebrity)
else:
    print('Error Code: ' + rescode)
