## 4. 유튜브 키워드 검색 - 파이썬 레시피 웹 활용 입문편


#Selenium?
#다양한 브라우저 및 플랫폼에서 웹 응용프로그램을 위한 자동화 테스트 스위트이다.
#웹 기반 응용 프로그램을 자동화하는 데 중점을 둔다.
#단 하나의 도구가 아니라 소프트웨어의 모음이다.
#여러 언어에서 웹 자동화 테스트 및 웹 자동화를 도와주는 라이브러리이다.

#Selenium 설치
#sudo apt-get update // 사용가능한 패키지와 그 버전들의 리스트를 업데이트
#sudo pip3 install selenium

#유튜브 검색을 위해 chrome과 chrome 드러이버 설치

#크롬설치
#->인증키 등록
#sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
#->크롬 브라우저 다운받을 PPA 추가 (/etc/apt/sources.list.d)
#sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
#->PPA 추가 후 apt-get update 하여 리스트 갱신
#sudo apt-get update
#->크롬 브라우저 설치
#sudo apt-get install google-chorme-stable
#-> 설치완료후 google.list 파일 삭제
#sudo rm -rf /etc/apt/sources.list.d/google.list
#-> apt manager 가 다운 받은 설치파일을 삭제
#sudo apt-get clean
#-> apt-get update 로 정상적으로 설치되었는지 확인
#sudo apt-get update

#크롬 드라이버 설치
#-> 크롬 버전확인
#google-chrome --version
#-> 버전에 맞는 크롬 드라이버 다운로드
#sudo wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
#-> 크롬 드라이버 압축풀기
#sudo unzip chromedriver_linux64
#-> 크롬 드라이버 이동하여 실행 권한 주기
#-> 자동화를 위해 chromedriver와 파이썬 파일을 같은 폴더에 놓는다.
#sudo mv chromedriver /var/www/html/pythonTut/basic
#sudo chown root:root /var/www/html/pythonTut/basic
#sudo chmod +x /var/www/html/pythonTut/basic



#검색 키워드 자동입력
#->유튜브 키워드 검색창의 경로를 알아보자.
#->selenium에서는 대체로 xpath로 경로를 계산하여 요소를 탐색한다.

#크롬 개발자도구로 검색창의 xpath를 알아보자.
#유튜브 검색창 우클릭 -> 검사 -> 검사 영역 우클릭 -> copy -> copy xpath
 #결과값 -> //*[@id="search"]
 # xpath 안돼서 name 으로 진행

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.youtube.com/')

wait = WebDriverWait(driver,10)
time.sleep(3)



#검색어 창을 찾아 search 변수에 저장
#search = driver.find_element_by_xpath('//*[@id="search"]/input')
# xpath 안됨....
search = driver.find_element_by_name('search_query')


#search 변수에 저장된 곳에 값을 전송
search.send_keys('we bare bears')
time.sleep(1)

#Enter 전송
#-> 엔터 혹은 방향키와 같이 특수한 키는 다음과 같이 입력한다.
#-> from selenium.webdriver.common.keys import Keys 참조
#-> search.send_keys(Keys.원하는키)
#-> Keys.ARROW_DOWN, Keys.ENTER, Keys.SPACE ...
#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)
