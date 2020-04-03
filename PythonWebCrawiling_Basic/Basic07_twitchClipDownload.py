# 7. 트위치 클립 다운로드 - 파이썬 레시피 웹 활용 입문편
# https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie

#클립 영상 소스링크
#-> 트위치 클립은 <video>태그에 src 속성을 확인하면 된다.
#-> 이번에는 추출할 요소의 태그가 명확하기 때문에 find_elements_by_name을 사용한다.
#-> selenium에서 추출한 요소의 속성값을 확인하기 위해 get_attribute를 사용한다.

from selenium import webdriver
import time
import re
from urllib.request import urlretrieve


# 크롬창 설정
#selenium을 통해 드라이버를 불러오기 전 여러가지 옶션을 줄 수 있다.
#-> headless 를 추가혐ㄴ 크롬창이 나타지않는다.
#-> os 환경이나 화면 크기를 지정할 수 있다.
#-> 접속환경 변경 시 실행결과가 달라질 수 있다.
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x108')
options.add_argument('user-agent=Chrome/80.0.3987.106')
driver = webdriver.Chrome('chromedriver' , options=options)

#특정클립 링크
driver.get('https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie')

time.sleep(3)

#video 태그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)

#영상 제목과 날짜
#-> 영상의 제목과 날짜를 추출한다.
#-> 2가지를 이용해서 파일명을 만든다.
title_element1 = driver.find_element_by_class_name('tw-flex')
title_element2 = title_element1.find_elements_by_tag_name('span')
#print(title_element2)
vid_title, vid_date = None, None
for span in title_element2:
    try:
        d_type = span.get_attribute('data-test-selector')
        #print(d_type)
        if d_type == 'title':
            #print(span.text)
            vid_title = span.text
        elif d_type == 'date':
            #print(span.text)
            vid_date = span.text
    except:
        pass

print(vid_title,'\t',vid_date)


#영상 다운로드
#-> 파일명으로 사용하기 위해 특수문자와 빈칸 없애기
#-> import re 참조
vid_title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_title)
vid_date = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_date)
print(vid_title,'\t',vid_date)

#-> from urllib.request import urlretrieve 참조
#-> 영상을 실제로 다운로드
urlretrieve(vid_url, vid_title+'_'+'.mp4')

driver.close()
