# 3. 네이버 웹툰 썸네일 가져오기 - 파이썬 레시피 웹 활용 입문편

from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
# 이미지 혹은 동영상의 링크를 통해 다운로드 구현
from urllib.request import urlretrieve

# 저장폴더 생성
# 자동으로 img 폴더를 생성하고 그곳에 저장시키도록 한다.
# os 모듈 사용
# os.path.isdir -> 이미 해당 디렉토리가 있는지 검사
# os.path.join -> 현재 경로에 입력된 text를 더하여 새로운 경로 생성
# os.makedirs -> 입력된 경로에 디렉토리 생성
try:
    if not(os.path.isdir('webtoon_image')):
        os.makedirs(os.path.join('webtoon_image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패")
        exit()

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#요일별 웹툰영역 추출하기
data_list=soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

# 전체 웹툰 리스트에서 제목 + 썸네일 영역을 추출하여 담는다.
li_list = []
for data in data_list:
    #제목 + 썸네일 영역 추출
    li_list.extend(data.findAll('li'))

#pprint(li_list)

#src -> img 태그와 title -> 제목이 추출된다.
#이제 추출한 src과 title 데이터에 속성명을 부여한다.
for li in li_list:
    # image 표시영역 찾기
    img = li.find('img')
    # image 표시영역의 title 값
    title = img['title']
    # image 표시영역의 src 값
    img_src = img['src']

    # 이미지 다운로드시 에러해결
    # 추출한 제목에서 특수문자가 있을 경우 에러가 발생한다.
    # 따라서 추출한 제목에서 특수문자를 다른문자로 변경하거나 삭제하도록 한다.
    # param1 -> 기준값
    # param2 -> 치환값
    # param3 -> 변경할 값
    # 변경할 값이 기준값에 속한 값이 아니라면 param2 값으로 치환한다.
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)

    # 이미지 다운로드하기
    # 입력 param1 -> 주소(src)
    # 입력 param2 -> 이미지 저장 디렉토리+파일명+확장자
    urlretrieve( img_src, './webtoon_image/'+title+'.jpg')
    print(title,img_src)
