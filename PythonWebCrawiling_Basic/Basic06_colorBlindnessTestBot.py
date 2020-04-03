# 6. 색맹테스트 봇 구현 - 파이썬 레시피 웹 활용 입문편
# http://zzzscore.com/color/ 에 구현되어있는 게임을 자동으로 진행하도록 구현


#색맹 테스트 코드
#-> 버튼이 4 -> 9 -> 16 ... 으로 늘어난다.
#-> div로 되어있다.
# xpath
# //*[@id="grid"]/div[1] -> //*[@id="grid"]/div[2] ...
#1to50 봇과 동일하게 진행하면 되지 않을까?
#but, //*[@id="grid"]/div[*]에서 div[]의 *은 찾고자 하는 내부요소가 있는경우만 탐색한다.
#이번에는 <div></div> 사이에 아무런 요소가 없다.
#이 경우 다음과같이 입력해야한다. -> //*[@id="grid"]/div

from selenium import webdriver
from pprint import pprint
import time
from collections import Counter
import time

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div ')
#print(len(btns))

# 정답 탐색 및 클릭 모듈
def analysis():
    # 정답 탐색
    # -> 각 div 의 rgba 값 추출
    # -> 추출한 값 중 다른곳이 정답
    # -> 디자인 정보(css) 추출
    # selenium의 value_of_css_property 로 해당 요소의 css 속성을 확인할 수 있다.
    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    #pprint(btns_rgba)

    #정답찾기
    # from collections import Counter 참조
    result = Counter(btns_rgba)
    #pprint(result) # value가 1이면 정답

    #value 1 탐색
    for key, value in result.items():
        if value == 1:
            answer = key
            break
    else:
        answer = None
        print("정답을 찾을 수 없음")


    #정답 누르기
    #-> answer에 저장된 색이 어느 위치에 있는지 btins_rgba에서 찾는다.
    #-> 해당 인덱스로 btns에 저장되어있는 요소를 찾아 클릭한다.
    if answer :
        index = btns_rgba.index(answer)
        btns[index].click()


#제한시간동안 실행
if __name__=="__main__":
    start = time.time()
    while time.time() - start <= 60:
        analysis()
