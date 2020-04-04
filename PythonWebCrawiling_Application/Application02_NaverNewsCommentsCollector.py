# 1. 네이버 뉴스 댓글 수집하기 - 파이썬 레시피 웹 활용 승급편

# requests와 bs4로 할 수 있으나 동적 페이지 크롤링은 약간 난이도가 높다.
# selenium으로 해보고 이후 requsets와 bs4를 이용하여 구현해보자.

# 페이지 분석
# https://sports.news.naver.com/news.nhn?oid=139&aid=0002130942&m_view=1&sort=LIKE
# -> 뉴스 댓글의 내용은 처음 접속 시 전부 받아오는 것이 아니라 나중에 받온다.
# -> 해당 기능은 javascript로 구현되며 기술 이름은 ajax 이다.
# -> selenium이 아닌 requests, bs4를 사용할 경우 다음과 같은 처리를 해야한다.
#   -> 추가로 데이터 요청 (url, 헤더 등)
#   -> 응답 시 데이터 형태
#   -> 응답 데이터의 가공(정규표현식, bs4 등)

from selenium import webdriver
import time
from pprint import pprint

# 모듈, 함수화
# -> 주 기능이 완성되면 모듈로 만들어 사용하도록 한다.
# -> 뉴스의 url 과 시간을 입력받도록 매개변수로 지정한다.
def get_comments(url,imp_time=5,delay_time=0.1):
    #웹드라이버
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(imp_time)
    driver.get(url)


    # 1. 더보기를 계속 클릭
    while True:
        try:
            moreviews= driver.find_element_by_css_selector('a.u_cbox_btn_more')
            moreviews.click()
            time.sleep(delay_time)
        except:
            break

    # 10. 속도개선
    # -> requests와 bs4로 뉴스 댓글을 가져오기 힘든 이유는 동적페이지 였기 때문이다.
    # -> selenium으로 현재 보여지는 화면의 코드를 가져오고, bs4로 구문분석 후 추출해보자.
    from bs4 import BeautifulSoup
    html = driver.page_source
    # html.parser
    soup = BeautifulSoup(html,'html.parser')


    # 2. 댓글 추출
    #속도개선 전
    #contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    #속도개선
    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]
    # 2.5 댓글을 전부 출력
    #for content in contents:
    #    print(content.text)

    # 3. 작성자 추출
    #속도개선 전
    #nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    #속도개선
    nicks = soup.select('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]

    # 4. 날짜추출
    #속도개선 전
    #dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    #속도개선
    dates = soup.select('span.u_cbox_date')
    dates = [date.text for date in dates]

    #5. 좋아요 추출
    #속도개선 전
    #likes = driver.find_elements_by_css_selector('em.u_cbox_cnt_recomm')
    #속도개선
    likes = soup.select('em.u_cbox_cnt_recomm')
    likes = [like.text for like in likes]

    #6. 싫어요 추출
    #속도개선 전
    #disLikes = driver.find_elements_by_css_selector('em.u_cbox_cnt_unrecomm')
    #속도개선
    disLikes = soup.select('em.u_cbox_cnt_unrecomm')
    disLikes = [disLike.text for disLike in disLikes]


    # 7. 취합
    comments = list(zip(nicks,dates,contents,likes,disLikes))
    #pprint(comments)

    driver.quit()
    return comments


# 메인
if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    url = 'https://sports.news.naver.com/news.nhn?oid=413&aid=0000097918&m_view=1&sort=LIKE'

    comment_data = get_comments(url,5,0.1)

    # 8. 엑셀로 저장
    # -> pandas 를 사용하여 저장한다.
    # -> 엑셀 상단의 열의 이름이 될 정보들을 clols에 리스트로 저장한다.
    # sudo apt-get install libbz2-dev
    # sudo pip3 install pandas
    # sudo pip3 install openpyxl
    # fuck...
    # No moudle named '_bz2' 라는 error 가 발생한다.
    # BZIP2 지원으로 파이썬을 재 빌드해야한다.

    #sudo apt-get update
    #sudo apt install libnss3-dev liblzma-dev libbz2-dev

    #파이썬 재설치

    #pandas, openpyxl
    import pandas as pd
    col = ['작성자','날짜','Comments','좋아요','싫어요']
    data_frame = pd.DataFrame(comment_data,columns=col)
    data_frame.to_excel('news5.xlsx',sheet_name='펩 최악의영입List',startrow=0,header=True)

    # 9. 속도측정
    # -> 댓글이 많은 기사일수록 시간이 오래걸린다.
    # -> datetime 모듈을 이용해 시간을 측정해보자.
    end = datetime.now()
    print(end-start)
