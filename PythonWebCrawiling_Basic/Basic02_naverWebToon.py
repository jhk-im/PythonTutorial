# 2. 네이버 웹툰 제목 가져오기 - 파이썬 레시피 웹 활용 입문편

from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()


#요일별 모든웹툰 표시 영역 추출
data1 = soup.find('div',{'class':'col_inner'})
#pprint(data1)


#findAll을 이용해여 a태그의 class="title" 을 검사하여 제목텍스트 추출준비
#제목 포함영역 추출
data2 = data1.findAll('a',{'class':'title'})
#pprint(data2)


#title의 text만 추출한다.
#for를 이용한 텍스트 추출 1
title_list1 = []
for t in data2:
    title_list1.append(t.text)
#pprint(title_list1)

#for를 이용한 텍스트 추출 2
title_list2 = [t.text for t in data2]
#pprint(title_list2)



# 현재까지는 모든 요일의 웹툰 제목을 가져온다.
# [웹툰표시영역 find] -> [해당 영역의 모든 title findAll] -> [for문 제목 추출]
# 이제는 다음과 같은 과정을 거치게 된다.
# [요일별 웬툰영역 find] -> [해당 영역의 모든 title findAll] -> [for문 제목 추출]



#요일별로 웹툰영역 구분해서 추출
#data1 과는 다르게 findAll을 사용한다.
data_list = soup.findAll('div',{'class':'col_inner'})

#추출된 각각의 제목들을 하나의 리스트로 묶는다.
week_title_list = []

#for 문으로 각각의 요일을 구분해서 데이터를 추출한다.
for divisionData1 in data_list:
    #제목 포함영역 추출
    divisionData2 = divisionData1.findAll('a',{'class':'title'})
    #pprint(divisionData2)

    #텍스트만 출력
    title_list3 = [t.text for t in divisionData2]
    #pprint(title_list3)
    #week_title_list.extend(title_list3) 1차원
    week_title_list.append(title_list3)

pprint(week_title_list)
#week_title_list 안에 요일별로 2차원 리스트가 작성된다. 
