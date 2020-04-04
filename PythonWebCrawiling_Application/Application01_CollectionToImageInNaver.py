# 1. 네이버 이미지 수집 Application - 파이썬 레시피 웹 활용 승급편

# Application 소개
# 네이버 사이트 이미지 탭을 이용하여, 검색한 키워드와 관려된 사진을 수집한다.
# 다운받은 사진들을 압축파일로 변환한다.

# 키워드 검색 자동화 -> 이미지 다운로드 -> 폴더생성

# tqdm 설치 - 텐서플로우 진행상태 표시하는 툴
# sudo pip3 install tqdm

#사이트 접속 -> 키워드 검색
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

keyword = '드웨인존슨'

# 1. 웹 접속 - 네이버 이미지 접속
print('Loading...')
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(30)

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
driver.get(url)

# 1.5 페이지 스크롤 다운 - 페이지를 스크롤 하여 더 많은 사진을 수집한다.
# -> 1초에 한번씩 10번 반복하여 페이지 다운 스크롤을 한다.
body = driver.find_element_by_css_selector('body')
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# 2. 이미지 링크 수집
imgs = driver.find_elements_by_css_selector('img._img')
result = []
for img in imgs:
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
#print(result)

driver.close()
print('Colloections complete!')


# 3. 폴더생성
import os
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))
    print('Create new directory!')
else :
    print('Image updates!')

#4. 이미지 순서대로 다운로드
from urllib.request import urlretrieve
for index, link in tqdm(enumerate(result)):
    start = link.rfind('.')
    end = link.rfind('&')
    #print(link[start:end])
    filetype = link[start:end] #.png
    urlretrieve(link, './{}/{}{}{}'.format(keyword,keyword,index,filetype))
print('Download complete!')
