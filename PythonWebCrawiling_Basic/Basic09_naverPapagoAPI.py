# 9. 네이버 파파고 API 사용하기 - 파이썬 레시피 웹 활용 입문편

# papago API 는 2가지 서비스가 있다.
#-> NMT(Neural Machine Translation) : 인공 신경망 기반 기계번역
#-> SMT(Statistical Machine Translation) : 통계 기반 기계 번역

# NMT : https://developers.naver.com/products/nmt/

#기본예제

import os
import sys
import urllib.request
import json
import requests

client_id = 'hYU0kQ0W3w2VnRBgEUAo'
client_secret = 'wpPHo8fHDh'

# 메모장 내용 변경
# -> 한글이 쓰여진 메모장 txt 파일을 번역하여 새로운 메모파일을 생성한다.
# -> 원본은 source.txt 번역본은 translate.txt 로 생성한다.
with open('source.txt','r',encoding='utf8') as f:
    srcText = f.read()

#encText = urllib.parse.quote('전혀 예상 못했어.')
encText = urllib.parse.quote(srcText)
data = 'source=ko&target=en&text=' + encText
url = 'https://openapi.naver.com/v1/papago/n2mt'
request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id',client_id)
request.add_header('X-Naver-Client-Secret',client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))

    #응답 데이터로 메모파일 생성
    #json 형 변환
    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    pprint(res)

    #파일생성
    with open('translate.txt','w',encoding='utf8') as f:
        f.write(res['message']['result']['translatedText'])

else:
    print('Error Code:' + rescode)

# urllib모듈이 아닌 requests 모듈로 요청하기
# import requests 참조
headers = {'X-Naver-Client-Id':client_id,
           'X-Naver-Client-Secret':client_secret}
testData = {'source':'ko',
            'target':'en',
            'text':'안녕하세요'.encode('utf-8')}
res = requests.post(url,data=testData,headers=headers)
#print(res.status_code)
pprint(res.json())
