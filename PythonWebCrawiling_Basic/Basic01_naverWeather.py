# 1. 네이버 날씨 미세먼지 가져오기 - 파이썬 레시피 웹 활용 입문편

#python 빌드를 위한 패키지 설치
#sudo apt-get update
#sudo apt-get upgrade
#sudo apt-get dist-upgrade
#sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
#sudo apt-get install libncurses5-dev libgdbm-dev libc6-dev
#sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
#sudo apt-get install libssl-dev openssl
#sudo apt-get install libffi-dev

#python 설치
#wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
#sudo tar xvfz Python-3.7.4.tgz
#sudo cd Python-3.7.4
#sudo ./configure --enable-optimizations
#sudo make
#sudo make install
#python3 -V
#sudo apt-get install idle-python3.7
#idle-python3.7


#Beautifulsoup ?
#HTML 및 XML 파일에서 데이터를 가져오는 Python 라이브러리 이다.
#Beautifulsoup 가 가져올 수 있는 page source 는 정적 스크립트이다.
#javascript 로 생성되는 동적 스크립트는 python 의 또다른 라이브러리인 selenium 을 이용해 pulling 한다.
#웹의 어지간한 data 는 beautiful soup 과 selenium 을 통해 가져올 수 있다.

#Beautifulsoup 설치
#sudo apt-get update // 사용가능한 패키지와 그 버전들의 리스트를 업데이트
#sudo apt-get install python3-pip // pip 는 python 라이브러리 패키지 관리 시스템이다
#sudo pip3 install requests
#sudo pip3 install beautifulsoup4


#!/usr/local/bin/python3
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text,'html.parser')
data1 = soup.find('div',{'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
#pprint(data2)

fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)
