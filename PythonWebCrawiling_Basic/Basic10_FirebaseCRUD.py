# 10. 파이어베이스로 crud 구현하기 - 파이썬 레시피 웹 활용 입문편

#설치
#sudo pip3 install firebase-admin

# 프로젝트 생성
# https://firebase.google.com/?hl=ko

#Realtime Database
#-> key, value 생성 (다중)

#키생성
# 사용자 및 권한 -> 설정 -> firebase admin sdk -> python -> 새비공개키 생성

#인증
#-> 발급시 예시를 참고하여 인증코드 작성
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pprint import pprint

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://androidsample-815f5.firebaseio.com/'
})

# db 위치지정
ref = db.reference()

# 해당 변수가 없으면 생성
ref.update({'kim':'developer'})

# 해당 경로가 없으면 생성한다.
ref = db.reference('Python Tutorial/Firebase')
ref.update({'Firebase Admin':'firebase.google.com'})
ref.update({'Firebase Realtime Database':'Create multi key, value '})
ref.update({'Firebase Key':'Create python key'})

#db 위치지정
ref = db.reference()
#해당 리스트가 없으면 생성한다.
ref.update({'Python Course':['생활코딩 WEB2 python','Jump to python','python 레시피-입문','python 레시피-승급']})


# 데이터 조회하기
#없는경로 조회하기
ref = db.reference('php')
pprint(ref.get())

#key -> value
ref = db.reference('kim')
pprint(ref.get())

#다중 key -> value
ref = db.reference('Python Tutorial/Firebase')
pprint(ref.get())

#리스트
ref = db.reference('Python Course')
pprint(ref.get())
