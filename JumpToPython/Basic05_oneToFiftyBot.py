# 5. 1 to 50 봇 구현 - 파이썬 레시피 웹 활용 입문편
# http://zzzscore.com/1to50/ 에 구현되어있는 게임을 자동으로 진행하도록 구현

# 1 to 50 코드
# 25개의 버튼은 div로 되어있다.
# -> 게임에 사용되는 모든 버튼 요소 정보를 가져온다.
# -> 각 버튼의 내부 텍스트를 파악하여 몇번 버튼인지 파악한다.
# -> 찾는 숫자면 클릭한다.
# -> xpath를 찾는다.
# //*[@id="grid"]/div[1], //*[@id="grid"]/div[2] ... //*[@id="grid"]/div[25]

from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50/')
driver.implicitly_wait(300)


# xpath 형태로 된 것을 모두 감지한다.
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
#print(len(btns))
#print(btns[0].text)
#print()

# 1번 클릭
#for btn in btns:
#    if btn.text == '1':
#        btn.click()

#1부터 50까지 클릭
#전역변수
num = 1

# 버튼을 찾아서 클릭하기 모듈
def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        print(btn.text, end='\t')
        if btn.text == str(num):
            btn.click()
            print(True)
            num += 1
            return

# 모듈 50번 실행
while num<=50:
    clickBtn()
